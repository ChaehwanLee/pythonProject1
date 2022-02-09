import sqlite3

con= None;
cs = None;

try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    insertsql = 'INSERT INTO tb_addr VALUES ("james3","123111","seoul")';
    cs.execute(insertsql);
    con.commit();

except:
    print('Duplicated ID Error');

finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();

