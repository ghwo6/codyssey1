import os
import json
# log_line은 log데이터를 리스트 객체를 받는다.

log_list = []

log_json = {}
count_while = 0

try:
    with open("D:\\study\Codyssey\\01_02\\mission_computer_main.log","rt",encoding="UTF_8") as input_file:
        
        #파일을 열어서 처리하는 함수 입력 input_file에서 log _line으로 변경 및 
        for line in input_file.readlines():
            log_list.append(line.strip('\n'))

except:
    print("mission_computer_main.log 파일을 열 수 없습니다.")
    exit()

        # 한줄씩 취합한 데이터(log_list)를 출력한다.
print('그대로 출력함')
for i in log_list:
    print(i)
        
print('\n시간의 역순으로 출력함\n')
for i in reversed(log_list):
    print(i)

# json으로 데이터를 추가하자

print('데이터를 Json형식에 추가한다.')

for line in log_list:
            
    time, event, message = line.split(',')

    # log_json.update(time,message)
    log_json[time] = message

    # json데이터를 출력한다.
# print('Json 데이터를 출력한다')
# for k,v in log_json.items():
#     print(k,v)

try:
    with open("D:\\study\Codyssey\\01_02\\mission_computer_main.json","wt",encoding="UTF-8") as output_file:
        
        #JSON형식으로 저장하는 함수 입력
        # print('JSON 형식으로 저장한다.')
        
        json.dump(log_json,output_file)
        # output_file.write('{\n')
        # for k,v in log_json.items():
        #     output_file.write("{k} : {v},\n")
        #     print(f"{k} : {v},\n")

except:
    print("mission_computer_main.json 파일을 열 수 없습니다.")
    exit()

# Oxygen 찾기 위해 읽기
print('작성한 파일을 읽습니다.')
try:
    with open("D:\\study\Codyssey\\01_02\\mission_computer_main.json","rt",encoding="UTF-8") as output_read_file:
       data_read = output_read_file.read()
except:
    print("mission_computer_main.json 파일을 열 수 없습니다.")
    exit()

print('Oxygen 항목을 찾습니다.')
for line in data_read.strip().split(','):

    if line.split(': ')[1].find('Oxygen') != -1:
        print(line)