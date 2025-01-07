# 반복문
# for / while

'''
# while 문: 조건식이 False 가 되면 반복문을 종료
# 들여쓰기(Indent / Depth)


초기값
while 조건문:
  실행문
  종료조건
'''

# VS Code 아래의 Spaces 조정을 통해 Indent 크기 조절 가능

i = 0
while i < 3:
  print("반복문 연습", i)
  i += 1
print("반복문 종료")

# 합계 구하기
num = 1
total = 0
while num <= 10:
  total += num
  num+=1
print(f"1부터 10까지의 합은 {total}입니다")

# 입력값 받기
user_input = ""
while user_input != "종료":
  user_input = input("원하는 값을 입력하세요. 종료 입력 시 종료됩니다.")
  print(f"입력한 값: {user_input}")
print("프로그램이 종료되었습니다.")

# 무한 루프(loop)
# break / continue
While True: