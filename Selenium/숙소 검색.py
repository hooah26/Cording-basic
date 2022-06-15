import time
from selenium import webdriver    #selenium에서 웹드라이버 가져온다. 이따 chrome연결해서 chrome드라이버 객체 만듦.
from selenium.webdriver.common.keys import Keys  # keys입력에 관한 메소드
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait # 출력화면이 나타날때까지 대기하는 메소드
from selenium.webdriver.common.by import By
import pyautogui

from selenium.webdriver.support import expected_conditions as EC # 브라우저 화면의 상태를 알려주는 메소드
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


browser = webdriver.Chrome(options=options)
browser.maximize_window() # 윈도우 창 최대화
url ='https://www.yanolja.com/'
browser.get(url)  #url 이동

browser.find_element_by_xpath('//*[@id="__next"]/section/header/div/div[3]/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[2]/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[3]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[3]/div/div/section/section[4]/button').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[1]/input').send_keys('제주도')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div[1]/header/nav/div[2]/form/div[1]/input').send_keys(Keys.ENTER)
time.sleep(5)

prev_height = browser.execute_script("return document.body.scrollHeight") 
print(prev_height)
#execute_script은 자바스크립트 명령문이다.
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    pyautogui.scroll(-prev_height)
    time.sleep(8)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height


page_source= browser.page_source
soup=BeautifulSoup(page_source,'lxml')
hotels=soup.find_all('div',{'class':'PlaceListItemText_container__fUIgA text-unit'})

count=0
for hotel in hotels:
    name= hotel.find('strong',{'class':'PlaceListTitle_text__2511B small'}).get_text()
    price=hotel.find('span',{'class':'PlacePriceInfo_salePrice__28VZD'}).get_text()
    rate=hotel.find('span',{'class':'PlaceListScore_rating__3Glxf'}).get_text()
    count+=1
    print(name, price, rate)
    
print('전체 개수: ', count)

