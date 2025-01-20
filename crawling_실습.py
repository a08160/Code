# 실습1. github 정보 가져오기 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys 모듈 추가
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from IPython.display import Image, display

def git_profile(id,password):
    
    # ChromeOptions 객체
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service()
    driver = webdriver.Chrome(options = chrome_options)
    driver.get("https://github.com/login")

    # 로그인
    id_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/input[3]')
    password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]')

    id_input.send_keys(id)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    passkey_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/div[2]/form/webauthn-get/button")
    passkey_input.click()
    
    time.sleep(5) # 2중 보안 해제

    profile_input1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div[4]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span")
    profile_input1.click()

    profile_input2 = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/ul/li[3]/a")
    profile_input2.click()

    # 프로필 이미지
    profile_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#upload-avatar-link > img'))
        )
    img_url = profile_img.get_attribute("src")
    display(Image(url=img_url))
    
    # ID
    id_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[1]/div[2]/h1/span[2]'))
    )
    print(f"ID: {id_input.text}")
    
    # 닉네임
    nickname_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[1]/div[2]/h1/span[1]'))
    )
    print(f"닉네임: {nickname_input.text}")

    # 자주 사용하는 레포지토리
    repo_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.repo'))
    )
    print(f"자주 사용하는 레포지토리: {repo_input.text}")

    driver.quit()
    
git_profile("a08160@g.skku.edu","ledong*1")

# 실습2. 다나와
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def product_search(product, price):
    # ChromeOptions 객체 생성 및 설정
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # ChromeDriver 서비스 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 다나와 웹사이트 접속
    driver.get("https://danawa.com")

    # 검색창에 검색어 입력
    try:
        search_input = driver.find_element(By.XPATH, '//input[@id="AKCSearch"]')
        search_input.send_keys(product)
        search_input.send_keys(Keys.ENTER)

        # 검색 결과 로드 대기 (최대 10초)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.prod_main_info'))
        )
    except Exception as e:
        print(f"Error during search: {e}")
        driver.quit()
        return

    # 결과 저장 변수
    result_links = []

    # 검색 결과 가져오기
    product_info = driver.find_elements(By.CSS_SELECTOR, '.prod_main_info')

    for product in product_info:
        try:
            # 가격 요소 추출 및 변환
            price_element = product.find_element(By.XPATH, './/span[contains(@class, "price")]')
            price_text = price_element.text.replace(',', '').replace('원', '').strip()  # 쉼표 및 단위 제거
            real_price = int(price_text)

            if real_price >= price * 10000:  # 입력 가격 조건 (만원 단위)
                # 조건을 만족하는 경우 링크 추출
                link_element = product.find_element(By.XPATH, './/a[contains(@class, "click_log_product_standard_title")]')
                link = link_element.get_attribute('href')
                result_links.append(link)
        except Exception as e:
            print(f"Error processing product: {e}")

    # 결과 출력
    print("Filtered Links:", result_links)

    # 브라우저 종료
    driver.quit()

# 함수 실행
product_search("노트북", 50)  # 예: 50만 원 이상 노트북 검색


# 실습3. Airbnb
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys 모듈 추가
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from datetime import datetime

