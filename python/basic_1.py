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