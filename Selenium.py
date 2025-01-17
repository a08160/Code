from selenium import webdriver

driver = webdriver.Chrome() # Edge 브라우저 실행
driver.get("https://www.musinsa.com/main/musinsa/recommend") # URl로 이동

input("대기") # 강제종료 막는 코드

print(driver.title)
driver.quit() # 브라우저 닫기

# 무한 스크롤
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys 모듈 추가
import time
from selenium.webdriver.chrome.options import Options
from cryptography.hazmat.primitives.asymmetric import ec

service = Service()
driver = webdriver.Chrome(service = service)
driver.get("https://naver.com")

search_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div/div/form/fieldset/div/input") # XPATH 가 가장 찾기 쉬움
search_input.click()
search_input.send_keys("Selenium")
search_input.send_keys(Keys.ENTER)
driver.implicitly_wait(5)

image_click = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[4]/a")
image_click.click()
time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# scrollTo: 절대 위치 / scrollBy: 상대 위치(헌재 위치에서 스크롤)

time.sleep(5)

driver.quit()

# 속성 값 가져오기
# 스크린샷

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys 모듈 추가
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service()
driver = webdriver.Chrome(service = service)
driver.get("https://naver.com")

# 검색입력 필드대기
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[3]/div/div/form/fieldset/div/input")) # 튜플로 묶어야 함
)

email_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[6]/ul/li[3]/a")
href = email_text.get_attribute("href")
print(href)

driver.save_screenshot("img.png")