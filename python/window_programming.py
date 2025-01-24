# 윈도우 프로그래밍
# import tkinter as tk
from tkinter import *

root = Tk()
root.title("윈도우 프로그래밍 연습")
root.geometry("640x480")

# 레이아웃 pack 방식
label1 = Label(root, text = "Top", bg = "red", fg = "white") # bg: 배경색 fg: 글자색
label1.pack(side="top", fill = "x", padx = 10, pady=10)

label2 = Label(root, text = "bottom", bg = "blue", fg = "white")
label2.pack(side="bottom", fill="x", padx = 10, pady = 10)

label3 = Label(root, text = "left", bg = "green", fg = "white")
label3.pack(side="left", fill="y", padx = 10, pady = 10)

label4 = Label(root, text = "right", bg = "yellow", fg = "black")
label4.pack(side="right", fill="y", padx = 10, pady = 10)

label5 = Label(root, text = "center", bg = "purple", fg = "indigo")
label5.pack(fill="both",expand= True, padx = 10, pady = 10)

# 레이아웃 Grid() 방식: 상대적인 위치


# 위젯---------
# Label
label = Label(root, text = "Hello, tkinter!", font=('Arial',20), fg = "blue")
label.pack()

root.mainloop()

# Button
def on_click():
    print("Button Click")

button = Button(root, text="클릭", command = on_click).pack()

# 글씨 입력
def show_text():
    entried = Entry.get()