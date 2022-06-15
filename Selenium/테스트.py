from csv import writer
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import requests
from bs4 import BeautifulSoup

# Selenium: webdriver를 통해 크롬 등 브라우저를 직접 제어한다. = 자스를 이용해 비동기적, 혹은 뒤늦게 불려오는 컨텐츠를 모두 가져올 수 있다는 것.
#request는 js로 동적으로 변화된 html을 볼 수 없고, 그 이전의 정적인 것만 볼 수 있는데 selenium은 js로 렌더링 완료된 Dom 결과물을 가져온다.

# 크롬 드라이버를 사용함. 
# 같은 위치에 있지 않으면 c:\download\chromedriver.exe 위치지정
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
#셀레늄의 웹드라이버는 브라우저에서 HTML을 파싱해주는 거라서, beaurifulsoup 사용하지 않아도 됨.
#그렇지만 셀레늄의 웹드라이버 객체의 page_source 가져오면 그게 브라우저의 html. requests통해 가져온 req의 text변수와 동일.



browser = webdriver.Chrome()   
#webdriver 객체를 만들었다. 웹브라우저를 제어하는 객체다. 크롬 드라이버.

browser.get("https://m.sports.naver.com/beijing2022/medal/index")

time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
#웹브라우저 객체의 page_source = requests객체의 text 변수와 동일. (html 소스). 그걸 beautifulsoup 사용해서 lxml방식으로 파싱.

#with부분 주석처리하고 실행해도, 이거 키고 닫아버림.

with open('test.html',"w",encoding="utf-8") as f:    #test.html이라는 이름의 파일명으로, w쓰기 모드로 파일을 열어라 = f 객체. 
    f.write(soup.prettify())  #f에 적어라. soup을 prettify한 거를.
    # with가 파일 열어서 실행하고 파일 닫는 거..


# print(browser.page_source)