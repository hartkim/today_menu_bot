from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from datetime import datetime    


def crawler(secret):

    id_= secret['id'].replace("\'","")
    pw_= secret['pw'].replace("\'","")
    
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    driver.implicitly_wait(20)	# 암시적 대기 시간 10초 설정

    #인스타 아이디
    id = id_
    #비밀번호
    pw = pw_

    #id와 pw를 입력하는 창의 요소 정보 획득
    input = driver.find_elements(By.TAG_NAME,"input")

    #아이디를 입력
    input[0].send_keys(id)

    #비밀번호 입력
    input[1].send_keys(pw)

    #엔터
    input[1].send_keys(Keys.RETURN)

    #로그인 정보 저장 여부 ("나중에 하기 버튼 클릭")
    btn_later1 = driver.find_element(By.CLASS_NAME,'_ac8f')
    btn_later1.click()
    time.sleep(3)

    #알림 설정 ("나중에 하기 버튼 클릭")
    btn_later2 = driver.find_element(By.CLASS_NAME,'_a9--._a9_1')
    btn_later2.click()

    searchurl="https://www.instagram.com/jins_onlbabsang/"

    driver.get(searchurl)
    time.sleep(10)

    ## 4. 최근사진 부터 크롤링

    posting = driver.find_elements(By.CLASS_NAME,'_aagw')
    time.sleep(3)
        
    posting[0].click()
    time.sleep(2)

    html = driver.page_source# html 긁어오기
    soup = BeautifulSoup(html,'html.parser')
    # 원하는 내용만 추출
    contents = soup.select("._aacl._aaco._aacu._aacx._aad7._aade")
    day = soup.select("_a9ze _a9zf")
    time.sleep(2)

    # 내용 뽑아서 menu에 저장
    contents = contents[0].text
    menu = contents.split()[3:-2]
    menu = (',').join(menu)
    menu = menu.replace(',', '\n').split('\n')


     # 오늘날짜 기록
    #now = datetime.today().strftime("%Y-%m-%d")
    # 원래 이 코드로 날짜 수집했는데, 그러면 크롤링 한 날짜가 수집이 되어서
    # 메뉴를 크롤링 하는 날이 달라질때마다 같은 메뉴인데 날짜가 달라짐
    # 그래서 아래와 같이 수정



    crawler_date = "2023년" + contents.split()[2].lstrip('#')
    datetime_string = crawler_date
    datetime_format = "%Y년%m월%d일"
    datetime_result = datetime.strptime(datetime_string, datetime_format)

    if datetime_result.day < 10:
        now = str(datetime_result.year)+"-"+'0'+str(datetime_result.month)  +"-" + '0'+str(datetime_result.day)
    else:
        now = str(datetime_result.year)+"-"+'0'+str(datetime_result.month)  +"-" + str(datetime_result.day)

    return now,menu


