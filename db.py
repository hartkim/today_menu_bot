import pymysql
import cryptography


# 최신날짜 가져오기
def get_today():

    with open('secret','r') as f:
        secret = {l.split('=')[0]: l.split('=')[1].rstrip() for l in f.readlines()}
        
    host_= secret['host'].replace("\'","")
    user_= secret['user'].replace("\'","")
    password_= secret['password'].replace("\'","")
    db_= secret['db'].replace("\'","")

    conn = pymysql.connect(host = host_,user = user_,password= password_,db=db_,charset ='utf8')
    cur = conn.cursor()

    sql = "SELECT day FROM menu_table ORDER BY day desc limit 1;"
    cur.execute(sql)
    result = cur.fetchone()
    result = (result[0])
    result= result.strftime("%Y-%m-%d")
    conn.close()
    return result
    

# 데이터 저장하기
def save_db(now,menu):
    with open('secret','r') as f:
        secret = {l.split('=')[0]: l.split('=')[1].rstrip() for l in f.readlines()}
        
    host_= secret['host'].replace("\'","")
    user_= secret['user'].replace("\'","")
    password_= secret['password'].replace("\'","")
    db_= secret['db'].replace("\'","")

    menu = (',').join(menu)

    conn = pymysql.connect(host = host_,user = user_,password= password_,db=db_,charset ='utf8')
    cur = conn.cursor()

    sql = "INSERT INTO menu_table (day, menu) VALUES (%s,%s)"
    val = (now,menu)
    print(now)
    print(menu)

    cur.execute(sql,val)
    conn.commit()
    conn.close()
    return print('db업데이트 완료')