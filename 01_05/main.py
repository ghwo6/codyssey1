'''
[수행과제]
numpy를 사용하기 위해서 import를 한다.
mars_base_main_parts-001.csv,
mars_base_main_parts-002.csv,
mars_base_main_parts-003.csv 파일들을
모두 numpy를 사용해서 읽어들여서 각각 arr1, arr2, arr3 과 같이 ndarray 타입으로 가져온다.
3개의 배열을 하나로 합치고(merge) 이름을 parts 라는 ndarray 를 생성한다.
parts를 이용해서 각 항목의 평균값을 구한다.
평균값이 50 보다 작은 값을 뽑아내서 parts_to_work_on.csv 라는 파일로 별도로 저장한다.
작성된 코드는 design_dome.py 라는 이름으로 저장한다.

[제약사항]
Python에서 기본 제공되는 명령어만 사용해야 하며 별도의 라이브러리나 패키지를 사용해서는 안된다.
numpy는 추가로 사용 할 수 있다.
파일로 저장하는 부분에는 반드시 예외처리가 되어 있어야 한다.

[보너스 과제]
parts_to_work_on.csv를 읽어서 parts2라는 ndarray에 저장한다.
parts2의 내용을 기반으로 전치행렬을 구하고 그 내용을 parts3에 저장하고 출력한다.


'''


import numpy as np
import os

print(np.__version__)

csv_list = ['mars_base_main_parts-001.csv','mars_base_main_parts-002.csv','mars_base_main_parts-003.csv']
folderName = '01_05' +os.sep


list_np = None

def csv_to_ndarray(file_name:str):
    return np.loadtxt(folderName+file_name, delimiter=',', skiprows=1, dtype=[('part_name', 'U50'), ('quantity', int)])

arr1 = csv_to_ndarray(csv_list[0])
arr2 = csv_to_ndarray(csv_list[1])
arr3 = csv_to_ndarray(csv_list[2])

print(arr1)
print(arr2)
print(arr3)

print(arr1.shape)
print(arr2.shape)
print(arr3.shape)


parts = np.concatenate([arr1,arr2,arr3])
print(parts)


# 이름들만 모으자
name = []

# print(parts.shape[0])

for i in range(parts.shape[0]):
    if parts[i][0] in name:
        pass
    else:
        name.append(str(parts[i][0]))
print(name)

# 중복 지우기
name = list(tuple(name))
print(name)

mean_parts = {}

temp = []
# 이름마다 반복
for n in name:
    div = 0
    # 한 줄마다 반복
    for i in range(parts.shape[0]):
        if parts[i][0] == n:
            temp.append(parts[i][1])
            div += 1
    mean_parts[str(n)] = round(float(sum(temp)/div),2)
    temp.clear()

print(mean_parts)

output_filename = os.path.join('01_05', 'parts_to_work_on.csv')
try:
    savefile = open(output_filename,'wt',encoding='utf-8')
except:
    print('파일이 열리지 않습니다.')
