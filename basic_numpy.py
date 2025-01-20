# 배열 합치기
a = np.array([1,2,3,4,5])
b = np.array([3,4,5,6,7])

print(np.hstack((a,b)))
print(np.vstack((a,b)))
print(np.column_stack((a,b)))

# 분할
c = np.array([a,b])

# 수평 분할: 수평이 기준
print(np.hsplit(c,5))
print(np.vsplit(c,2))


# 실습. 야구기록 데이터 정렬 실습. 야구기록 데이터 정렬
# BeautifulSoup 활용

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import numpy
import requests

# ChromeOptions 객체 생성 및 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

# ChromeDriver 서비스 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.koreabaseball.com/")

driver.find_element(By.XPATH, '//*[@id="lnb"]/li[2]/a').click()

driver.find_element(By.XPATH, '//*[@id="lnbTeamRank"]').click()

res = requests.get(driver.current_url)
soup = BeautifulSoup(res.text, "html.parser")

contents = soup.find_all("thead")[0].text.strip()
records = soup.find_all("tbody")[0].text.strip()

driver.quit()

contents,records = np.array([contents.split("\n")]), records.split("\n")

records = list(filter(lambda x: x != "", records))

record_list = np.array([records[i:i+12] for i in range(0, len(records), 12)])

total_record = np.vstack((contents, record_list))

with open("2024kbo.txt", "w") as f:
    f.write("======================================= 2024 한국 프로야구 성적표 =======================================\n")
    for row in total_record:
        f.write("\t".join(row) + "\n")

with open("2024kbo.txt", "r") as f:
    data = f.read()
    print(data)


# 실습. 야구기록 데이터 정렬 실습. 야구기록 데이터 정렬
# Selenium만 활용

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy

# ChromeOptions 객체 생성 및 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

# ChromeDriver 서비스 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.koreabaseball.com/")

driver.find_element(By.XPATH, '//*[@id="lnb"]/li[2]/a').click()

driver.find_element(By.XPATH, '//*[@id="lnbTeamRank"]').click()

contents = np.array([[i.text for i in driver.find_elements(By.CSS_SELECTOR, "thead > tr > th")][:12]])
records = [i.text for i in driver.find_elements(By.CSS_SELECTOR, "tbody > tr")][:10]

driver.quit()

new_record = []
for record in records:
    new_record.append(record.split(" "))
                    
new_record = np.array(new_record)

total_record = np.vstack((contents, new_record))

with open("2024kbo.txt", "w") as f:
    f.write("======================================= 2024 한국 프로야구 성적표 =======================================\n")
    for row in total_record:
        f.write("\t".join(row) + "\n")

with open("2024kbo.txt", "r") as f:
    data = f.read()
    print(data)

