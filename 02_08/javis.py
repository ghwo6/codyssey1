import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import csv

# PEP 8 스타일 가이드 준수
# 함수 이름은 소문자와 언더스코어 사용
# 변수 할당 시 '=' 양쪽에 공백 추가

def transcribe_audio_to_csv(audio_path, output_dir):
    """
    음성 파일을 텍스트로 변환하고 시간 정보와 함께 CSV 파일로 저장합니다.

    Args:
        audio_path (str): 변환할 음성 파일의 경로
        output_dir (str): CSV 파일을 저장할 디렉토리 경로
    """
    # 파일명과 확장자 분리
    filename = os.path.basename(audio_path)
    name, _ = os.path.splitext(filename)
    csv_path = os.path.join(output_dir, f'{name}.csv')

    print(f"'{filename}' 파일 처리를 시작합니다...")

    try:
        # 음성 파일 로드
        sound = AudioSegment.from_file(audio_path)
    except Exception as e:
        print(f"'{filename}' 파일을 로드할 수 없습니다: {e}")
        return

    # 음성이 없는 부분을 기준으로 파일 분할 (silence_thresh와 min_silence_len 조정 가능)
    # silence_thresh: 데시벨(dBFS) 단위로, 이 값보다 조용하면 침묵으로 간주
    # min_silence_len: 밀리초(ms) 단위로, 최소 침묵 시간
    chunks = split_on_silence(
        sound,
        min_silence_len=500,
        silence_thresh=sound.dBFS - 14,
        keep_silence=500
    )

    if not chunks:
        print(f"'{filename}' 파일에서 음성을 감지할 수 없습니다.")
        return

    # Recognizer 객체 생성
    recognizer = sr.Recognizer()
    transcription_data = []
    current_time_ms = 0

    # 분할된 각 음성 조각을 텍스트로 변환
    for i, chunk in enumerate(chunks):
        chunk_path = f'chunk{i}.wav'
        chunk.export(chunk_path, format='wav')

        with sr.AudioFile(chunk_path) as source:
            audio_listened = recognizer.record(source)
            try:
                # Google Web Speech API를 사용하여 텍스트로 변환 (한국어 설정)
                text = recognizer.recognize_google(audio_listened, language='ko-KR')
                
                # 시간(초)과 인식된 텍스트 저장
                start_time_sec = current_time_ms / 1000
                transcription_data.append([f'{start_time_sec:.2f}', text])
                print(f"  {start_time_sec:.2f}s: {text}")

            except sr.UnknownValueError:
                # 음성을 인식할 수 없는 경우
                pass
            except sr.RequestError as e:
                # API 요청에 실패한 경우
                print(f"  API 요청 오류 발생: {e}")
        
        # 다음 조각의 시작 시간을 계산하기 위해 현재 조각의 길이를 더함
        # 실제 침묵 길이도 고려해야 하지만, 여기서는 조각의 길이만으로 근사
        current_time_ms += len(chunk)
        os.remove(chunk_path) # 임시 파일 삭제

    # CSV 파일로 저장
    if transcription_data:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['time', 'text'])  # 헤더
            writer.writerows(transcription_data)
        print(f"'{csv_path}' 파일에 변환 내용이 저장되었습니다.")
    else:
        print(f"'{filename}' 파일에서 변환할 텍스트를 찾지 못했습니다.")


def search_keyword_in_csvs(search_dir, keyword):
    """
    보너스 과제: 지정된 디렉토리의 CSV 파일들에서 키워드를 검색합니다.

    Args:
        search_dir (str): 검색할 CSV 파일들이 있는 디렉토리 경로
        keyword (str): 검색할 키워드
    """
    print(f"\n--- '{keyword}' 키워드 검색 시작 ---")
    found = False
    for filename in os.listdir(search_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(search_dir, filename)
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                # 헤더 스킵
                next(reader, None) 
                for row in reader:
                    if len(row) >= 2 and keyword in row[1]:
                        print(f"  - 파일: {filename}, 시간: {row[0]}s, 내용: {row[1]}")
                        found = True
    if not found:
        print(f"'{keyword}'를 포함하는 내용을 찾지 못했습니다.")


# --- 메인 실행 부분 ---
if __name__ == '__main__':
    # 음성 파일이 저장된 디렉토리 (상황에 맞게 변경)
    AUDIO_DIR = '02_08/audio_files'
    # CSV 파일이 저장될 디렉토리
    CSV_OUTPUT_DIR = '02_08/csv_results'

    # 디렉토리가 없으면 생성
    if not os.path.exists(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)
        print(f"'{AUDIO_DIR}' 디렉토리가 생성되었습니다. 음성 파일을 넣어주세요.")

    if not os.path.exists(CSV_OUTPUT_DIR):
        os.makedirs(CSV_OUTPUT_DIR)

    # 1. STT 변환 및 CSV 저장 수행
    audio_files = [f for f in os.listdir(AUDIO_DIR) if f.endswith(('.wav', '.mp3', '.m4a'))]
    if not audio_files:
        print(f"'{AUDIO_DIR}' 디렉토리에 처리할 음성 파일이 없습니다.")
    else:
        for audio_file in audio_files:
            full_path = os.path.join(AUDIO_DIR, audio_file)
            transcribe_audio_to_csv(full_path, CSV_OUTPUT_DIR)