import numpy as np
import os

print(np.__version__)

csv_list = ['mars_base_main_parts-001.csv','mars_base_main_parts-002.csv','mars_base_main_parts-003.csv']

# 집어 넣을 np.darray 데이터
list_np = np.array(('',1))
print(list_np)

def read_csv_files_to_npArray(filename:str):
    data = np.genfromtxt(os.path.join(r'01_05',filename),delimiter=',',dtype=None,encoding='UTF-8')
    print(data)
    return data


for i in csv_list:
    list_np = np.concatenate((list_np,read_csv_files_to_npArray(i)))
print(list_np)