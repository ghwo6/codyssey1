'''
수행과제
emergency_storage_key.zip 의 암호를 풀 수 있는 코드를 작성한다.
단 암호는 특수 문자없이 숫자와 소문자 알파벳으로 구성된 6자리 문자로 되어 있다.
암호를 푸는 코드를 unlock_zip() 이라는 이름으로 함수로 만든다.
암호를 푸는 과정을 출력하는데 시작 시간과 반복 회수 그리고 진행 시간등을 출력한다.
암호를 푸는데 성공하면 암호는 password.txt로 저장한다.
암호를 풀 수 있는 전체 코드는 door_hacking.py로 저장한다.

제약사항
python에서 기본 제공되는 명령어 이외의 별도의 라이브러리나 패키지를 사용해서는 안된다.
단 zip 파일을 다루는 부분은 외부 라이브러리 사용 가능하다.
파일을 다루는 부분은 예외처리가 되어있어야 한다.
경고 메시지 없이 모든 코드는 실행 되어야 한다.

보너스 과제
암호를 좀 더 빠르게 풀 수 있는 알고리즘을 제시하고 코드로 구현한다.

'''

'''
import shutil
import zipfile

'''

import zipfile
import time

fileName = r'02_01/emergency_storage_key.zip'

output_dir = r'02_01/emergency_storage'

password_ch = [chr(i) for i in range(97,123)] + [str(i) for i in range(10)]

def unlock_zip():
    start_time = time.time()

    zip_file1 = zipfile.ZipFile(fileName,output_dir,'r')
    for i1 in password_ch:
        for i2 in password_ch:
            for i3 in password_ch:
                for i4 in password_ch:
                    for i5 in password_ch:
                        for i6 in password_ch:
                            password = str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6)
                            print(password)
                            zip_file1.setpassword(password.encode())
                            try:
                                zip_file1.extractall(output_dir)
                                zip_file1.close()
                                print(password + "풀었다.")
                                return print(time.time  - start_time)
                            except:
                                print(time)
                                pass


unlock_zip()


                        
                            
