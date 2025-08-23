# 수행과제
# Mars_Base_Inventory_List.csv 의 내용을 읽어 들어서 출력한다.
# Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환한다.
# 배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬한다.
# 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다.
# 인화성 지수가 0.7 이상되는 목록을 CSV 포멧(Mars_Base_Inventory_danger.csv)으로 저장한다.

import os

print(os.getcwd())
os.chdir(r'.\01_03')
print(os.getcwd())

print('csv파일을 읽습니다.')
try:
    with open('Mars_Base_Inventory_List.csv','rt',encoding="UTF-8") as file1:
        csv_str = file1.read()
except:
    print('파일이 열리지 않습니다.')
    exit()

# print(csv_str)



csv_list_temp = csv_str.splitlines()
# print('csv_list_temp 를 출력합니다.')
# for i in csv_list_temp:
#     print(i)

csv_list = []

# 코드를 잘못짯다.
# 숫자로 인덱싱 할 방법을 떠올리지 못하겠다.
# for i in csv_list_temp[1:-1]:
#     csv_list = i.split(',')
# csv_list_temp[1:-1]까지는 잘했다고 보나 csv_list의 요소를 인덱싱 할 방법이 없다.
# 아래에서 해결함

# 마지막 줄을 뺴먹엇었다.
# for i in csv_list_temp[1:-1]:

for i in csv_list_temp[1:]:
    csv_list.append(i.split(','))


# print("csv_list 를 출력합니다.")
# for i in csv_list:
#     print(i)



# csv_list_sorted = []
# for i in csv_list:
#     for j in i:
#         csv_list_sorted[i][j] = j

# 문제 발생
# csv_list_sorted = [["","","","",0]]*len(csv_list)

# for i in range(1,len(csv_list)-1):
#     for j in range(0,5):
#         csv_list_sorted[i][j] = csv_list[i][j]

# print("csv_list_sorted를 정렬하기 전에 출력합니다.")
# for i in csv_list_sorted:
#     for j in i:
#         print(j)
#     print()

csv_list_sorted = []
# csv_list_sorted.append([inner_list[:] for inner_list in csv_list])

csv_list_sorted = [inner_list[:] for inner_list in csv_list]

# print("\n정렬 전에 csv_list_sorted를 출력합니다.\n")
# for i in csv_list_sorted:
#     for j in i:
#         print(f"{j}",end=" ")
#     print()

temp_list = []

for i in range(len(csv_list_sorted)):
    for j in range(len(csv_list_sorted)-1-i):
        if float(csv_list_sorted[j][4]) < float(csv_list_sorted[j+1][4]):
            temp_list = csv_list_sorted[j+1]
            csv_list_sorted[j+1] = csv_list_sorted[j]
            csv_list_sorted[j] = temp_list


# print("csv_list_sorted를 정렬한 후 출력합니다.")
# for i in range(len(csv_list_sorted)):
#     for j in range(0,5):
#         print(f"\"{csv_list_sorted[i][j]}\"",end=" ")
#     print()

try:
    csv_file = open(r'Mars_Base_Inventory_danger.csv','wt',encoding="UTF-8")
except:
    print('에러 발생')
    exit()

print("인화성이 0.7이상인 값을 출력합니다.")
for i in range(len(csv_list_sorted)):
    if float(csv_list_sorted[i][4]) >=0.7:

        csv_file.write(','.join([csv_list_sorted[i][0],csv_list_sorted[i][1],csv_list_sorted[i][2],csv_list_sorted[i][3],csv_list_sorted[i][4]]))
        csv_file.write('\n')
        # print(','.join([csv_list_sorted[i][0],csv_list_sorted[i][1],csv_list_sorted[i][2],csv_list_sorted[i][3],csv_list_sorted[i][4]]))
        
        for j in range(5):
            # print(f"\'{csv_list_sorted[i][j]}\'",end=" ")
            print(f"{csv_list_sorted[i][j]}",end=" ")
        print()

print('인화성이 0.7이상인 성분들을 Mars_Base_Inventory_danger.csv에 저장했습니다.')
csv_file.close()