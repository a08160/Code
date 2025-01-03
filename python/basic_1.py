# VS code Python 실행 단축키: Ctrl+F5

# 한 줄 주석(ctrl+/)

# 여러 줄 주석의 경우 토글로 가리기 가능
'''
여러 줄 주석
'''
"""
여러 줄 주석
"""

# print("Hello world")
print("Hello world")

# , 사용 시, 공백 적용
print("Hello", "World") 

print("Hello", "World", sep="")
print("010","1234","5678", sep="-")
print("Hello","Python", 1, 2, sep=" ")
print() # 줄바꿈 처리
print("안녕하세요")

# 한 줄 출력 방법
print("안녕하세요", end="")
print("코딩온입니다.")

# 변수 할당
ive = 'I AM'
print(ive)

ive = '장원영'
print(ive)

# f 문자열 포맷팅
print(f'제가 좋아하는 가수는 {ive}입니다.')
print('제가 좋아하는 가수는 ',ive,"입니다.",sep="")

print(type(77)) # 정수 타입
print(type(77.2)) # 실수 타입

# 이스케이프 문자 \: 원래 문자의 역할을 벗어나게 함
print("\'안녕하세요")
print("\"안녕하세요")

a=77
print(type(a))
a=7.2
print(type(a))

print('111\n1111') # \n 줄바꿈
print('111\t1111') # \t tab(8칸)


# 실습2 개를 만드시오
print('''|\\_/|
|q p|\t/}
( ʘ )"""\\
|"^"`\t |
||_/=\\\\__|''')

num = 10
b_num = 0b1010
h_num = 0xA
print(num)
print(b_num)
print(h_num)

print(bin(10)) # 10 to 2
print(type(bin(65))) # 문자열
print(hex(10)) # 10 to 16
print(type(hex(65))) # 문자열

# 아스키 코드 / 유니코드 변환
# 문자들을 2진수로 풀이하기 위해 약속한 코드값
# 유니코드는 아스키코드의 확장판

print(ord('0')) # 유니코드를 원래 문자로 변환
print(ord('A'))
print(chr(48)) # 원래 문자를 유니코드로 변환
print(chr(65)) 