import os
import datetime
import sounddevice as sd
from scipy.io.wavfile import write

# 녹음 관련 설정
SAMPLE_RATE = 44100  # 샘플링 속도 (Hz)
RECORD_DIRECTORY = '02_07/records'  # 녹음 파일 저장 폴더

def record_audio():
    """
    사용자의 마이크 입력을 받아 오디오 파일로 저장합니다.
    파일 이름은 '년월일-시간분초.wav' 형식으로 생성됩니다.
    """
    # records 폴더가 없으면 생성
    if not os.path.exists(RECORD_DIRECTORY):
        os.makedirs(RECORD_DIRECTORY)
        print(f"'{RECORD_DIRECTORY}' 폴더를 생성했습니다.")

    try:
        duration_input = input('녹음할 시간(초)을 입력하세요 (예: 5): ')
        duration = int(duration_input)
        
        print(f'\n{duration}초 동안 녹음을 시작합니다...')
        
        # 오디오 녹음 실행
        recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=2, dtype='int16')
        sd.wait()  # 녹음이 끝날 때까지 대기
        
        print('녹음이 완료되었습니다.')
        
        # 파일명 생성을 위한 현재 시간 정보
        now = datetime.datetime.now()
        filename = now.strftime('%Y%m%d-%H%M%S') + '.wav'
        filepath = os.path.join(RECORD_DIRECTORY, filename)
        
        # 녹음된 데이터를 WAV 파일로 저장
        write(filepath, SAMPLE_RATE, recording)
        
        print(f"녹음 파일이 '{filepath}' 경로에 저장되었습니다.")
        
    except ValueError:
        print('오류: 유효한 숫자를 입력해주세요.')
    except Exception as e:
        print(f'녹음 중 오류가 발생했습니다: {e}')


def main():
    """
    메인 실행 함수. 사용자에게 메뉴를 보여주고 선택에 따라 기능을 실행합니다.
    """
    print('="자비스가 필요해!" 프로그램을 시작합니다.=')
    while True:
        print('\n[메뉴]')
        print('1. 음성 녹음 시작')
        print('2. 종료')
        
        choice = input('원하는 기능의 번호를 입력하세요: ')
        
        if choice == '1':
            record_audio()
        elif choice == '2':
            print('프로그램을 종료합니다.')
            break
        else:
            print('잘못된 입력입니다. 1, 2 중에서 선택해주세요.')

if __name__ == '__main__':
    main()