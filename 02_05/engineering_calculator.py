import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QGridLayout, 
                             QPushButton, QLineEdit)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class EngineeringCalculator(QWidget):
    """
    PyQt6를 사용하여 아이폰 공학용 계산기 UI를 구현한 클래스입니다.
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        UI의 기본 설정을 초기화합니다.
        """
        self.setWindowTitle('공학용 계산기')
        self.setGeometry(100, 100, 400, 600)

        # 전체 레이아웃은 수직 박스 레이아웃으로 설정
        grid = QGridLayout()
        self.setLayout(grid)

        # 결과가 표시될 디스플레이창(QLineEdit) 생성
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont('Arial', 40))
        self.display.setStyleSheet('background-color: #333; color: white; border: none;')
        grid.addWidget(self.display, 0, 0, 1, 10)

        # 계산기 버튼 레이블 정의
        buttons = [
            ['(', ')', 'mc', 'm+', 'm-', 'mr', 'C', '+/-', '%', '÷'],
            ['2nd', 'x²', 'x³', 'xʸ', 'eˣ', '10ˣ', '7', '8', '9', '×'],
            ['¹/ₓ', '√x', '³√x', 'ʸ√x', 'ln', 'log₁₀', '4', '5', '6', '−'],
            ['x!', 'sin', 'cos', 'tan', 'e', 'EE', '1', '2', '3', '+'],
            ['Rad', 'sinh', 'cosh', 'tanh', 'π', 'Rand', '0', '', '.', '=']
        ]

        # 버튼 생성 및 그리드 레이아웃에 추가
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text == '':
                    continue
                
                button = QPushButton(text)
                button.setFont(QFont('Arial', 16))
                button.clicked.connect(self.on_button_clicked)

                # 버튼 스타일링
                if text in '÷×−+=':
                    button.setStyleSheet('background-color: #f1a33c; color: white; border-radius: 10px;')
                elif text in ['C', '+/-', '%']:
                    button.setStyleSheet('background-color: #a5a5a5; color: black; border-radius: 10px;')
                elif text.isdigit() or text == '.':
                     button.setStyleSheet('background-color: #333333; color: white; border-radius: 10px;')
                else:
                    button.setStyleSheet('background-color: #505050; color: white; border-radius: 10px;')

                button.setMinimumSize(60, 60)

                # '0' 버튼은 두 칸을 차지하도록 설정
                if text == '0':
                    grid.addWidget(button, i + 1, j, 1, 2)
                else:
                    grid.addWidget(button, i + 1, j, 1, 1)

    def on_button_clicked(self):
        """
        버튼이 클릭되었을 때 호출되는 이벤트 핸들러입니다.
        """
        button = self.sender()
        key = button.text()
        current_text = self.display.text()

        if key == 'C':
            self.display.setText('0')
        elif current_text == '0' and key not in ['C', '.', '+/-']:
            self.display.setText(key)
        else:
            self.display.setText(current_text + key)


if __name__ == '__main__':
    # Python 3.x 버전 환경에서 실행
    app = QApplication(sys.argv)
    calc = EngineeringCalculator()
    calc.show()
    sys.exit(app.exec())