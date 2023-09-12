#필요한 모듈 임포트

import time
from datetime import datetime
from read_file import read_file
from crawler import crawler
from db import get_today, save_db, connect_db
from obap_slack import msg_bot


while True:
    time.sleep(600) # 10(600초)분에 한번 실행

    secret = read_file()

    # 최신날짜 가져오기
    connection = connect_db(secret)  # get_today 함수에서 close() 를 해주기 때문에 나중에 쓸 때 다시 연결해 줘야함
    result = get_today(connection)

    # 오늘 날짜 가져오기
    today = datetime.today().strftime("%Y-%m-%d")
        
        # 만약 오늘날짜 != db날짜 이면, 오늘의 밥상 크롤링
    if today != result:
            #크롤링
        now_menu = crawler(secret)
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
    connection = connect_db(secret) 
    save_db(connection, now, menu)

    # pymysql.connect(host=서버IP주소, user=사용자, passoword=암호, db=데이터베이스, charset=문자세트)

    # 슬랙봇
    chat = "안녕하세요! 오밥요정입니다!\n\n\n\n{}\n\n\n\n 오늘의 밥상 메뉴는 \n\n\n\n {} \n\n\n\n 즐거운 점심시간 되세요!".format(now,('\n').join(menu)) # 보낼 메시지 입력
    msg_bot(secret, chat)
    break