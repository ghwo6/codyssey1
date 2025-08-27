import os
import cv2

def find_people_in_cctv():
    """
    CCTV 사진들이 있는 폴더를 검색하여 사람이 포함된 이미지를 찾아 표시합니다.
    """
    # 1. 사진 목록 가져오기 및 이미지 파일 필터링
    image_dir = '02_10/images'
    allowed_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    
    try:
        # 지정된 디렉토리의 파일 목록을 가져옵니다.
        all_files = os.listdir(image_dir)
        # 이미지 파일 형식인 것만 필터링합니다.
        image_files = [f for f in all_files if f.lower().endswith(allowed_extensions)]
    except FileNotFoundError:
        print(f"오류: '{image_dir}' 폴더를 찾을 수 없습니다. 폴더를 생성하고 이미지를 넣어주세요.")
        return

    if not image_files:
        print(f"'{image_dir}' 폴더에 이미지 파일이 없습니다.")
        return

    # OpenCV에서 제공하는 HOG 기반 사람 탐지기 초기화
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # 2. 순차적으로 사진 검색 및 사람 찾기
    for filename in image_files:
        # 이미지 파일 경로 생성
        image_path = os.path.join(image_dir, filename)
        
        # 이미지 읽기
        image = cv2.imread(image_path)
        
        # 이미지 파일이 아니거나 손상된 경우 건너뛰기
        if image is None:
            print(f"'{filename}' 파일을 읽을 수 없습니다. 건너뜁니다.")
            continue

        # 사람 탐지 (detectMultiScale은 사람을 찾으면 (x, y, w, h) 좌표 목록을 반환)
        # winStride와 padding은 탐지 정확도와 속도에 영향을 주는 파라미터입니다.
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
        
        # 3. 사람을 찾으면 화면에 이미지 출력
        if len(rects) > 0:
            print(f"'{filename}' 파일에서 사람을 {len(rects)}명 찾았습니다. 'Enter' 키를 누르면 계속 진행합니다.")
            
            # 4. (보너스 과제) 사람을 찾아 빨간색 사각형으로 표시
            for (x, y, w, h) in rects:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # 이미지 출력
            cv2.imshow('Person Detected', image)
            
            # 5. 엔터키를 누르면 다음 사진 검색
            # cv2.waitKey(0)는 아무 키나 입력될 때까지 무한정 대기합니다.
            # Enter 키(ASCII 13)만 특정하려면 반복문으로 확인할 수 있으나,
            # 문제의 의도는 '일시 정지'이므로 any key로 구현합니다.
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    # 6. 검색 완료 메시지 출력
    print('모든 사진 검색이 끝났습니다.')

if __name__ == '__main__':
    find_people_in_cctv()