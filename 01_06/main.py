'''
수행과제
더미 센서에 해당하는 클래스를 생성한다. 클래스의 이름은 DummySensor로 정의한다.
DummySensor의 멤버로 env_values라는 사전 객체를 추가한다. 사전 객체에는 다음과 같은 항목들이 추가 되어 있어야 한다.
화성 기지 내부 온도 (mars_base_internal_temperature)
화성 기지 외부 온도 (mars_base_external_temperature)
화성 기지 내부 습도 (mars_base_internal_humidity)
회성 기지 외부 광량 (mars_base_external_illuminance)
화성 기지 내부 이산화탄소 농도 (mars_base_internal_co2)
화성 기지 내부 산소 농도 (mars_base_internal_oxygen)
DummySensor는 테스트를 위한 객체이므로 데이터를 램덤으로 생성한다.
DummySensor 클래스에 set_env() 메소드를 추가한다. set_env() 메소드는 random으로 주어진 범위 안의 값을 생성해서 env_values 항목에 채워주는 역할을 한다. 각 항목의 값의 범위는 다음과 같다.
화성 기지 내부 온도 (18~30도)
화성 기지 외부 온도 (0~21도)
화성 기지 내부 습도 (50~60%)
화성 기지 외부 광량 (500~715 W/m2)
화성 기지 내부 이산화탄소 농도 (0.02~0.1%)
화성 기지 내부 산소 농도 (4%~7%)
DummySensor 클래스는 get_env() 메소드를 추가하는데 get_env() 메소드는 env_values를 return 한다.
DummySensor 클래스를 ds라는 이름으로 인스턴스(Instance)로 만든다.
인스턴스화 한 DummySensor 클래스에서 set_env()와 get_env()를 차례로 호출해서 값을 확인한다.
전체 코드를 mars_mission_computer.py 파일로 저장한다.

제약사항
Python에서 기본 제공되는 명령어만 사용해야 하며 별도의 라이브러리나 패키지를 사용해서는 안된다.
단 random을 다루는 라이브러리는 사용 가능하다.
Python의 coding style guide를 확인하고 가이드를 준수해서 코딩한다.
경고 메시지 없이 모든 코드는 실행 되어야 한다.

보너스 과제
출력하는 내용을 날짜와시간, 화성 기지 내부 온도, 화성 기지 외부 온도, 화성 기지 내부 습도 ,화성 기지 외부 광량, 화성 기지 내부 이산화탄소 농도, 화성 기지 내부 산소 농도 와 같이 파일에 log를 남기는 부분을 get_env()에 추가 한다.
'''


import random
import os

folderPath = r'01_06'

class DummySensor:

    env_values = {'mars_base_internal_temperature': None,
                            'mars_base_external_temperature': None,
                            'mars_base_internal_humidity': None,
                            'mars_base_external_illuminance': None,
                            'mars_base_internal_co2': None,
                            'mars_base_internal_oxygen': None}
    def __init__(self):
        
        self.env_values = {'mars_base_internal_temperature': 0,
                            'mars_base_external_temperature': 0,
                            'mars_base_internal_humidity': 0,
                            'mars_base_external_illuminance': 0,
                            'mars_base_internal_co2': 0,
                            'mars_base_internal_oxygen': 0}
    def set_env(self):

        self.env_values['mars_base_internal_temperature'] = round(random.random()*22+18,2)
        self.env_values['mars_base_external_temperature'] = round(random.random()*21,2)
        self.env_values['mars_base_internal_humidity'] = round(random.random()*10+50,2)
        self.env_values['mars_base_external_illuminance'] = random.random()*215+500
        self.env_values['mars_base_internal_co2'] = round(random.random()*0.08+0.02,2)
        self.env_values['mars_base_internal_oxygen'] = round(random.random()*3+4,2)

    def get_env(self):
        file = open(os.path.join(folderPath+'/'+'get_env.txt'),'wt',encoding='utf-8')
        file.write(str(self.env_values))
        file.close()
        return self.env_values
    

ds = DummySensor()
ds.set_env()
print(ds.get_env())
