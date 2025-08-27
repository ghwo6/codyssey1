# calculator.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QPushButton, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# -----------------------------------------------------------------------------
# 계산기 핵심 로직 클래스
# -----------------------------------------------------------------------------
class Calculator:
    """ 계산기의 모든 핵심 연산과 상태 관리를 담당하는 클래스 """
    def __init__(self):
        self.reset()

    def reset(self):
        """ 모든 상태를 초기화합니다.  """
        self.current_input = '0'
        self.first_operand = None
        self.operator = None
        self.new_input_starts = True
        return self.current_input

    def add_digit(self, digit):
        """ 입력된 숫자를 현재 값에 추가합니다. [cite: 25] """
        if self.new_input_starts or self.current_input == '0':
            self.current_input = digit
            self.new_input_starts = False
        else:
            self.current_input += digit
        return self.current_input

    def add_decimal(self):
        """ 소수점을 추가합니다. 이미 있으면 추가하지 않습니다. [cite: 26] """
        if '.' not in self.current_input:
            self.current_input += '.'
            self.new_input_starts = False
        return self.current_input

    def toggle_sign(self):
        """ 현재 숫자의 부호를 변경합니다. (음수/양수 전환)  """
        if self.current_input != '0':
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
        return self.current_input

    def percent(self):
        """ 현재 숫자를 100으로 나눈 값으로 변환합니다.  """
        try:
            value = float(self.current_input) / 100
            self.current_input = str(value)
        except ValueError:
            self.current_input = 'Error'
        return self.current_input

    def set_operator(self, op):
        """ 연산자(+, -, *, /)를 설정합니다.  """
        try:
            # 연산자를 연속으로 누를 경우, 중간 계산을 수행
            if self.operator and not self.new_input_starts:
                self.equal()
            self.first_operand = float(self.current_input)
            self.operator = op
            self.new_input_starts = True
        except ValueError:
            self.current_input = 'Error'
        return self.current_input

    def equal(self):
        """ '=' 버튼에 해당하며, 최종 계산을 수행합니다. [cite: 27] """
        if self.operator is None or self.first_operand is None or self.new_input_starts:
            return self.current_input

        try:
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
                    self.current_input = 'Error' # 0으로 나누기 예외 처리 
                    return self.current_input
                result = self.first_operand / second_operand

            # [보너스 과제] 소수점 6자리 이하로 반올림 
            if isinstance(result, float) and '.' in str(result):
                if len(str(result).split('.')[1]) > 6:
                    result = round(result, 6)

            self.current_input = str(int(result) if result == int(result) else result)

        except ValueError:
            self.current_input = 'Error'

        self.first_operand = None
        self.new_input_starts = True
        return self.current_input

# -----------------------------------------------------------------------------
# 계산기 UI 클래스
# -----------------------------------------------------------------------------
class CalculatorApp(QWidget):
    """ 계산기 UI를 생성하고 Calculator 로직 클래스와 연결합니다. """
    def __init__(self):
        super().__init__()
        self.core = Calculator() # Calculator 클래스 인스턴스 생성 
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(80)
        self.update_display(self.core.current_input)
        grid.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            ('AC', 1, 0), ('+/-', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0, 1, 2), ('.', 5, 2), ('=', 5, 3)
        ]

        for item in buttons:
            btn_text, row, col = item[:3]
            rowspan = item[3] if len(item) > 3 else 1
            colspan = item[4] if len(item) > 4 else 1

            button = QPushButton(btn_text)
            button.clicked.connect(self.button_clicked) # 모든 버튼을 하나의 핸들러에 연결 
            button.setFixedSize(80 if colspan == 1 else 170, 80)

            if btn_text in ['/', '*', '-', '+', '=']:
                button.setStyleSheet('background-color: #f9a032; color: white; font-size: 24px;')
            elif btn_text in ['AC', '+/-', '%']:
                 button.setStyleSheet('background-color: #a5a5a5; font-size: 24px;')
            else:
                button.setStyleSheet('background-color: #333333; color: white; font-size: 24px;')

            grid.addWidget(button, row, col, rowspan, colspan)

        self.setWindowTitle('Calculator')
        self.show()

    def update_display(self, text):
        """ 결과 표시창의 내용을 업데이트하고 폰트 크기를 조절합니다. """
        # [보너스 과제] 텍스트 길이에 따라 폰트 크기 동적 조절 
        length = len(text.replace(',', ''))
        if length > 15:
            font_size = 20
        elif length > 10:
            font_size = 30
        else:
            font_size = 40
        self.display.setFont(QFont('Arial', font_size))

        # 세 자리마다 콤마 추가
        try:
            if '.' in text:
                parts = text.split('.')
                integer_part = f'{int(parts[0]):,}'
                self.display.setText(f'{integer_part}.{parts[1]}')
            else:
                self.display.setText(f'{int(text):,}')
        except (ValueError, IndexError):
             self.display.setText(text)

    def button_clicked(self):
        """ 버튼 클릭 시 Calculator 클래스의 해당 메서드를 호출합니다. """
        button = self.sender()
        key = button.text()
        result = ''

        if key.isdigit():
            result = self.core.add_digit(key)
        elif key == '.':
            result = self.core.add_decimal()
        elif key == 'AC':
            result = self.core.reset()
        elif key == '+/-':
            result = self.core.toggle_sign()
        elif key == '%':
            result = self.core.percent()
        elif key in ['+', '-', '*', '/']:
            self.core.set_operator(key)
            result = self.core.current_input
        elif key == '=':
            result = self.core.equal()

        self.update_display(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    sys.exit(app.exec_())