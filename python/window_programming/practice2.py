from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# ChromeDriver 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 동행복권 당첨번호 페이지 접속
driver.get("https://www.dhlottery.co.kr/gameResult.do?method=byWin")
time.sleep(2)

# 현재 회차 찾기
current_no = int(driver.find_element(By.XPATH,
                                  '//*[@id="dwrNoList"]/option[1]').text)

# 회차 입력 받기
try:
    draw_no = int(input("당첨 회차를 입력하세요: "))
    
    if draw_no >= 1 and draw_no <= current_no:

        # 회차 선택 dropdown menu 찾기
        dropdown = driver.find_element(By.ID, "dwrNoList")
        dropdown.click()  # dropdown 메뉴를 클릭
        time.sleep(1)
        
        # 해당 회차 번호를 선택
        option = driver.find_element(By.XPATH, f"//option[text()='{draw_no}']")
        option.click()
        time.sleep(2)

        # 당첨 번호 및 보너스 번호 출력
        numbers = driver.find_elements(By.CLASS_NAME, "ball_645")
        winning_numbers = [num.text for num in numbers[:-1]]  # 보너스 번호 제외
        bonus_number = numbers[-1].text

        print(f"당첨 번호: {', '.join(winning_numbers)}")
        print(f"보너스 번호: {bonus_number}")
        
    else:
        print("해당 회차는 진행하지 않았습니다.")
except Exception as e:
    print("오류 발생:", e)
finally:
    driver.quit()


# # 창 생성 페이지

# root = Tk() # 창 생성
# root.title("로또 당첨 확인") # 페이지 이름
# root.geometry("640x480") # 창 사이즈
