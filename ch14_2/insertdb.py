import sqlite3

con= None;
cs = None;

try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    insertsql = 'INSERT INTO tb_addr VALUES ("%s","%s","%s")';
    name = input('Input Name:');
    phone = input('Input Phone:');
    addr = input('Input Addr:');
    cs.execute(insertsql % (name, phone, addr));
    con.commit();

except:
    print('Duplicated ID Error');

finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();

