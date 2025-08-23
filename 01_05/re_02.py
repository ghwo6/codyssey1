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

for (l1,l2) in parts:
    parts_list.append(l1)
# print(parts_set)
print()
print(parts_list)