import pymysql
import pymysql.cursors

_db = pymysql.connect(
    host = 'woSIN.mysql.pythonanywhere-services.com',
    port = 3306,
    user = 'woSIN',
    password = '!10JwsJws10',
    db = 'woSIN$ubion'
)

## cursor 생성
cursor = _db.cursor(pymysql.cursors.DictCursor)

## table 생성 쿼리문 
create_user = """
    create table 
    if exists    
    user(
    id varchar(32) primary key,
    password varchar(64) not null,
    name varchar(32) not null
    )
"""

## sql 쿼리문 실행
cursor.execute(create_user)
# 동기화
_db.commit()
# 서버와의 연결을 종료
_db.close()
print('table 생성 완료')



