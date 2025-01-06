# list 선언
number=[1,2,3,"Hello","Python"]

# 인덱싱(Indexing): 인덱스 번호로 원소를 추출하는 행위
print(number)
print(number[0])
''' print(number[100])''' 


# list 함수 : 리스트를 생성하는 내장함수(반복 가능한 객체를 리스트로 생성)
# 반복 가능한 객체? ex. 문자열, 튜플, 집합, 딕셔너리, 리스트
# 숫자형은 반복 불가능
text = "Hello, Python"
print(list(text))

'''
Invalid = 1234
print(list(Invalid)) # TypeError: 'int' object is not iterable(정수는 반복가능한 객체가 아님)
'''

# 슬라이싱(slicing)
shop = ["반팔", "청바지", "이어폰", "키보드"]
print(shop[0:0])

# 값 삭제
# del list[index]
del shop[1] 
del shop[0:]

# list 연산
a = [1,2,3]
b = [1,2]
print(a+b) # +: 리스트 합치기 / -: 연산 불가
print(a*2) # a의 원소를 반복

# Quiz1
date = "20250106"
year = date[:4]
month = date[4:6]
day = date[6:]
print(year + "년" + month +"월" + day + "일") # 2025년 01월 06일

# 문자열에서 사용 가능한 함수
print(len(date))
print(text.count("l")) # count 내에는 문자열만 입력가능 / 대소문자 구분함

# 리스트 슬라이싱
shop = ["반팔","청바지","이어폰",["무선키보드","기계식키보드"]] 
print(shop[:2])
print(shop[3:])
print(shop[-2])
print(shop[:])

# 리스트 수정
shop[0] = "긴팔"
print(shop)
# shop[100]="신발" # Error 발생: 존재하는 Index 범위 내에서만 수정 가능

# 리스트 삭제
del shop[1]

# 정렬 함수
num = [3,1,5,2]
num_new = sorted(num, reverse = True)
num.sort(reverse=True)

# 위치 찾기 메서드
# index(찾을 요소): 맨 처음에 나오는 요소의 위치를 반환
# 리스트에 찾을 요소가 없으면 오류가 발생생
a = ['q', 'w', 'e', 'r', 'w']
print(a.index('w'))

# 정렬 함수
num = [3,1,5,2]
num_asc = sorted(num)
num_desc = sorted(num,reverse = True)

korean = ["김","이","박","최","정"]
korean.sort(reverse=True)
print(korean)

korean.reverse()

# Quiz2
alphabet = ["b","c","a","d"]
alphabet.reverse()
print(alphabet.index("c"))

# 요소 추가/삭제/삽입
a = ["a","b", "c", "c" ,"안녕", "hi"]
a.append("Good")
print(a)

a.pop()
print(a)

a.pop(2)
print(a)

a.insert(2, "잘가")
print(a)

a.remove("안녕")
print(a)

a.pop()

x = ["q", "w", "e", "r", "w"]
print(x.count("w"))


rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# 1. 2번 인덱스 값 출력
print(rainbow.index(2))

# 2. 알파벳 순서로 정렬한 값 출력하기
print(rainbow.sort)

# 3. 좋아하는 색 맨 마지막에 추가하기
rainbow.append("green")

# 4. 3~6번째 값 삭제하기

del rainbow[3:7]