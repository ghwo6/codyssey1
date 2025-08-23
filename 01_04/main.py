# 날아가 버린 천장의 돔의 길이를 재어보니 10m가 나왔다.
# 타원이 아닌 완전한 반구체의 형태를 한 돔의 전체 면적을 구하는 식을 세워보고
# sphere_area()라는 함수로 제작한다.
# 함수는 파라메터로 지름(diameter)을 입력받게 구현한다.
# 사용 할 수 있는 재료는 유리, 알루미늄, 탄소강이 있다고 할 때
# 각각 무게는 다음과 같을 때
# sphere_area() 함수에 재질을 material이라는 파라메터로 추가 할 수 있게 만들고
# 두께는 thickness라는 파라메터로 입력할 수 있게 만든다.


	
# 제약사항
# Python에서 기본 제공되는 명령어만 사용해야 하며 별도의 라이브러리나 패키지를 사용해서는 안된다.
# 입력되는 지름의 값이 0이 되면 안된다.
# 한번 계산으로 종료되지 않고 계속해서 조건을 바꾸어가며 반복해서 계산할 수 있게 해야한다.
# 출력값이 소수점 이하로 너무 길 때에는 소수점 3자리까지만 출력 할 수 있어야 한다.
# 더 이상 계산이 필요없을 때에는 쉽게 종료 할 수 있어야 한다.



# 재질의 무게
# 유리: 2.4g /cm3
# 알루미늄: 2.7g/cm3
# 탄소강: 7.85g/cm3

import os


# 재질은 재질 리스트에서 입력 받게끔하자
material = ''
diameter = 0.0
thickness = 1.0
area = 0.0
weight = 0.0
input_temp = ''
test_bool = False
select_number = 0

input_parameter = ['재질','지름','두께']
material_list = ['유리','알루미늄','탄소강']


# print(os.getcwd())
os.chdir(r'.\01_04')
# print(os.getcwd())

# 함수의 편의성을 위해 두께는 cm로 통일 해두었다. 나중에 이를 cm, m 로 입력가능하게 바꾸자
def sphere_area(diameter, material='glass', thickness=1.0):
    
    

    print(f'재질 => {material}, 지름 => {diameter}, 두께 => {thickness}, 면적 => {area}, 무게 => {weight} kg')
    pass

test_bool = False
while test_bool == False:
    input_temp = input('재질을 입력하시오')
    if input_temp in material_list:
        material = input_temp
        test_bool = True
    else :
        print('다시 입력해주세요. 유리. 탄소강. 알루미늄.')

test_bool = False
while test_bool==False:
    input_temp = input("diameter를 입력하시오. 단위 : (cm)")
    try:
        diameter = float(input_temp)
        test_bool = True
    except:
        print(f'{input_temp}는 지름으로 입력할 수 없습니다.. 다시 입력해주세요.')

test_bool = False
while test_bool == False:
    input_temp = input("두께를 입력하시오. 단위 : (cm)")
    try:
        thickness = float(input_temp)
        test_bool = True
    except:
        print(f'{input_temp}는 두께로 입력할 수 없습니다.. 다시 입력해주세요.')
while True :
    sphere_area(diameter,material,thickness)
    print('1. 재질')
    print('2. 지름')
    print('3. 두께')
    
    input_temp = input('무엇을 바꾸겟습니까?')
    if input_temp.isdigit() == True:
        select_number = int(input_temp)
    else:
        print('잘못 입력하셨습니다. 다시 입력하십시오.')
        continue
    
