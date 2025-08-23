# import os

print('Hello Mars')

error_count = 0

try:
    with open('D:\\study\\Codyssey\\01_01\\mission_computer_main.log','rt',encoding='UTF-8') as file:
        try:
            with open('D:\\study\\Codyssey\\01_01\\log_analysis.md','wt',encoding='UTF-8') as output_file:
                
                # 문법에 오류있는 str.find() 함수에서는 첫번째 매개변수로 단일 str 만 입력가능하며
                # 본 코드는 List 로 작성되어서 오류가 발생한것으로 보인다.
                # for line in file:
                #     if line.find(['unstable','explosion']) != -1:
                #         print(line,end='')

                output_file.write('### mission_computer_main.log를 분석한 결과입니다.\n')
                output_file.write('\n')

                for line in file:
                    # print(line)
                    if 'unstable' in line or 'explosion' in line:
                        error_count +=1

                        if error_count == 1:
                            output_file.write('### 로그 내용중 이상한 현상이 포착되었습니다.\n')
                            output_file.write('### 이를 분석하기에 적절한 연구가 필요하다고 생각됩니다.\n')

                            print('### 로그 내용중 이상한 현상이 포착되었습니다.\n')
                            print('### 이를 분석하기에 적절한 연구가 필요하다고 생각됩니다.\n')
                            output_file.write('\n')
                            output_file.write('```\n')
                        print(line)
                        output_file.write(line)
                if error_count != 0:
                    # output_file.seek(-1)

                    output_file.write('```\n')

                if error_count != 0 :
                    output_file.write(f'## 위 {error_count}건의 로그 내용을 확인해주시기 바랍니다.\n')
                    output_file.write('## 본 사의 무궁한 발전을 바랍니다.')
                    print(f'### 위 {error_count}건의 로그 내용을 확인해주시기 바랍니다.')
                    print('### 본 사의 무궁한 발전을 바랍니다.')

        except:
            print('log_analysis.md 파일이 열리지 않습니다.')

        
    
except:
    print('로그 파일이 열리지 않습니다.')
    exit()