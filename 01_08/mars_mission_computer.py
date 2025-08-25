'''
수행과제
파이썬 코드를 사용해서 다음과 같은 미션 컴퓨터의 정보를 알아보는 메소드를 get_mission_computer_info() 라는 이름으로 만들고 문제 7에서 완성한 MissionComputer 클래스에 추가한다.

- 필요한 미션 컴퓨터의 시스템 정보
운영체계
운영체계 버전
CPU의 타입
CPU의 코어 수
메모리의 크기
get_mission_computer_info()에 가져온 시스템 정보를 JSON 형식으로 출력하는 코드를 포함한다.
미션 컴퓨터의 부하를 가져오는 코드를 get_mission_computer_load() 메소드로 만들고 MissionComputer 클래스에 추가한다
get_mission_computer_load() 메소드의 경우 다음과 같은 정보들을 가져 올 수 있게한다.
CPU 실시간 사용량
메모리 실시간 사용량
get_mission_computer_load()에 해당 결과를 JSON 형식으로 출력하는 코드를 추가한다.
get_mission_computer_info(), get_mission_computer_load()를 호출해서 출력이 잘되는지 확인한다.
MissionComputer 클래스를 runComputer 라는 이름으로 인스턴스화 한다.
runComputer 인스턴스의 get_mission_computer_info(), get_mission_computer_load() 메소드를 호출해서 시스템 정보에 대한 값을 출력 할 수 있도록 한다.
최종적으로 결과를 mars_mission_computer.py 에 저장한다.

	
제약사항
python에서 기본 제공되는 명령어 이외의 별도의 라이브러리나 패키지를 사용해서는 안된다.
단 시스템 정보를 가져오는 부분은 별도의 라이브러리를 사용 할 수 있다.
시스템 정보를 가져오는 부분은 예외처리가 되어 있어야 한다.
모든 라이브러리는 안정된 마지막 버전을 사용해야 한다.
'''

import platform
import psutil
import json
import random
import os

folderPath = r'01_08'

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

    def get_internal_temperature(self):
        return self.env_values['mars_base_internal_temperature']

    def get_external_temperature(self):
        return self.env_values['mars_base_external_temperature']

    def get_internal_humidity(self):
        return self.env_values['mars_base_internal_humidity']

    def get_external_illuminance(self):
        return self.env_values['mars_base_external_illuminance']

    def get_internal_co2(self):
        return self.env_values['mars_base_internal_co2']

    def get_internal_oxygen(self):
        return self.env_values['mars_base_internal_oxygen']


class MissionComputer:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": 0.0,
            "mars_base_external_temperature": 0.0,
            "mars_base_internal_humidity": 0.0,
            "mars_base_external_illuminance": 0.0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0.0,
        }
        self.ds = DummySensor()
        self.ds.set_env()
    def get_mission_computer_info(self):
        try:

            # psutil을 사용하여 메모리 크기를 바이트 단위로 가져옵니다.
            total_memory_gb = round(psutil.virtual_memory().total / (1024**3), 2)

            info = {
                'os': platform.system(),
                'os_version': platform.version(),
                'cpu_type': platform.processor(),
                'cpu_cores': os.cpu_count(),
                'memory_size_gb': total_memory_gb
            }
            # indent=4 옵션으로 JSON을 보기 좋게 출력합니다.
            print(json.dumps(info, indent=4, ensure_ascii=False))
        except Exception as e:
            error_message = {'error': f'시스템 정보 조회 중 오류 발생: {e}'}
            print(json.dumps(error_message, indent=4, ensure_ascii=False))


    def get_mission_computer_load(self):
        """
        미션 컴퓨터의 실시간 부하 정보를 가져와 JSON 형식으로 출력합니다.
        - CPU 및 메모리의 실시간 사용량 
        - 시스템 정보는 예외 처리를 포함합니다. 
        """
        try:
            load_info = {
                # interval=1로 1초간의 CPU 사용량을 측정합니다.
                'cpu_usage_percent': psutil.cpu_percent(interval=1),
                'memory_usage_percent': psutil.virtual_memory().percent
            }
            print(json.dumps(load_info, indent=4))
        except Exception as e:
            error_message = {'error': f'시스템 부하 조회 중 오류 발생: {e}'}
            print(json.dumps(error_message, indent=4, ensure_ascii=False))



    def get_sensor_data(self):
        import time
        import json

        

        while True:
            self.env_values["mars_base_internal_temperature"] = self.ds.get_internal_temperature()
            self.env_values["mars_base_external_temperature"] = self.ds.get_external_temperature()
            self.env_values["mars_base_internal_humidity"] = self.ds.get_internal_humidity()
            self.env_values["mars_base_external_illuminance"] = self.ds.get_external_illuminance()
            self.env_values["mars_base_internal_co2"] = self.ds.get_internal_co2()
            self.env_values["mars_base_internal_oxygen"] = self.ds.get_internal_oxygen()
            
            print(json.dumps(self.env_values, indent=4))
            time.sleep(5)
            self.ds.set_env()
    

runComputer = MissionComputer()

print("--- Mission Computer System Info ---")
runComputer.get_mission_computer_info()

print("\n--- Mission Computer System Load ---")
runComputer.get_mission_computer_load()