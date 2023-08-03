#필요한 모듈 임포트

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from datetime import datetime
import pymysql
import cryptography
import slack_sdk





while True:
    #time.sleep(600) # 10분에 한번 실행
    time.sleep(600)
    # 시크릿 파일 읽기
    with open('secret','r') as f:
        secret = {l.split('=')[0]: l.split('=')[1].rstrip() for l in f.readlines()}

    # 시크릿 파일읽어온 것에서 값 정의
    id_= secret['id'].replace("\'","")
    pw_= secret['pw'].replace("\'","")
    password_= secret['password'].replace("\'","")
    db_= secret['db'].replace("\'","")
    token = secret['SLACK_TOKEN'].replace("\'","")
    channel = secret['SLACK_CHANNEL'].replace("\'","")


    # 최신날짜 가져오기
    conn = pymysql.connect(host='127.0.0.1', user='root', password= password_, db=db_, charset='utf8')
    cur = conn.cursor()

    sql = "SELECT day FROM menu_table ORDER BY day desc limit 1;"
    cur.execute(sql)
    result = cur.fetchone()
    result = (result[0])
    result= result.strftime("%Y-%m-%d")
    conn.close()

    # 오늘 날짜 가져오기
    today = datetime.today().strftime("%Y-%m-%d")
        
        # 만약 오늘날짜 != db날짜 이면, 오늘의 밥상 크롤링
    if today != result:
            #크롤링
        driver = webdriver.Chrome()

        driver.get("https://www.instagram.com")
        driver.implicitly_wait(10)	# 암시적 대기 시간 10초 설정


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
        time.sleep(2)

        # 내용 뽑아서 menu에 저장
        contents = contents[0].text

        menu = contents.split()[3:-2]
        menu = (',').join(menu)
        menu = menu.replace(',', '\n').split('\n')
        
        # 오늘날짜 기록
        now = datetime.today().strftime("%Y-%m-%d")

    else:
        print('오늘날짜 데이터 수집 완료')
        continue

    # 만약 크롤링 했는데 오늘 날짜랑 크롤링 날짜가 같다면.. 계속 크롤링
    if today != now:
        print('아직 안올라옴')
        continue
    
    print("올라왔네요잉")
    
    # 올라왔다면 db에 저장하고 챗봇한테 ㄱㄱ

    # pymysql.connect(host=서버IP주소, user=사용자, passoword=암호, db=데이터베이스, charset=문자세트)

    conn = pymysql.connect(host='127.0.0.1', user='root', password=password_, db=db_, charset='utf8')
    cur = conn.cursor()

    sql = "INSERT INTO menu_table (day, menu) VALUES (%s,%s)"
    val = (now,menu)

    cur.execute(sql,val)
    conn.commit()
    conn.close()
    print('db업데이트 완료')

    # 슬랙봇

    SLACK_TOKEN = token  #본인의 Slack Bot Token 입력
    SLACK_CHANNEL = channel #메시지를 보낼 Channel명 입력


    def Msg_bot(slack_messege):  #slack bot massage
        slack_token = SLACK_TOKEN   #slack bot token
        channel = SLACK_CHANNEL     #chnnel for sending massege from slack bot
        message = slack_messege     #message from slack bot
        client = slack_sdk.WebClient(token=slack_token)
        client.chat_postMessage(channel=channel, text=message)


        # 원래 번호도 하려 했으나... 어려워서 일단 보류
        #real_menu = []
        #for value in enumerate(menu):
            #print(value)
            #real_menu.append(value)


    chat =print("안녕하세요! \n\n\n{}\n\n\n오늘의 밥상 메뉴는 \n\n\n\n {} \n\n\n\n즐거운 점심시간 되세요!".format(now,('\n').join(menu))) # 보낼 메시지 입력

    Msg_bot(chat)




