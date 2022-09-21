from tkinter import *
from tkinter import colorchooser
from Game import Game
from tkinter import messagebox


def button_enterin(event):
    event.widget["fg"] = "Green"


def button_enterout(event):
    event.widget["fg"] = "Black"


def new_game():
    game = Game(bg_color.get(), snake_color.get())
    game.start()
    game.play()


def custom():
    win = Toplevel()
    win.title("Custom")
    win.resizable(False, False)
    win.config()

    win_height = 100
    win_width = 500

    s_width = win.winfo_screenwidth()
    s_height = win.winfo_screenheight()

    x_cor = int((s_width / 2) - (win_width / 2))
    y_cord = int((s_height / 2) - (win_height / 2))

    win.geometry("{}x{}+{}+{}".format(win_width, win_height, x_cor, y_cord))
    button_snake_color = Button(win, text="Change snake color", command=lambda: change_color("snake", win),
                                font=("Fixedsys", 15))
    button_snake_color.place(x=20, y=20)
    button_bg_color = Button(win, text="Change background color", command=lambda: change_color("bg", win),
                             font=("Fixedsys", 15))
    button_bg_color.place(x=240, y=20)

    button_destroy = Button(win, text="Cancel", command=lambda: win.destroy(), font=("Fixedsys", 10))
    button_destroy.place(x=200, y=70)


def change_color(what, win):
    color = colorchooser.askcolor()
    if what == "snake":
        if color[1] == "#ff0000":
            messagebox.showwarning(title="Bad color",
                                   message="You can not chose red as color of the snake, red is an apple!")
            change_color("snake", win)
            return
        snake_color.set(color[1])
    else:
        bg_color.set(color[1])
    win.lift()


window = Tk()
window.title("Snake game")
window.resizable(False, False)
window.config()

window_height = 600
window_width = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
title = Label(window, text="Snake game", font=("Fixedsys", 35), pady=70)
title.pack()

new_game = Button(window, text="New game", borderwidth=0, font=("Fixedsys", 30), pady=20, command=new_game)
new_game.bind("<Enter>", button_enterin)
new_game.bind("<Leave>", button_enterout)
new_game.pack()

customize = Button(window, text="Customize", borderwidth=0, font=("Fixedsys", 30), pady=20, command=custom)
customize.bind("<Enter>", button_enterin)
customize.bind("<Leave>", button_enterout)
customize.pack()

snake_color = StringVar()
snake_color.set("Blue")
bg_color = StringVar()
bg_color.set("Green")

window.mainloop()
