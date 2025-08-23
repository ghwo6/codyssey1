# 날아가 버린 천장의 돔의 길이를 재어보니 10m가 나왔다.
# 타원이 아닌 완전한 반구체의 형태를 한 돔의 전체 면적을 구하는 식을 세워보고
# sphere_area()라는 함수로 제작한다.
# 함수는 파라메터로 지름(diameter)을 입력받게 구현한다.
# 사용 할 수 있는 재료는 유리, 알루미늄, 탄소강이 있다고 할 때
# 각각 무게는 다음과 같을 때
# sphere_area() 함수에 재질을 material이라는 파라메터로 추가 할 수 있게 만들고
# 두께는 thickness라는 파라메터로 입력할 수 있게 만든다.

# 재질의 무게
# 유리: 2.4g /cm3
# 알루미늄: 2.7g/cm3
# 탄소강: 7.85g/cm3

import os


# 재질은 재질 리스트에서 입력 받게끔하자
material = ''
diameter = 0.0
thickness = 10.0
area = 0.0
weight = 0.0
input_temp = ''
try_bool = False

input_parameter = ['재질','지름','두께']
material_list = ['유리','알루미늄','탄소강']


# print(os.getcwd())
os.chdir(r'.\01_04')
# print(os.getcwd())

# 함수의 편의성을 위해 두께는 mm로 통일 해두었다. 나중에 이를 cm, m 로 입력가능하게 바꾸자
def sphere_area(diameter, material='glass', thickness=10):
    
    


    pass

def input_exact(order_str):
    # 자료형을 입력 받으면 <- Str 일까?
    # 거기에 따라서 재질, 지름 , 두께 가 출력되도록 하자 <- 오류 , 지름과 두께는 같은 자료형이다.
    # 문자를 입력하여 재질인지 두께인지 지름인지를 표기하자
    while try_bool==False:

        input_temp = input(f"{order_str}를 입력하시오")

        if order_str == '재질':
            if order_str in material_list:
                material = input_temp
                try_bool = True
                continue
            else: # 잘못된 재질 값으로 다시 입력 필요함
                continue
                # continue는 while try 문에서 어떤 작용을 할까?
            try_bool = True # 여기다 쓸까 위에 if 안에다 쓸까
        elif order_str =='지름':
            try:
                diameter = float(input_temp)

            except:
                
        print(f'{input_temp}는 {order_str}으로 입력할 수 없습니다.. 다시 입력해주세요')
        continue
    pass



print('')
try_bool = False
while try_bool==False:
    try:
        input_temp = input("diameter를 입력하시오")
        diameter = float(input_temp)
    except:
        print(f'{input_temp}는 지름으로 입력할 수 없습니다.. 다시 입력해주세요')
