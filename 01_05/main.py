import numpy as np
import os

print(np.__version__)

csv_list = ['mars_base_main_parts-001.csv','mars_base_main_parts-002.csv','mars_base_main_parts-003.csv']


list_np = None

def read_csv_files_to_npArray(np1:np.ndarray,filename:str):
    with open('.\01_05'+f'{filename}','rt',encoding='UTF-8') as csv_data:
        read_list = csv_data.read().split()
        l = list()
        for i in read_list:

            l.append(i.split(','))
        print(np.array(l[1::]))


read_csv_files_to_npArray(list_np,csv_list[0])