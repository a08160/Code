# 예외 처리

try:
    x = int(input("숫자를 입력하세요"))
    result = 10 / x

except (ZeroDivisionError, ValueError) as e:
    print("에외메세지 : ", e)

else: # 예외 미발생 시 작동
    print(f"result는 {result}")

finally: # 예외와 관계 없이 무조건 실행
    print("프로그램을 종료합니다")

def divide(a,b):
	if b==0:
		raise ZeroDivisionError("0으로 나눌 수 없습니다.")
	return a/b
	
print(divide(1,0))