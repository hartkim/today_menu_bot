#필요한 모듈 임포트

import time
from datetime import datetime
from Crawler import crawler
from db import get_today
from db import save_db
from slack import Msg_bot

while True:
    time.sleep(600) # 10분에 한번 실행
    #time.sleep(600)
    # 최신날짜 가져오기
    result = get_today()

    # 오늘 날짜 가져오기
    today = datetime.today().strftime("%Y-%m-%d")
        
        # 만약 오늘날짜 != db날짜 이면, 오늘의 밥상 크롤링
    if today != result:
            #크롤링
        now_menu = crawler()
        now = now_menu[0]
        menu = now_menu[1]
    else:
        print('오늘날짜 데이터 수집 완료')
        continue

    # 만약 크롤링 했는데 오늘 날짜랑 크롤링 날짜가 같다면.. 계속 크롤링
    if today != now:
        print('아직 안올라옴')
        continue
    
    print("올라왔네요잉")
    
    # 올라왔다면 db에 저장하고 챗봇한테 ㄱㄱ

    save_db(now,menu)

    # pymysql.connect(host=서버IP주소, user=사용자, passoword=암호, db=데이터베이스, charset=문자세트)

    # 슬랙봇

    chat = "안녕하세요! \n\n\n\n{}\n\n\n\n 오늘의 밥상 메뉴는 \n\n\n\n {} \n\n\n\n 즐거운 점심시간 되세요!".format(now,('\n').join(menu)) # 보낼 메시지 입력
    Msg_bot(chat)