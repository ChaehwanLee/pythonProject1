# deletedb.py

import sqlite3

con= None;
cs = None;

try:
    con = sqlite3.connect('addr.db');
    cs = con.cursor();
    deletesql = 'DELETE FROM tb_addr WHERE name="%s" ';
    name = input('Input Name:');

    cs.execute(deletesql % (name));
    con.commit();

except:
    print('Error');

finally:
    if cs is not None:
        cs.close();
    if con is not None:
        con.close();

