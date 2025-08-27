import os
import zipfile
# 이미지 처리 및 화면 출력을 위해 pygame 외부 라이브러리를 사용합니다.
# 제약조건에 따라 이 부분은 외부 라이브러리 사용이 허용됩니다. [cite: 16]
# 터미널에서 'pip install pygame' 명령어로 설치해야 합니다.
import pygame

class MasImageHelper:
    """
    화성 CCTV 이미지를 처리하고 관리하는 클래스입니다. [cite: 20, 21]

    이 클래스는 지정된 디렉토리에서 이미지 파일을 찾아 목록을 관리하고,
    이전/다음 이미지로 쉽게 이동할 수 있는 기능을 제공합니다.
    """
    def __init__(self, path):
        """
        클래스 초기화. 이미지 디렉토리 경로를 받아 이미지 목록을 생성합니다.
        """
        self.path = path
        self.images = []
        self.index = 0
        
        # 유효한 이미지 파일 확장자 정의
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        
        # 디렉토리가 존재하면 이미지 파일 목록을 정렬하여 저장
        if os.path.isdir(self.path):
            files = sorted(os.listdir(self.path))
            for file in files:
                # 파일 확장자를 소문자로 변환하여 이미지 파일인지 확인
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    self.images.append(os.path.join(self.path, file))

        if not self.images:
            print(f"'{self.path}' 디렉토리에서 이미지를 찾을 수 없습니다.")

    def get_current_image_surface(self):
        """
        현재 인덱스에 해당하는 이미지를 pygame Surface 객체로 불러옵니다.
        이미지 목록이 비어있으면 None을 반환합니다.
        """
        if not self.images:
            return None
        return pygame.image.load(self.images[self.index])

    def next_image(self):
        """
        다음 이미지로 인덱스를 이동합니다. 마지막 이미지면 처음으로 돌아갑니다.
        """
        if not self.images:
            return
        self.index = (self.index + 1) % len(self.images)

    def prev_image(self):
        """
        이전 이미지로 인덱스를 이동합니다. 첫 이미지면 마지막으로 돌아갑니다.
        """
        if not self.images:
            return
        self.index = (self.index - 1 + len(self.images)) % len(self.images)

def main():
    """
    메인 실행 함수.
    CCTV.zip 압축 해제, 이미지 뷰어 실행 및 사용자 입력을 처리합니다.
    """
    zip_file = '02_09/CCTV.zip'
    extract_folder = '02_09/CCTV/'

    # 1. CCTV.zip 파일의 압축을 해제하여 CCTV 폴더를 만듭니다. 
    if os.path.exists(zip_file):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall('./02_09/CCTV/')
        print(f"'{zip_file}' 파일의 압축을 '{extract_folder}' 폴더에 해제했습니다.")
    else:
        print(f"'{zip_file}'을 찾을 수 없습니다. '{extract_folder}' 폴더가 이미 있는지 확인합니다.")

    if not os.path.isdir(extract_folder):
        print(f"'{extract_folder}' 폴더를 찾을 수 없어 프로그램을 종료합니다.")
        return

    # MasImageHelper 클래스 인스턴스 생성
    image_helper = MasImageHelper(extract_folder)

    # 이미지가 없는 경우 프로그램 종료
    if not image_helper.images:
        return

    # Pygame 초기화
    pygame.init()

    # 2. 첫 번째 이미지를 읽어 화면에 출력합니다. 
    # 첫 이미지 크기에 맞춰 화면 크기 설정
    initial_image = image_helper.get_current_image_surface()
    screen_size = initial_image.get_size()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('화성 기지 외부 CCTV')
    
    screen.blit(initial_image, (0, 0))
    pygame.display.flip()

    # 메인 루프: 사용자 입력(키보드) 대기
    running = True
    while running:
        for event in pygame.event.get():
            # 창 닫기 버튼을 누르면 종료
            if event.type == pygame.QUIT:
                running = False
            
            # 키보드 키를 눌렀을 때
            if event.type == pygame.KEYDOWN:
                current_image = None
                # 3. 왼쪽/오른쪽 방향 키에 따라 이전/다음 사진을 보여줍니다. 
                if event.key == pygame.K_LEFT:
                    image_helper.prev_image()
                    current_image = image_helper.get_current_image_surface()
                elif event.key == pygame.K_RIGHT:
                    image_helper.next_image()
                    current_image = image_helper.get_current_image_surface()
                
                # 이미지가 변경되었으면 화면을 다시 그림
                if current_image:
                    # 창 크기를 새 이미지 크기에 맞게 조절
                    screen = pygame.display.set_mode(current_image.get_size())
                    screen.blit(current_image, (0, 0))
                    pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()