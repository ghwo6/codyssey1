import tkinter as tk
from tkinter import messagebox
import random

class MinesweeperGUI:
    def __init__(self, master, rows=16, cols=16, mines=40):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines

        # UI 개선을 위한 색상 및 폰트 설정
        self.colors = {
            'bg': '#c0c0c0',
            'clicked_bg': '#a0a0a0',
            'unclicked_bg': '#c0c0c0',
            1: '#0000ff', 2: '#008200', 3: '#ff0000', 4: '#000084',
            5: '#840000', 6: '#008284', 7: '#840084', 8: '#000000'
        }
        self.cell_font = ("Arial", 12, "bold")

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        """GUI 위젯(프레임, 버튼, 레이블)을 생성하고 배치합니다."""
        self.master.title("지뢰찾기")
        self.master.configure(bg=self.colors['bg'])
        # 창 크기 조절 방지
        self.master.resizable(False, False)

        # 상단 정보 프레임
        top_frame = tk.Frame(self.master, bg=self.colors['bg'], relief=tk.RIDGE, bd=2)
        top_frame.pack(pady=10, padx=10, fill=tk.X)

        self.flag_label = tk.Label(top_frame, text=f"{self.mines:03}", font=("Arial", 16, "bold"), bg=self.colors['bg'], fg='red')
        self.flag_label.pack(side=tk.LEFT, padx=10)

        self.restart_button = tk.Button(top_frame, text="🙂", font=("Arial", 16), command=self.new_game, relief=tk.RAISED, width=3)
        self.restart_button.pack(side=tk.LEFT, expand=True)

        # 게임 보드 프레임
        board_frame = tk.Frame(self.master, bg=self.colors['bg'], relief=tk.SUNKEN, bd=2)
        board_frame.pack(pady=(0, 10), padx=10)

        self.buttons = []
        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                btn = tk.Button(board_frame, width=2, height=1, relief=tk.RAISED, bg=self.colors['unclicked_bg'],
                                font=self.cell_font)
                btn.grid(row=r, column=c)
                btn.bind('<Button-1>', lambda e, r=r, c=c: self.on_left_click(r, c))
                btn.bind('<Button-3>', lambda e, r=r, c=c: self.on_right_click(r, c))
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def new_game(self):
        """새 게임을 시작하고 모든 변수와 UI를 초기화합니다."""
        self.game_over = False
        self.first_click = True
        self.flags = 0
        self.cells_opened = 0
        self.mine_locations = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        # UI 초기화 (가장 중요한 부분)
        for r in range(self.rows):
            for c in range(self.cols):
                btn = self.buttons[r][c]
                btn.config(text="", state=tk.NORMAL, relief=tk.RAISED, bg=self.colors['unclicked_bg'])
        
        self.update_flag_label()
        self.restart_button.config(text="🙂")


    def place_mines(self, first_r, first_c):
        """첫 클릭 이후에 지뢰를 배치합니다. (첫 클릭이 지뢰가 되지 않도록)"""
        mines_placed = 0
        while mines_placed < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            # 첫 클릭 위치와 그 주변에는 지뢰를 배치하지 않음
            if self.mine_locations[r][c] != '*' and (abs(r - first_r) > 1 or abs(c - first_c) > 1):
                self.mine_locations[r][c] = '*'
                mines_placed += 1
        
        # 주변 지뢰 수 계산
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_locations[r][c] != '*':
                    count = self.count_adjacent_mines(r, c)
                    self.mine_locations[r][c] = count

    def count_adjacent_mines(self, r, c):
        """(r, c) 주변 8칸의 지뢰 수를 계산합니다."""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= r + i < self.rows and 0 <= c + j < self.cols and self.mine_locations[r + i][c + j] == '*':
                    count += 1
        return count

    def on_left_click(self, r, c):
        """마우스 왼쪽 클릭 처리"""
        if self.game_over or self.buttons[r][c]['state'] == tk.DISABLED or self.buttons[r][c]['text'] == '🚩':
            return
        
        if self.first_click:
            self.place_mines(r, c)
            self.first_click = False

        btn = self.buttons[r][c]
        value = self.mine_locations[r][c]

        if value == '*':
            self.game_over = True
            btn.config(text='💣', bg='red')
            self.reveal_all_mines()
            self.restart_button.config(text="😵")
            messagebox.showerror("게임 오버", "지뢰를 밟았습니다!")
            return

        self.reveal_cell(r, c)
        self.check_win()

    def on_right_click(self, r, c):
        """마우스 오른쪽 클릭 처리 (깃발)"""
        if self.game_over or self.buttons[r][c]['state'] == tk.DISABLED:
            return
        
        btn = self.buttons[r][c]
        if btn['text'] == '':
            if self.flags < self.mines:
                btn.config(text='🚩', state='normal', fg='red')
                self.flags += 1
        elif btn['text'] == '🚩':
            btn.config(text='')
            self.flags -= 1
        
        self.update_flag_label()

    def reveal_cell(self, r, c):
        """재귀적으로 칸을 열고 UI를 업데이트합니다."""
        if not (0 <= r < self.rows and 0 <= c < self.cols) or self.buttons[r][c]['state'] == tk.DISABLED:
            return

        btn = self.buttons[r][c]
        value = self.mine_locations[r][c]
        
        btn.config(state=tk.DISABLED, relief=tk.FLAT, bg=self.colors['clicked_bg'])
        self.cells_opened += 1

        if isinstance(value, int) and value > 0:
            btn.config(text=str(value), fg=self.colors.get(value, 'black'))
        elif value == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.reveal_cell(r + i, c + j)

    def reveal_all_mines(self):
        """게임 종료 시 모든 지뢰의 위치를 보여줍니다."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_locations[r][c] == '*' and self.buttons[r][c]['text'] != '🚩':
                    self.buttons[r][c].config(text='💣', bg='#ff9999')

    def check_win(self):
        """승리 조건을 확인합니다."""
        if not self.game_over and self.cells_opened == (self.rows * self.cols) - self.mines:
            self.game_over = True
            self.restart_button.config(text="😎")
            self.reveal_all_mines_on_win()
            messagebox.showinfo("승리!", "축하합니다! 모든 지뢰를 찾았습니다!")

    def reveal_all_mines_on_win(self):
        """승리했을 때 깃발로 표시되지 않은 지뢰를 자동으로 표시합니다."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_locations[r][c] == '*':
                    self.buttons[r][c].config(text='🚩', fg='red')

    def update_flag_label(self):
        """깃발 개수 레이블을 업데이트합니다."""
        remaining_mines = self.mines - self.flags
        self.flag_label.config(text=f"{remaining_mines:03}")


if __name__ == "__main__":
    root = tk.Tk()
    game = MinesweeperGUI(root)
    root.mainloop()