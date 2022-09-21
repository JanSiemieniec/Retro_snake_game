import threading
from tkinter import *
import random
import time


class Game:

    def __init__(self, bg_color, snake_color):
        self.bg_color = bg_color
        self.snake_color = snake_color
        self.tab = []
        self.window = Toplevel()
        self.score = Label(self.window, text="Score: 0", font=("Arial", 25), fg=self.snake_color)
        self.side = StringVar()
        self.snake = []

    def start(self):
        self.window.title("Snake game")
        self.window.resizable(False, False)
        self.window.config()

        window_height = 600
        window_width = 600

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.score.grid(row=0, column=0, columnspan=12)
        for j in range(0, 11):
            new = []
            for i in range(0, 11):
                temp = Label(self.window, bg=self.bg_color, width=7, height=3, borderwidth=2, relief="solid")
                temp.grid(row=j + 1, column=i)
                new.append(temp)

            self.tab.append(new)
        self.window.bind("<Up>", self.change_side)
        self.window.bind("<Down>", self.change_side)
        self.window.bind("<Left>", self.change_side)
        self.window.bind("<Right>", self.change_side)
        self.window.focus_set()

    def change_side(self, event):
        if event.keysym == "Up" and self.side != "down":
            self.side = "up"
        elif event.keysym == "Down" and self.side != "up":
            self.side = "down"
        elif event.keysym == "Left" and self.side != "right":
            self.side = "left"
        elif event.keysym == "Right" and self.side != "left":
            self.side = "right"

    @staticmethod
    def vector(y):
        if y <= 5:
            return "right"
        return "left"

    def play(self):
        snake_head = Point(random.randint(0, 10), random.randint(0, 10))
        self.tab[snake_head.x][snake_head.y].configure(bg=self.snake_color)
        self.side = self.vector(snake_head.y)
        self.apple(snake_head.x, snake_head.y)
        thread = threading.Thread(target=self.playing, args=(snake_head.x, snake_head.y))
        thread.start()

    def playing(self, randx, randy):
        counter = 1
        while counter <= 10 and self.window.winfo_exists():
            self.snake.insert(0, Point(randx, randy))
            self.tab[randx][randy].configure(bg=self.bg_color)
            if self.side == "left":
                if randy - 1 < 0:
                    break
                randy -= 1
            elif self.side == "right":
                if randy + 1 > 10:
                    break
                randy += 1
            elif self.side == "down":
                if randx + 1 > 10:
                    break
                randx += 1
            else:
                if randx - 1 < 0:
                    break
                randx -= 1
            if self.tab[randx][randy].cget("bg") == "Red":
                self.apple(randx, randy)
                counter += 1
                self.snake.append(Point(randx, randy))
            elif self.tab[randx][randy].cget("bg") == self.snake_color:
                break

            self.tab[self.snake[len(self.snake) - 1].x][self.snake[len(self.snake) - 1].y].configure(bg=self.bg_color)
            self.snake.pop()
            for i in self.snake:
                self.tab[i.x][i.y].configure(bg=self.snake_color)
            self.tab[randx][randy].configure(bg=self.snake_color)
            self.score.configure(text="Score: " + str(counter - 1))
            time.sleep(0.5 - (counter * 0.03))
        if not self.window.winfo_exists():
            return
        if counter == 11:
            self.score.configure(text="You win")
        else:
            self.score.configure(text="You lose :(")
        time.sleep(2)
        for i in reversed(range(1, 4)):
            self.score.configure(text="Next game starts in " + str(i))
            time.sleep(1)
        self.playagain()

    def playagain(self):
        for j in range(0, 11):
            for i in range(0, 11):
                self.tab[i][j].config(bg=self.bg_color)
        self.snake = []
        self.play()

    def apple(self, randx, randy):
        apple_point = Point(random.randint(0, 10), random.randint(0, 10))
        if self.tab[apple_point.x][apple_point.y].cget("bg") == self.snake_color:
            self.apple(randx, randy)
            return
        self.tab[apple_point.x][apple_point.y].configure(bg="Red")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
