import sqlite3

con = sqlite3.connect('addr.db') # db생성
cs = con.cursor();
dropsql = 'DROP TABLE IF EXISTS tb_addr';
creatsql = '''
    CREATE TABLE tb_addr(
        name CHAR(16) PRIMARY KEY,
        phone CHAR(16),
        addr TEXT
    )
''';

cs.execute(dropsql);
cs.execute(creatsql);
con.commit();

cs.close(); # 2개의 연결통로
con.close(); # connection이 맺어지면 반드시 만들어야 함

#create db