def hotel(place,start_date, end_date, guest): # 날짜 입력은 YYYY-MM-DD 의 형태
    
    # ChromeOptions 객체 생성 및 설정
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # ChromeDriver 서비스 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Airbnb 웹사이트 접속
    driver.get("https://airbnb.com")

    time.sleep(2)
    
    # 지역
    place_input1 = driver.find_element(By.XPATH, '//*[@id="search-tabpanel"]/div/div[1]/div[1]/label/div')
    place_input1.click()
    place_input2 = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[1]/div[1]/label/div/input')
    place_input2.send_keys(place)
    place_input2.send_keys(Keys.ENTER)

    # 날짜 계산
    start_date_split = start_date.split("-")
    year_diff = int(start_date_split[0]) - datetime.now().year
    month_diff = int(start_date_split[1]) - datetime.now().month
    time_diff = year_diff * 12 + month_diff  # 연도 차이를 월 단위로 변환 후 합산
    
    # '다음 달' 버튼 클릭 반복
    next_button_locator = (By.XPATH, '//button[@aria-label="다음 달로 전환하려면 앞으로 이동하세요."]')
    for _ in range(time_diff):
        next_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(next_button_locator))
        next_button.click()
        time.sleep(1)

    # 시작 날짜 클릭
    start = driver.find_element(By.XPATH, f'//button[@data-state--date-string="{start_date}"]')
    start.click()

    time.sleep(1)
    
    # 종료 날짜 입력
    end_date_split = end_date.split("-")
    year_diff = int(end_date_split[0]) - int(start_date_split[0])
    month_diff = int(end_date_split[1]) - int(start_date_split[1])
    time_diff = year_diff * 12 + month_diff  # 연도 차이를 월 단위로 변환 후 합산
    
    # '다음 달' 버튼 클릭 반복
    next_button_locator = (By.XPATH, '//button[@aria-label="다음 달로 전환하려면 앞으로 이동하세요."]')
    for _ in range(time_diff):
        next_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(next_button_locator))
        next_button.click()
        time.sleep(1)
        
    end = driver.find_element(By.XPATH, f'//button[@data-state--date-string="{end_date}"]')
    end.click()

    time.sleep(1)

    # 게스트 입력
    guest_input1 = driver.find_element(By.XPATH, '//*[@id="search-tabpanel"]/div/div[5]/div[2]/div[1]/div/div[1]')
    guest_input1.click()

    guest_input2 = driver.find_element(By.XPATH, '//*[@id="stepper-adults"]/button[2]')
    for i in range(guest):
        guest_input2.click()
        time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="search-tabpanel"]/div/div[5]/div[2]/div[3]/button').click()
    time.sleep(5)

    # 호텔명
    name = driver.find_element(By.XPATH, '//*[@id="title_929577433075951818"]')
    print(f"호텔명: {name.text}")
    
    # 가격
    price = driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div[2]/div/div/span[3]/div/button/div/div/span')
    print(f"가격: {price.text}")
    
hotel("서울","2025-03-24", "2025-03-26", 5)

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import base64
import os
import requests

def image_save(keyword, num): # 저장하고 싶은 키워드와 이미지 개수 지정

    # 저장할 경로 지정 (사자 폴더에 저장)
    save_dir = f"C:/Users/SAMSUNG/image_practice/{keyword}/"
    os.makedirs(save_dir, exist_ok=True)

    # ChromeOptions 객체
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://google.com")
    
    # 이미지 태그 클릭
    search_input1 = driver.find_element(By.CSS_SELECTOR, '[aria-label="이미지 검색 "]')
    search_input1.click()
    
    # 이미지 페이지 검색
    search_input2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea")
    search_input2.click()
    search_input2.send_keys(keyword)
    search_input2.send_keys(Keys.ENTER)
    time.sleep(3)
    
    # 무한 스크롤링과 이미지 가져오기
    img_elements = []
    while len(img_elements) < num:
        # 새로 로드된 이미지 요소 찾기
        new_elements = driver.find_elements(By.CLASS_NAME, 'mNsIhb')
        for element in new_elements:
            img = element.find_element(By.TAG_NAME, "img")
            src = img.get_attribute('src')
            if src not in img_elements:  # 중복을 방지하기 위해 src만 추가
                img_elements.append(src)
                
        # 스크롤 내리기
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)  # 페이지 로딩을 기다림

    # 크롤링 종료 후 드라이버 종료
    driver.quit()
    
    img_elements = img_elements[:num]  # 이미지 개수 제한
    i = 1
    for src in img_elements:
        if src.startswith("data:image"):  # base64 형식일 경우 처리
            img_data_decoded = base64.b64decode(src.split("base64,")[1])
            with open(save_dir + f"{keyword}_{i}.png", "wb") as f:
                f.write(img_data_decoded)
        else:
            try:
                response = requests.get(src)
                with open(save_dir + f"{keyword}_{i}.png", "wb") as f:
                    f.write(response.content)
            except Exception as e:
                print(f"Failed to download image {i}: {e}")
        i += 1

image_save("라면", 100)