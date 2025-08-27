# calculator.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QPushButton, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class CalculatorApp(QWidget):
    """
    아이폰 스타일의 계산기 애플리케이션 클래스
    """
    def __init__(self):
        super().__init__()
        self.initUI()
        self.reset()

    def initUI(self):
        """
        UI를 초기화하고 구성요소를 설정합니다.
        """
        grid = QGridLayout()
        self.setLayout(grid)

        # 결과 표시창 설정
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont('Arial', 40))
        self.display.setFixedHeight(80)
        grid.addWidget(self.display, 0, 0, 1, 4)

        # 버튼 레이아웃 정의
        # (텍스트, 행, 열, 행 병합, 열 병합)
        buttons = [
            ('AC', 1, 0, 1, 1), ('+/-', 1, 1, 1, 1), ('%', 1, 2, 1, 1), ('/', 1, 3, 1, 1),
            ('7', 2, 0, 1, 1), ('8', 2, 1, 1, 1), ('9', 2, 2, 1, 1), ('*', 2, 3, 1, 1),
            ('4', 3, 0, 1, 1), ('5', 3, 1, 1, 1), ('6', 3, 2, 1, 1), ('-', 3, 3, 1, 1),
            ('1', 4, 0, 1, 1), ('2', 4, 1, 1, 1), ('3', 4, 2, 1, 1), ('+', 4, 3, 1, 1),
            ('0', 5, 0, 1, 2), ('.', 5, 2, 1, 1), ('=', 5, 3, 1, 1)
        ]

        # 버튼 생성 및 그리드에 추가
        for btn_text, row, col, rowspan, colspan in buttons:
            button = QPushButton(btn_text)
            button.clicked.connect(self.button_clicked)
            button.setFont(QFont('Arial', 20))
            button.setFixedSize(80, 80)
            if btn_text == '0':
                button.setFixedSize(170, 80)
            
            # 버튼 스타일 설정 (색상)
            if btn_text in ['/', '*', '-', '+', '=']:
                button.setStyleSheet('background-color: #f9a032; color: white;')
            elif btn_text in ['AC', '+/-', '%']:
                 button.setStyleSheet('background-color: #a5a5a5;')
            else:
                button.setStyleSheet('background-color: #333333; color: white;')

            grid.addWidget(button, row, col, rowspan, colspan)

        self.setWindowTitle('Calculator')
        self.show()

    def reset(self):
        """
        계산기 상태를 초기화합니다.
        """
        self.current_input = '0'
        self.first_operand = None
        self.operator = None
        self.new_input_starts = True
        self.update_display()

    def update_display(self):
        """
        결과 표시창의 내용을 업데이트합니다.
        """
        # 숫자에 세 자리마다 콤마 추가 (소수점은 제외)
        try:
            if '.' in self.current_input:
                parts = self.current_input.split('.')
                integer_part = f'{int(parts[0]):,}'
                self.display.setText(f'{integer_part}.{parts[1]}')
            else:
                self.display.setText(f'{int(self.current_input):,}')
        except ValueError:
             self.display.setText(self.current_input)


    def button_clicked(self):
        """
        버튼 클릭 이벤트를 처리합니다.
        """
        button = self.sender()
        key = button.text()

        if key.isdigit():
            if self.new_input_starts or self.current_input == '0':
                self.current_input = key
                self.new_input_starts = False
            else:
                self.current_input += key
        
        elif key == '.' and '.' not in self.current_input:
            self.current_input += '.'
            self.new_input_starts = False

        elif key == 'AC':
            self.reset()

        elif key == '+/-':
            if self.current_input != '0':
                if self.current_input.startswith('-'):
                    self.current_input = self.current_input[1:]
                else:
                    self.current_input = '-' + self.current_input
        
        elif key == '%':
            try:
                value = float(self.current_input) / 100
                self.current_input = str(value)
            except ValueError:
                self.current_input = 'Error'
        
        elif key in ['+', '-', '*', '/']:
            if self.first_operand is None:
                self.first_operand = float(self.current_input)
            else: # 연산자 버튼을 연속으로 누를 경우 중간 계산 수행
                self.calculate()
                self.first_operand = float(self.current_input)
            
            self.operator = key
            self.new_input_starts = True

        elif key == '=':
            self.calculate()
            self.first_operand = None
            self.operator = None

        self.update_display()

    def calculate(self):
        """
        사칙연산을 수행합니다.
        """
        if self.operator and self.first_operand is not None:
            second_operand = float(self.current_input)
            result = 0
            
            if self.operator == '+':
                result = self.first_operand + second_operand
            elif self.operator == '-':
                result = self.first_operand - second_operand
            elif self.operator == '*':
                result = self.first_operand * second_operand
            elif self.operator == '/':
                if second_operand == 0:
                    self.current_input = 'Error'
                    return
                result = self.first_operand / second_operand

            # 정수 결과는 정수로 표시
            if result == int(result):
                self.current_input = str(int(result))
            else:
                self.current_input = str(result)
            
            self.new_input_starts = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    sys.exit(app.exec_())