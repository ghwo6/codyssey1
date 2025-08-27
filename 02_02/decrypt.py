
import os

PASSWORD_FILE = "02_01/password.txt"
RESULT_FILE = "02_02/result.txt"
ALPHABET_SIZE = 26


def apply_caesar_shift(text, shift):
    """
    주어진 텍스트에 카이사르 암호 시프트를 적용하여 해독된 문자열을 반환합니다.
    
    Args:
        text (str): 해독할 원본 문자열.
        shift (int): 적용할 시프트 값 (0-25).

    Returns:
        str: 시프트가 적용된 해독된 문자열.
    """
    decoded_chars = []
    for char in text:
        if 'a' <= char <= 'z':
            # 소문자 처리: 아스키 코드를 기준으로 시프트 적용 후 알파벳 범위를 벗어나지 않도록 나머지 연산
            shifted_char = chr((ord(char) - ord('a') - shift + ALPHABET_SIZE) % ALPHABET_SIZE + ord('a'))
        elif 'A' <= char <= 'Z':
            # 대문자 처리: 위와 동일
            shifted_char = chr((ord(char) - ord('A') - shift + ALPHABET_SIZE) % ALPHABET_SIZE + ord('A'))
        else:
            # 알파벳이 아닌 문자는 그대로 유지
            shifted_char = char
        decoded_chars.append(shifted_char)
    
    return ''.join(decoded_chars)

def caesar_cipher_decode(target_text):
    """
    주어진 텍스트에 대해 모든 가능한 카이사르 시프트(0-25) 결과를 화면에 출력합니다.
    (요구사항에 명시된 함수)
    
    Args:
        target_text (str): 해독을 시도할 암호문.
    """
    print('--- Trying all 26 possible shifts ---\n')
    for shift_key in range(ALPHABET_SIZE):
        result = apply_caesar_shift(target_text, shift_key)
        # {shift_key:2}는 숫자를 두 자리 공간에 오른쪽 정렬하여 출력합니다.
        print(f'Shift {shift_key:2}: {result}')
    print('\n' + '-' * 40)

def get_correct_shift_from_user():
    """
    사용자로부터 올바른 시프트 값을 입력받아 반환합니다.
    0-25 사이의 유효한 정수가 입력될 때까지 반복합니다.

    Returns:
        int: 사용자가 선택한 시프트 값.
    """
    while True:
        try:
            shift_input = input('Enter the shift number that reveals the correct message: ')
            shift_num = int(shift_input)
            if 0 <= shift_num < ALPHABET_SIZE:
                return shift_num
            else:
                print(f'[WARNING] Please enter a number between 0 and {ALPHABET_SIZE - 1}.')
        except ValueError:
            print('[ERROR] Invalid input. Please enter a whole number.')

def main():
    """
    프로그램의 메인 로직을 실행합니다.
    파일 읽기, 모든 경우의 수 출력, 사용자 입력, 최종 결과 저장 순으로 진행됩니다.
    """
    # 1. 암호 파일 읽기
    try:
        with open(PASSWORD_FILE, 'r', encoding='utf-8') as f:
            ciphertext = f.read().strip()
    except FileNotFoundError:
        print(f"[CRITICAL ERROR] Password file not found at: {PASSWORD_FILE}")
        sys.exit(1) # 파일이 없으면 프로그램 종료

    # 2. 모든 가능한 해독 결과 출력
    caesar_cipher_decode(ciphertext)

    # 3. 사용자로부터 올바른 시프트 값 입력받기
    correct_shift = get_correct_shift_from_user()

    # 4. 최종 해독문 생성
    final_result = apply_caesar_shift(ciphertext, correct_shift)

    # 5. 결과 파일에 저장
    try:
        with open(RESULT_FILE, 'w', encoding='utf-8') as f:
            f.write(final_result)
        print(f"\n[SUCCESS] Decoded text has been saved to {RESULT_FILE}")
        print(f"  - Shift Key Used: {correct_shift}")
        print(f"  - Decoded Text: {final_result}")
    except IOError as e:
        print(f"[CRITICAL ERROR] Failed to write to result file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()