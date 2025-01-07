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
# break
while True:
  num = int(input('숫자 입력(0 입력 시 종료): '))

  if num == 0:
    print("프로그램 종료")
    break

  print(f"입력한 숫자는 {num}입니다")

# continue
while True:
  num = int(input('숫자 입력(음수 입력 시 종료): '))

  if num < 0:
    print('프로그램 종료')
    break

  if num % 2 != 0:
    continue
  
  print(f"입력한 짝수는 {num}입니다")


# 실습. while문 사용하기

while True:
    answer = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료): ")
    if answer == "종료":
        print("프로그램을 종료합니다.")
        break
    else:
        try:
            answer = int(answer)
            if answer > 0:
                i = 1
                total = 0
                while i <= answer:
                    total += i
                    i+=1
                print(f"1부터 {answer}까지의 합은 {total}입니다.")
            else:
                print("양수만 입력하세요")
        except ValueError:
            print("양수만 입력하세요")
        
# IsDigit을 활용한 While문 실습

while True:
    answer = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료): ")
    if answer == "종료":
        print("프로그램을 종료합니다.")
        break
    elif answer.isdigit() == True:
        answer = int(answer)
        if answer > 0:
            i = 1
            total = 0
            while i <= answer:
                total += i
                i+=1
            print(f"1부터 {answer}까지의 합은 {total}입니다.")
        else:
            print("양수만 입력하세요.")
    else:
        print("양수만 입력하세요.")