'''
수행과제
값들을 연속적으로 출력하기 위해서 MissionComputer 클래스에 있는 get_mission_computer_info(), get_mission_computer_load() 두 개의 메소드를 time 라이브러리를 사용해서 각각 20초에 한번씩 결과를 출력 할 수 있게 수정한다.
MissionComputer 클래스를 runComputer 라는 이름으로 인스턴스화 한다.
runComputer 인스턴스의 get_mission_computer_info(), get_mission_computer_load(), get_sensor_data() 메소드를 각각 멀티 쓰레드로 실행 시킨다.
다시 코드를 수정해서 MissionComputer 클래스를 runComputer1, runComputer2, runComputer3 이렇게 3개의 인스턴스를 만든다.
3개의 인스턴스를 멀티 프로세스로 실행시켜서 각각 get_mission_computer_info(), get_mission_computer_load(), get_sensor_data()를 실행시키고 출력을 확인한다.
최종적으로 결과를 mars_mission_computer.py 에 저장한다.

제약사항
python에서 기본 제공되는 명령어 이외의 별도의 라이브러리나 패키지를 사용해서는 안된다.
단 쓰레드와 멀티 프로세스를 다루는 부분은 외부 라이브러리 사용 가능하다.
경고 메시지 없이 모든 코드는 실행 되어야 한다.

보너스 과제
멀티 쓰레드와 멀티 프로세스에서 반복적으로 출력되는 중간에 특정한 키를 입력 받아 출력을 멈출 수 있게 코드를 작성한다.


'''


import platform
import psutil
import json
import random
import os
import time
import multiprocessing

folderPath = r'01_09'

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
        
        self.tinfo = 0
        self.tload = 0
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

        while True:

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
            time.sleep(20)



    def get_mission_computer_load(self):
        """
        미션 컴퓨터의 실시간 부하 정보를 가져와 JSON 형식으로 출력합니다.
        - CPU 및 메모리의 실시간 사용량 
        - 시스템 정보는 예외 처리를 포함합니다. 
        """
        while True:

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
            time.sleep(20)




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
    

# runComputer = MissionComputer()

if __name__ == "__main__":
    print("미션 컴퓨터 모니터링을 시작합니다. 중지하려면 Enter 키를 누르세요.")

    # 프로세스 종료 이벤트를 생성합니다.
    stop_event = multiprocessing.Event()

    # 3개의 인스턴스를 생성합니다.
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    # 각 인스턴스의 메소드를 타겟으로 하는 프로세스를 생성합니다.
    p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info, args=(stop_event,))
    p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load, args=(stop_event,))
    p3 = multiprocessing.Process(target=runComputer3.get_sensor_data, args=(stop_event,))

    # p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info)
    # p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load)
    # p3 = multiprocessing.Process(target=runComputer3.get_sensor_data)
    # 프로세스를 시작합니다.
    p1.start()
    p2.start()
    p3.start()

    # 사용자가 Enter를 누를 때까지 메인 프로세스는 대기합니다.
    input()
    
    # Enter 입력 후 모든 자식 프로세스에 종료 신호를 보냅니다.
    print("모니터링을 중지합니다...")
    stop_event.set()

    # 모든 자식 프로세스가 종료될 때까지 기다립니다.
    p1.join()
    p2.join()
    p3.join()
    
    print("모든 모니터링 프로세스가 종료되었습니다.")