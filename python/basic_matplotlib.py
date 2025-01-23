# Matplotlib 데이터 시각화

import matplotlib.pyplot as plt
# from matplotlib import font_manager

# path = "Pretendard-Medium.otf"
# font = font_manager.FontProperties(fname = path).get_name()
# plt.rc('font', family = font)

# Matplotlib 데이터 시각화

x = list(range(1,6))
y = list(range(5,10))

plt.plot(x,y, color = "red", linestyle="--", linewidth = 1, label = "Graph")
plt.legend(loc="upper center", fontsize = 15, title = "Contents", frameon= False)

# 마커 생성
plt.plot(x,y, marker = "o", markersize =30, markerfacecolor="white", markeredgecolor = "red")
plt.title("Matplotlib", fontsize = 20, pad=20, backgroundcolor = "red", color="blue")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True, axis = "both", color="gray", linestyle="--", linewidth=0.5)

plt.show()


x = [1,2,3,4]
y1= [1,2,3,4]
y2= list(i*2 for i in range(1,5))
y3= list(i*3 for i in range(1,5))
y4= list(i*4 for i in range(1,5))

plt.plot(x,y1, label = "y=x", color="red")
plt.plot(x,y2, label = "y=2x", color="red")
plt.plot(x,y3, label = "y=3x", color="red")
plt.plot(x,y4, label = "y=4x", color="red")

plt.legend(title = "4graph", loc = "upper center", ncol = 4)
plt.title("graph sample")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

fig, axes = plt.subplots(2,2)

# 하나씩 여러개 그리기 방법1
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("x=y")

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("x=2y")

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title("x=3y")

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title("x=4y")

plt.suptitle("sample graph")
plt.tight_layout()
plt.show()

# 하나씩 여러개 그리기 방법2
x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]
y3 = [3, 6, 9, 12]
y4 = [4, 8, 12, 16]
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, y1)
axes[0, 0].set_title("x=y")

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("x=2y")

axes[1, 0].plot(x, y3)
axes[1, 0].set_title("x=3y")

axes[1, 1].plot(x, y4)
axes[1, 1].set_title("x=4y")

plt.suptitle("sample graph")
plt.tight_layout()
plt.show()

# 막대그래프
categories = ["A","B","C"]
values = [10,15,7]

plt.bar(categories, values, width=0.5, color=["red","blue","g"])
plt.show()

# 막대그래프
categories = ["A", "B", "C"]
values = [10, 15, 7]

plt.bar(
    categories,
    values,
    width=0.5,
    color=["r", "g", "b"],
    alpha=0.5,
    edgecolor="black",
    linewidth=5,
    # align="edge",
)

bars = plt.bar(categories, values, color="orange", label="Bar Graph")
plt.xticks(categories, ["2023", "2024", "2025"])

# 바그래프별 텍스트 넣기
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x좌표(막대의 중심)
        bar.get_height() - 0.5,  # y좌표
        str(bar.get_height()),
        ha="center",
        va="top",
        color="black"
    )

plt.title("Bar graph")
plt.show()

# 수평 막대그래프 그리기

categories = ["A","B","C"]
values = [10,15,7]

bars = plt.barh(categories,values,color = ["r","g","b"])

for bar in bars:
    plt.text(
        bar.get_width() + 0.7, # x 좌표
        bar.get_y() + bar.get_height() / 2, # y 좌표
        str(bar.get_width()),
        ha = "right",
        va = "center",
        color = "black"
    )

# plt.xticks(categories,["2023","2024","2025"]) 눈금 표기기

plt.legend(bars, ["2023","2024","2025"], title = "Year", ncol = 3)
plt.axvline(x=values[0], linestyle="--")

plt.title("Horizontal Bar Graph", pad = 10)
plt.xlabel("category")
plt.ylabel("year")
plt.show()

# plt.savefig("bar.png", format="png") 파일 저장하기

# 히스토그램 그리기

import matplotlib.pyplot as plt

data = [1,2,2,3,4,6,7,2,4,12,3,4,5,6,7]

plt.hist(data, color = "g", histtype = "barstacked", bins = 12   ,range=(0,10))

plt.show()


from numpy import random

data1 = random.randint(1,11,10)
data2 = random.randint(1,11,10)
plt.hist([data1,data2], bins = 10, color = ["green", "purple"], label=["data1","data2"])
plt.legend()
plt.show()

from numpy import random

x = random.randint(1,11,5)
y = random.randint(1,11,5)
sizes = [20,50,80,100,200]
colors = [10,20,30,40,50]

plt.scatter(x,y ,s=sizes, c=colors, cmap= "viridis")
plt.colorbar(label="color bar")

plt.show()



# 산점도 추가 예제

import numpy as np

n = 50
x = np.random.rand(n)
y = np.random.rand(n)

area = (30 * np.random.rand(n)) ** 2
colors = np.random.rand(n)

plt.scatter(x,y, s=area, c=colors, cmap= "Spectral",alpha=0.5) # alpha : 투명도 조절 변수



# 파이차트 그리기
# sizes = [25, 25, 20, 20]
# labels =["A","B","C","D"]

sizes = [15,30,34,10]
labels = ["Apple","Banana","Grapes","Cherry"]
explode = [0,0.1,0,0]  # 데이터 강조

plt.pie(sizes, labels=labels, explode = explode, autopct = "%1.1f%%", shadow = True, startangle= 140)

plt.show()


# 도넛 차트: wedgeporps의 width를 조절

# 실습1. 꺾은선 그래프
import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
sales_2019 = [100,120,140,110,130,150,160,170,180,200,190,210]
sales_2020 = [90,110,130,120,140,160,170,160,150,180,200,190]

plt.plot(months, sales_2019, label = "2019")
plt.plot(months, sales_2020, label = "2020")

plt.legend()

plt.title("Monthly Sales Comparison (2019-2020)")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()




# 실습2. 막대 그래프
import matplotlib.pyplot as plt

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
data = [20, 35, 15, 27, 45]

plt.bar(
    categories,
    data,
    width = 0.75,
    linewidth = 1,
    align = "center",
    alpha = 0.9
)

plt.ylim((0,50))

plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.xticks(rotation=45)

plt.grid(True,color="lightgrey",linewidth = "0.6")

plt.tight_layout()
plt.show()


# 실습3. 파이 차트
import matplotlib.pyplot as plt

sizes = [32,16,18,34]
fruits = ["Banana","Melon","Grapes","Apple"]
emphasize =[0.1,0,0.1,0]
colors = ["yellow","g","purple","r"]

# 딕셔너리로 조절하는 게 좋을 듯?

plt.pie(
    sizes,
    labels = fruits,
    explode = emphasize,
    autopct= "%1.1f%%",
    startangle = 120,
    colors= colors,
    wedgeprops= {'linewidth':1, 'edgecolor' : "black", "width":0.75})

# counterclock 데이터의 반영 방향을 반대로(기본. 반시계 방향)

plt.tight_layout()
plt.show()

