from selenium import webdriver
import time  # 시간 지연
import random  # 지연시간을 랜덤으로 처리
from selenium.webdriver.common.keys import Keys #키보드 관련 메소드
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# 크롬 드라이버 객체 생성
browser = webdriver.Chrome(options=options)
# 페이지 이동
browser.get("http://www.naver.com")
# class link_login 선택후 클릭
browser.find_element_by_class_name("link_login").click()
time.sleep(random.uniform(1,3)) # 1-3초동안 대기

# 자바스크립트로 id,pw를 input에 입력해주는 명령어
input_js = 'document.getElementById("id").value="{id}"; document.getElementById("pw").value="{pw}";'.format(id="aaa",pw="1111")
#페이지의 html코드 중 id가 id인 곳을 찾아서, 'aaa'를 넣고. id가 pw인 곳을 찾아서, '1111'을 넣어라.


# 자바스크립트 구문 실행
browser.execute_script(input_js) #현재 페이지에서 자바스크립트로 명령문 내리는 것.
time.sleep(2) # 2초동안 대기

browser.find_element_by_id("log.login").click()