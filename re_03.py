import numpy as np
import os

print(np.__version__)

csv_list = ['mars_base_main_parts-001.csv','mars_base_main_parts-002.csv','mars_base_main_parts-003.csv']


arr1 = np.genfromtxt(os.path.join(r'01_05',csv_list[0]),delimiter=',',skip_header=1,dtype=None,encoding='UTF-8')
arr2 = np.genfromtxt(os.path.join(r'01_05',csv_list[1]),delimiter=',',skip_header=1,dtype=None,encoding='UTF-8')
arr3 = np.genfromtxt(os.path.join(r'01_05',csv_list[2]),delimiter=',',skip_header=1,dtype=None,encoding='UTF-8')

parts = np.concatenate((arr1,arr2,arr3),axis=0)

# print(parts)
# print(parts.shape)
# print(parts.ndim)

# print(arr1)
# print(arr1.shape)
# print(arr1.ndim)

print(parts)
print(parts[0][0])
for l in parts:
    print(l[0])
parts_set = set()
parts_list = list()
# for l in parts:
#     parts_set.add(l[0])
#     parts_list.append(l[0])

for l1,l2 in parts.tolist():
    print(l1)
    parts_list.append(l1)
# print(parts_set)
# print()
# print(parts_list)
# print(parts_list)

# 여기서 보니까 중복된 값이 만들어 진다.
# parts_list = list(set(parts_list))
# st = list(parts_set)
# for i in parts_list:
#     print(f'{i}의 갯수는 {parts_list.count(i)} 입니다. 1이 맞는지 확인해주세요.')

# 세트로 만들어보자 -> 중복이 없는 재료들을 구하기 위해 중복되지 않은 set(집합)을 생각함
parts_set = set(parts_list)

print('세트 출력')
print(parts_set)
# 정말로 중복된 값이 없는지 확인하고 싶다. -> 리스트로 바꿔서 확인해보자 -> 위에서 확인해보자
parts_list = list(parts_set)
for i in parts_list:
    print(f'{i}의 갯수는 {parts_list.count(i)} 입니다. 1이 맞는지 확인해주세요.')


