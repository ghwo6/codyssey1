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
import math
GRAVITY_MARS = 3.73
GRAVITY_EARTH = 9.81
GRAVITY_RATIO = GRAVITY_MARS / GRAVITY_EARTH

# 재질은 재질 리스트에서 입력 받게끔하자

# 재질
material = '유리'
# 지름(cm)
diameter = 0.0
# 두께(cm)
thickness = 1.0
# 면적
area = 0.0
# 무게
weight = 0.0
# 입력받는값 저장소
input_temp = ''

#
input_bool = False
material_dict = {'유리':2.4,'알루미늄':2.7,'탄소강':7.85}

# 선택지를 입력받는값
select_number = 0

# print(os.getcwd())
os.chdir(r'.\01_04')
# print(os.getcwd())

def input_material() :
    while True:
        input_temp = input('재질을 입력해주세요. (유리,알루미늄,탄소강)')
        if input_temp in material_dict.keys():
            return input_temp
        else:
            print('잘못된 값을 입력하셨습니다.')

def input_diameter() :
    while True:
        input_temp = input('지름을 입력해주세요. (cm)')
        if input_temp.isdecimal():
            if input_temp.strip() != '0' and input_temp.strip() != '0.0' :
                return float(input_temp)
            else:
                print('0을 입력하시면 안됩니다.')
        else:
            print('숫자가 아닌 값을 입력하셨습니다.')

def input_thickness():
    while True:
        input_temp = input('두께를 입력해주세요. (cm)')
        if input_temp.isdecimal():
            if input_temp.strip() != '0' and input_temp.strip() != '0.0':
                return float(input_temp)
            else:
                print('0을 입력하시면 안됩니다.')
        else:
            print('숫자가 아닌 값을 입력하셨습니다.')
def sphere_area(d:float,m:str = '유리',t:float = 1.0) :
# d 는 지름, m 은 재질, t 는 두께
    # global material
    # global diameter
    # global thickness

    # 면적
    # math.pi*(d**2)
    # 겉넓이
    # math.pi*(d**2)
    # 무게[kg]
    # math.pi*(d**2)*t*material_dict[m]/1000

    # material_dict[m]

    # 계산
    area = math.pi*(float(d)*float(d))
    weight = math.pi*(float(d)*float(d))*t*material_dict[m]/1000 * GRAVITY_RATIO

    # 반올림
    area = round(area,3)
    weight = round(weight,3)

    # 출력
    print(f'재질 ⇒ {str(m)}, 지름 ⇒ {str(d)}cm, 두께 =⇒ {t}cm, 면적 ⇒{str(area)}cm^2 , 무게 ⇒ {str(weight)} kg')


continue_bool = True

while continue_bool == True:

    print(f'1. 재질 \t {material}')
    print(f'2. 지름 \t {str(diameter)}')
    print(f'3. 두께 \t {str(thickness)}')

    select_number = input('바꾸려는 값을 입력해주세요.')

    if select_number == '1':
        material = input_material()
    elif select_number == '2':
        diameter = input_diameter()
    elif select_number == '3':
        thickness = input_thickness()
    
    sphere_area(diameter,material,thickness)