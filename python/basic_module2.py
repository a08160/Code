# sys
import sys
print(sys.argv) # 명령형 인수 전체 리스트를 출력
print(sys.argv[1:])
print(sys.version) # 파이썬 버젼 출력
# sys.exit(0) # 프로그램 종료 => 이후 코드는 출력 안 됨


# os(Operation System)
import os
print("현재 작업 디렉토리", os.getcwd) # 현재 작업 디렉토리 출력
file_path = os.chdir(os.getcwd()) # 해당 경로로 이동
dir = os.popen("dir") # ls 명령어 조회(shell에 따라 dir 활용)
print(dir.read()) #"ls" 명령어 출력 결과 가져오기

os.mkdir("temp") # 파일 생성
os.rmdir("temp") # 파일 제거

print(os.environ.get('PATH')) # 환경 변수 확인

# json(JavaScript Object Notation)
# Javascript object 자료형과 유사하게 생긴 텍스트 형식
# 가독성이 뛰어남. 컴퓨터도 사람도 모두 해석하기 편함
# Python 객체 <=> Json 형태 변환
# json 의 bool 형 언어는 소문자로 시작

import json

python_dict = {
    "name":"Lilly",
    "age":20,
    "city":"Busan",
    "bool": True
}


json_str= json.dumps(python_dict) # python 객체를 json 문자열로 변환
print(json_str)

json_obj = json.loads(json_str) # json 문자열을 python 객체로 변환


# 서드파트 모듈: 표준 모듈이 아닌 외부 개발자에 의해 개발된 모듈