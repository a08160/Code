# 윈도우 프로그래밍
# import tkinter as tk
from tkinter import *

root = Tk() # 창 생성
root.title("윈도우 프로그래밍 연습") # 페이지 이름
root.geometry("640x480") # 창 사이즈

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

# Button
def on_click():
    print("Button Click")

button = Button(root, text="클릭", command = on_click).pack()

# Entry
# 입력을 위해서는 레이아웃은 메서드 체인을 사용할 수 없음
entry = Entry(root, width = 30)
entry.pack()

# Text 여러줄 입력
text = Text(root, width = 40, height = 10)
text.pack()

# 글씨 입력
def show_text():
    entried = entry.get()
    label.config(text=f"입력된 문자는 : {entried}") # config를 통해서 입력 가능
    entry.delete(0, END) # 엔트리에 있는 문자열 삭제
    # text
    print(text.get("1.0", END))

button = Button(root, text="버튼 클릭", command = show_text).pack()

label = Label(root, text = "")
label.pack()

# Frame
top_frame = Frame(root, bg = 'lightblue')
top_frame.pack(fill="x")
Label(top_frame, text="top frame").pack(pady=30)

bottom_frame = Frame(root,bg = 'lightgreen')
bottom_frame.pack(fill="both", expand=True)
Label(bottom_frame, text = "bottom frame").pack()

# CheckButton
def show_state():
    print(f"선택은 {var.get()}")

var = IntVar()
check = Checkbutton(root, text="동의", variable = var, command = show_state).pack()

var = StringVar(value = "옵션1") # value 설정 시 해당 value의 button만 클릭되어 있음
radio1 = Radiobutton(root, text="옵션1",variable=var,value="option1", command=show_state).pack(pady=10)
radio2 = Radiobutton(root, text="옵션2",variable=var,value="option2", command=show_state).pack(pady=10)
radio3 = Radiobutton(root, text="옵션3",variable=var,value="option3", command=show_state).pack(pady=10)

# ListBox
listbox = Listbox(root)

def show_selected():
    selection = listbox.curselection
    print(selection)
    if selection:
        print(f"선택된 과일은 : {list.get(selection[0])}")

listbox.pack(pady=10)
for item in ["apple","banana","melon","grapes","cherry"]:
    listbox.insert(END, item)

button = Button(root, text ="선택", command = show_selected)
button.pack(pady = 10)

# Messagebox 모듈
from tkinter import messagebox

def show_message():
    messagebox.showinfo("경고", "메세지창 띄우기 연습") # 제목 / 내용

button = Button(root, text="클릭", command=show_message)
button.pack(pady= 10)

# 메뉴
from tkinter import messagebox

def new_file():
    messagebox.showinfo("메뉴","파일이 선택되었습니다")

def exit_app():
    root.quit()

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff = 0) # tearoff 메뉴 분리 여부
file_menu.add_command(label="New", command=new_file) # 명령어 수행
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = exit_app)

menu_bar.add_cascade(label="파일",menu = file_menu) # 서브 메뉴 생성
root.config(menu=menu_bar) # 옵션 삽입

root.mainloop()