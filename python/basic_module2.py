# sys
import sys
print(sys.argv) # 명령형 인수 전체 리스트를 출력
print(sys.argv[1:])
print(sys.version) # 파이썬 버젼 출력
sys.exit(0) # 프로그램 종료 => 이후 코드는 출력 안 됨


# os(Operation System)
import os
print("현재 작업 디렉토리", os.getcwd)


# json
import json