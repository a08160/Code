# 모듈(module)

import practice_module

print(practice_module.add(5,7))

p1 = practice_module.Calculator()

print(p1.multiply(1,2))

# Quiz
# 1.divide(x,y) 함수 추가(y=0 인 케이스 고려)
# 자연로그 e 2.718 변수 추가
# Calculator 클래스에 제곱을 구하는 square(x) 메서드

print(p1.square(2))

# 모듈 불러오기
# 1. import 모듈 2. from 모듈 import 시퀀스
# import 모듈 as a 라고 했을 때, as = alias

from datetime import datetime, timedelta, date
import time

now = datetime.today() # 현재시간

print(now)
print(now.year)
print(now.minute)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# timedelta는 날짜 연산
next_year = now + timedelta(weeks=1, hours=1)
before_year = now - timedelta(weeks=1, hours=1)
print(next_year)


# 개강일 출력
open_date = date(year=2024, month=12, day=30)
print(open_date)

# 개강일로부터 지난 시간
print((date.today()-open_date).days)
print(date.today().weekday()) # weekday() 요일을 숫자로 변환(0~6)

print(time.time()) # timestamp. 1970년 1월 1일 00:00:00 을 기준으로 현재까지의 시간(초단위)
print(time.localtime()) # 로컬 시간대 출력

print("2초 대기")
time.sleep(2) # 지정된 초단위 시간 동안 프로그램 실행 중지
print("대기 완료")

start_time = time.perf_counter()
time.sleep(2)
end_time = time.perf_counter()
print(end_time - start_time)


# math 모듈
import math

print(math.pi)
print(math.sqrt(25))
print(math.factorial(4))

print(math.ceil(3.14)) # 올림
print(math.floor(3.14)) # 내림
print(round(3.14)) # 반올림
print(round(3.74))

# random module
import random

rand_int = random.randint(1,10) # 1 이상 10 이하의 정수
print(rand_int)

rand_float = random.uniform(1.5,6.5) # 1.5 이상 6.5 이하의 실수
print(rand_float)

rand_between = random.random() # 0 이상 1 미만 무작위 실수
print(rand_between)

rand_range = random.randrange(10,1000) # 10 이상 100 미만 무작위 정수
print(rand_range)

nums = [i for i in range(1,8)]
rand_choice = random.choice(nums) # 리스트 내에서 무작위 선택(단일 선택택)
print(rand_choice)

fruits = ["귤", "사과", "바나나","키위","귤"]
rand_sample = random.sample(fruits, 2) # 비복원 무작위 추출 후 리스트 저장
print(rand_sample)