'''수행과제
password.txt 파일을 읽어온다.
카이사르의 암호를 풀 수 있는 함수를 caesar_cipher_decode() 라는 이름으로 만든다.
caesar_cipher_decode() 함수는 풀어야 하는 문자열을 파라메터로 추가한다. 이때 파라메터의 이름은 target_text으로 한다.
caesar_cipher_decode() 에서 자리수에 따라 암호표가 바뀌게 한다. 자리수는 알파벳 수만큼 반복한다.
자리수에 따라서 해독된 결과를 출력한다.
몇 번째 자리수로 암호가 해독되는지 찾아낸다. 눈으로 식별이 가능하면 해당 번호를 입력하면 그 결과를 result.txt로 저장을 한다.

제약사항
python에서 기본 제공되는 명령어 이외의 별도의 라이브러리나 패키지를 사용해서는 안된다.
반복 할 때마다 결과를 눈으로 확인 할 수 있어야 한다.
경고 메시지 없이 모든 코드는 실행 되어야 한다.
파일을 다루는 부분은 모두 예외처리가 되어 있어야 한다.
암호가 확인 되었을 때 최종 암호가 result.txt로 저장되어야 한다.

보너스 과제
텍스트 사전을 만들고 사전에 있는 단어와 일치하는 키워드가 암호속에서 발견될 경우 반복을 멈출 수 있게 작성해 보시오.

'''
chars = string.ascii_lowercase + string.digits

try:
    password_file = open('password.txt', 'r')
    password = password_file.read()
    password_file.close()
except:
    print('파일을 열지 못했습니다.')
    quit()

def caesar_cipher_decode(target_text):
    for i in range(26):
        result = ''
        for char in target_text:
            if char in chars:
                char_index = chars.find(char)
                result += chars[(char_index - i) % 26]
print(password)