#select1db.py

import sqlite3

con= None;
cs = None;

try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    selectsql = 'SELECT * FROM tb_addr WHERE name=%s';
    name = input('Input Name...');
    cs.execute(selectsql % (name));
    datas = cs.fetchone();
    print('이름은 %s, 전화번호는 %s, 주소는 %s' % data);

except:
    print('Error');

finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();

