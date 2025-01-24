# 연습 실습. 쿠폰 추첨기기

from tkinter import *
from numpy import random
from tkinter import *

def on_click():
    name_list = ["김민경", "이동건", "최승우", "최영", "한수빈","김혜은", "조경록","이채연"]

    name = random.sample(name_list, 2)
    print(name)
    text.delete("1.0", END)
    text.insert(END,name)

window = Tk()
window.title("쿠폰추첨기")
window.geometry("1296x840")

# 이미지 넣기
label_img = Label(window)
img = PhotoImage(file="window_programming\coupon.jpg")
label_img.config(image=img)
label_img.pack()

Button(window, text="추첨", command = on_click).pack()

# 추첨된 사람 출력
text =Text(window, width=40, height=5,bg = "green")
text.pack()


window.mainloop()