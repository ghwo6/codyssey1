import zipfile
import itertools
import string
import time
import os
import io
from multiprocessing import Pool, Manager, cpu_count

def find_password(args):
    """
    각 프로세스에서 실행될 작업 함수.
    할당된 암호 조합을 검사합니다.
    """
    zip_data_bytes, char_subset, found_event, result_queue = args
    
    try:
        # 메모리에 로드된 zip 데이터로 ZipFile 객체 생성
        zip_file = zipfile.ZipFile(io.BytesIO(zip_data_bytes))
    except zipfile.BadZipFile:
        # 유효하지 않은 zip 데이터인 경우, 이 프로세스는 작업을 중단
        return None

    # 주어진 문자(char_subset)로 시작하는 모든 암호 조합 생성
    # 예: 'a'가 주어지면 'a'로 시작하는 모든 6자리 암호 검사
    password_length = 6
    chars = string.ascii_lowercase + string.digits
    password_generator = itertools.product(chars, repeat=password_length - 1)

    for p_tuple in password_generator:
        # 다른 프로세스가 이미 암호를 찾았다면 현재 작업 중단
        if found_event.is_set():
            return None
            
        password = char_subset + ''.join(p_tuple)
        
        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            
            # 암호 찾기 성공!
            found_event.set()  # 다른 모든 프로세스에 중단 신호 전송
            result_queue.put(password) # 결과 큐에 암호 저장
            return password
        except:
            # 암호가 틀리면 계속 진행
            continue
            
    return None

def unlock_zip_parallel(zip_file_name='02_01/emergency_storage_key.zip'):
    """
    멀티프로세싱을 사용하여 zip 파일 암호를 병렬로 탐색합니다.
    """
    print('=' * 40)
    print('🚀 Starting parallel password search...')
    print(f"Target file: {zip_file_name}")
    print('=' * 40)

    # 1. ZIP 파일을 메모리로 미리 로딩 (Disk I/O 최소화)
    try:
        with open(zip_file_name, 'rb') as f:
            zip_data = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{zip_file_name}' was not found.")
        return

    start_time = time.time()
    
    # 사용할 문자셋과 CPU 코어 수 설정
    chars = string.ascii_lowercase + string.digits
    num_processes = cpu_count()
    print(f"Utilizing {num_processes} CPU cores for the search.")
    print('-' * 40)

    # 멀티프로세싱 환경 설정
    with Manager() as manager:
        found_event = manager.Event()  # 암호 발견 시 다른 프로세스를 중지시키는 신호
        result_queue = manager.Queue() # 결과를 저장할 큐

        # 각 프로세스에 작업을 분배
        # ('a', zip데이터, 이벤트, 큐), ('b', zip데이터, 이벤트, 큐)... 와 같이 작업을 나눔
        tasks = [(zip_data, char, found_event, result_queue) for char in chars]

        # 프로세스 풀(Pool) 생성 및 작업 실행
        with Pool(processes=num_processes) as pool:
            pool.map_async(find_password, tasks)
            
            # 작업이 끝날 때까지 대기
            pool.close()
            pool.join()

        # 결과 확인
        if not result_queue.empty():
            password = result_queue.get()
            total_time = time.time() - start_time
            
            print("\n" + "=" * 40)
            print("✔️ Password found!")
            print(f"Password: {password}")
            print(f"Total time: {total_time:.2f} seconds")
            print("=" * 40)
            
            try:
                with open('02_01password.txt', 'w') as f:
                    f.write(password)
                print("Password successfully saved to 'password.txt'.")
            except IOError as e:
                print(f"Error: Could not write password to file. {e}")
        else:
            print("\n❌ Password not found after checking all combinations.")


if __name__ == '__main__':
    unlock_zip_parallel()