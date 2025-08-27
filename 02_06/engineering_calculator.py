# engineering_calculator.py

import sys
import math
from PyQt6.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QPushButton, QLineEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# -----------------------------------------------------------------------------
# 1. 이전 단계에서 작성한 계산기 핵심 로직
# -----------------------------------------------------------------------------

class Calculator:
    """기본적인 사칙연산 기능을 제공하는 계산기 클래스."""
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            return '오류'
        return x / y

class EngineeringCalculatorLogic(Calculator):
    """
    Calculator 클래스를 상속받아 공학용 계산 기능을 추가한 클래스.
    이름 충돌을 피하기 위해 EngineeringCalculatorLogic으로 변경.
    """
    def __init__(self):
        super().__init__()
        self.memory = 0

    def sin(self, x): return math.sin(math.radians(x))
    def cos(self, x): return math.cos(math.radians(x))
    def tan(self, x):
        if math.isclose(math.cos(math.radians(x)), 0): return '오류'
        return math.tan(math.radians(x))
    def sinh(self, x): return math.sinh(x)
    def cosh(self, x): return math.cosh(x)
    def tanh(self, x): return math.tanh(x)
    def pi(self): return math.pi
    def power_of_two(self, x): return x ** 2
    def power_of_three(self, x): return x ** 3
    def reciprocal(self, x):
        if x == 0: return '오류'
        return 1 / x
    def sqrt(self, x):
        if x < 0: return '오류'
        return math.sqrt(x)
    def log10(self, x):
        if x <= 0: return '오류'
        return math.log10(x)
    def factorial(self, x):
        if x < 0 or x != int(x): return '오류'
        return float(math.factorial(int(x)))

    # 메모리 기능
    def memory_store(self, value): self.memory = value
    def memory_recall(self): return self.memory
    def memory_clear(self): self.memory = 0
    def memory_add(self, value): self.memory += value
    def memory_subtract(self, value): self.memory -= value


# -----------------------------------------------------------------------------
# 2. UI와 로직을 결합한 최종 계산기 클래스
# -----------------------------------------------------------------------------

class EngineeringCalculator(QWidget):
    """
    PyQt6 UI와 계산기 로직을 통합한 공학용 계산기 클래스입니다.
    """
    def __init__(self):
        super().__init__()
        # 계산기 로직 인스턴스 생성
        self.logic = EngineeringCalculatorLogic()
        self.init_ui()

        # 계산 상태를 관리하는 변수
        self.reset_state()

    def reset_state(self):
        """계산기 상태를 초기화합니다."""
        self.first_operand = None
        self.operator = None
        self.new_input_started = True

    def init_ui(self):
        self.setWindowTitle('공학용 계산기')
        self.setGeometry(100, 100, 400, 600)

        grid = QGridLayout()
        self.setLayout(grid)

        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont('Arial', 40))
        self.display.setStyleSheet('background-color: #333; color: white; border: none;')
        grid.addWidget(self.display, 0, 0, 1, 10)

        buttons = [
            ['(', ')', 'mc', 'm+', 'm-', 'mr', 'C', '+/-', '%', '÷'],
            ['2nd', 'x²', 'x³', 'xʸ', 'eˣ', '10ˣ', '7', '8', '9', '×'],
            ['¹/ₓ', '√x', '³√x', 'ʸ√x', 'ln', 'log₁₀', '4', '5', '6', '−'],
            ['x!', 'sin', 'cos', 'tan', 'e', 'EE', '1', '2', '3', '+'],
            ['Rad', 'sinh', 'cosh', 'tanh', 'π', 'Rand', '0', '', '.', '=']
        ]

        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == '': continue
                button = QPushButton(text)
                button.setFont(QFont('Arial', 16))
                button.clicked.connect(self.on_button_clicked)

                if text in '÷×−+=': button.setStyleSheet('background-color: #f1a33c; color: white; border-radius: 10px;')
                elif text in ['C', '+/-', '%']: button.setStyleSheet('background-color: #a5a5a5; color: black; border-radius: 10px;')
                elif text.isdigit() or text == '.': button.setStyleSheet('background-color: #333333; color: white; border-radius: 10px;')
                else: button.setStyleSheet('background-color: #505050; color: white; border-radius: 10px;')
                
                button.setMinimumSize(60, 60)
                if text == '0': grid.addWidget(button, i + 1, j, 1, 2)
                else: grid.addWidget(button, i + 1, j, 1, 1)

    def on_button_clicked(self):
        """버튼 클릭 이벤트를 처리하는 메인 핸들러입니다."""
        button = self.sender()
        key = button.text()
        current_text = self.display.text()
        
        # 숫자 및 소수점 처리
        if key.isdigit() or key == '.':
            if self.new_input_started:
                self.display.setText(key)
                self.new_input_started = False
            elif key == '.' and '.' in current_text:
                return # 소수점 중복 입력 방지
            else:
                self.display.setText(current_text + key)
        
        # 연산자 처리
        elif key in ['+', '−', '×', '÷']:
            self.first_operand = float(current_text)
            self.operator = key
            self.new_input_started = True

        # '=' 계산 실행
        elif key == '=':
            if self.operator and self.first_operand is not None:
                second_operand = float(current_text)
                op_map = {'+': self.logic.add, '−': self.logic.subtract, '×': self.logic.multiply, '÷': self.logic.divide}
                result = op_map[self.operator](self.first_operand, second_operand)
                self.display.setText(str(result))
                self.reset_state()
        
        # 'C' (Clear)
        elif key == 'C':
            self.display.setText('0')
            self.reset_state()
            
        # 단일 연산자 처리
        else:
            try:
                current_value = float(current_text)
                result = None
                
                # 삼각함수 및 기본 공학 함수
                if key == 'sin': result = self.logic.sin(current_value)
                elif key == 'cos': result = self.logic.cos(current_value)
                elif key == 'tan': result = self.logic.tan(current_value)
                elif key == 'sinh': result = self.logic.sinh(current_value)
                elif key == 'cosh': result = self.logic.cosh(current_value)
                elif key == 'tanh': result = self.logic.tanh(current_value)
                elif key == 'x²': result = self.logic.power_of_two(current_value)
                elif key == 'x³': result = self.logic.power_of_three(current_value)
                elif key == '√x': result = self.logic.sqrt(current_value)
                elif key == 'log₁₀': result = self.logic.log10(current_value)
                elif key == '¹/ₓ': result = self.logic.reciprocal(current_value)
                elif key == 'x!': result = self.logic.factorial(current_value)
                elif key == '+/-': result = -current_value
                elif key == '%': result = current_value / 100
                elif key == 'π':
                    result = self.logic.pi()
                    self.new_input_started = True # pi는 새 입력으로 간주
                
                # 메모리 기능
                elif key == 'mc': self.logic.memory_clear()
                elif key == 'mr': result = self.logic.memory_recall()
                elif key == 'm+': self.logic.memory_add(current_value)
                elif key == 'm-': self.logic.memory_subtract(current_value)
                    
                if result is not None:
                    self.display.setText(str(round(result, 10))) # 소수점 10자리까지만 표시
                    if key not in ['m+', 'm-']:
                         self.new_input_started = True

            except ValueError:
                self.display.setText('오류')
                self.reset_state()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = EngineeringCalculator()
    calc.show()
    sys.exit(app.exec())