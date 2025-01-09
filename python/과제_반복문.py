# 과제. 자판기 프로그램
# 조건1.사용자는 소비자, 주인 두 가지 종류로 입력받기(번호 또는 값 입력), 그 외의 값은 잘못된 값으로 출력
# 조건2.소비자일 때 마시고 싶은 음료를 입력받기
    # 조건2-1.값이 있으면 vending_machine에서 제거, 없으면 "없음" 출력
# 조건3. 주인일 때, 추가/삭제 두 가지 종류 입력 받기(조건1과 같게)
    # 조건3-1.추가일 때 추가할 음료수 입력받고 vending_machine에 추가 후, 같은 값끼리 연결되게 출력
    # 조건3-2.삭제일 때 삭제할 음료수 입력받고 값이 있으면 제거, 없으면 "없음" 출력

'''
* 조건1
- 1. 소비자 / 2. 주인 의 방식을 입력 받음(roll)
- 해당 목차를 처음에 제시
- 잘못 작성할 시 목차를 다시 제공 및 "다시 입력해주세요" 문구 출력

* 소비자일 때와 주인일 때의 코드를 따로 작성하고 마지막에 병합
'''

# 기능1. 음료 구매
# 기능2. 남은 음료수 확인
# 기능3. 음료수가 있는 지 확인
# 기능4. 음료수 추가
# 기능5. 음료수 제거

## 함수 정의
# 함수 정의
def check_machine(): # 남은 음료수를 확인할 수 있는 함수
    print("남은 음료수: ", vending_machine)

def is_drink(): # 음료수가 남았는 지 확인하는 함수
    if len(vending_machine) == 0:
        print("남은 음료수가 없습니다.")
    else:
        print("남은 음료수: ", vending_machine)

def add_drink():
    a = input("추가할 음료수는?: ")
    vending_machine.append(a)
    return vending_machine.sort()

vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
set_vending_machine = set(vending_machine)

# 역할 나누기
# 주인이 할 수 있는 것 기능 2~5
# 소비자가 할 수 있는 것 1~3
import itertools

rolls = {("1","소비자"):1,("2","주인"):2}
flattened_rolls = list(itertools.chain(*rolls.keys()))
while True:
    roll = input('''1. 소비자
2. 주인
사용자를 입력하세요.: ''')
    if roll in flattened_rolls:
        if roll in list(rolls.keys())[0]: # 소비자
            while True:
                func = input('''1. 음료수 구매
2. 남은 음료수 확인
3. 자판기 사용 종료
어떤 기능을 사용하시겠습니까?(숫자만 입력해주세요): ''')
                if func in ["1","2","3"]:
                    if func == "1":
                        what_drink = input("마시고 싶은 음료는? ")
                        if what_drink in vending_machine:
                            print(f"{what_drink} 드릴게요.")
                            vending_machine.remove(what_drink)
                            check_machine()
                        else:
                            print(f"{what_drink}가 없습니다.")
                    if func == "2":
                        if len(vending_machine) == 0:
                            print(f"{what_drink}가 없습니다.")
                        else:
                            check_machine()
                    if func == "3":
                        print("자판기 프로그램을 종료합니다.")
                        break
                else:
                    print("다시 입력해주세요")
                    continue
                ans = input("자판기를 계속 사용하시겠습니까?(y/n): ")
                if ans == "y":
                    continue
                else:
                    print("자판기 프로그램을 종료합니다.")
                    break
        break
        if roll in list(rolls.keys())[1]: # 주인
            while True:
                func = input('''1. 남은 음료수 확인
2. 음료수 추가
3. 음료수 제거
4. 자판기 사용 종료
어떤 기능을 사용하시겠습니까?(숫자만 입력해주세요): ''')
                if func in ["1","2","3","4"]:
                    if func == "1":
                        if len(vending_machine) == 0:
                            print(f"{what_drink}가 없습니다.")
                        else:
                            check_machine()
                    if func == "2":
                        add_drink()
                        check_machine()
                    if func == "3":
                        try:
                            vending_machine.remove(input("제거할 음료수? "))
                            print("제거 완료")
                            check_machine()
                        except:
                            print("해당 음료수가 자판기에 없습니다.")
                            check_machine()
                    if func == "4":
                        print("자판기 프로그램을 종료합니다.")
                        break
                else:
                    print("다시 입력해주세요")
                    continue    
                ans = input("자판기를 계속 사용하시겠습니까?(y/n): ")
                if ans == "y":
                    continue
                else:
                    print("자판기 프로그램을 종료합니다.")
                    break
        break
    else:
        print("숫자나 값을 입력해주세요.")
        continue

# 멘토님 사용자 정의 함수

def check_machine():
    print("남은 음료수: ", vending_machine)
    
def is_drink(drink):
    return drink in vending_machine

def add_drink(drink):
    vending_machine.append(drink)
    print(f"{drink} 추가 완료")

def remove_drink(drink):
    if is_drink(drink):
        vending_machine.remove(drink)
        print(f"{drink} 드릴게여")
    else:
        print("음료가 없습니다")