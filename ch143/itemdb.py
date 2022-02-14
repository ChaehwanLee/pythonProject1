# itemdb.py
import sqlite3,itemsql

def connect(dbname):
    con = sqlite3.connect(dbname);
    return con;
def close(*cs):
    for c in cs:
        if c is not None:
            c.close();

def makeTable(name):
    try:
        con = connect(name);
        cs = con.cursor();
        cs.execute(itemsql.MAKE_TABLE);
        con.commit();
    except:
        print('Make Table Error');
    finally:
        close(cs,con);


def insert(*data):
    try:
        con = connect('item.db');
        cs = con.cursor();
        cs.execute(itemsql.ITEM_INSERT % data);
        con.commit();
    except:
        raise Exception;
    finally:
        close(cs, con);


def delete(id):
    try:
        con = connect('item.db');
        cs = con.cursor();
        cs.execute(itemsql.ITEM_DELETE % (id));
        con.commit();
    except:
        raise Exception;
    finally:
        close(cs, con);

def update(*data):
    try:
        con = connect('item.db');
        cs = con.cursor();
        cs.execute(itemsql.ITEM_UPDATE % data);
        con.commit();
    except:
        raise Exception;
    finally:
        close(cs, con);

def selectone(id):
    try:
        con = connect('item.db');
        cs = con.cursor();
        cs.execute(itemsql.ITEM_SELECT_ONE % (id));
        results = cs.fetchone();
    except:
        raise Exception;
    finally:
        close(cs, con);
    return results;

def select():
    try:
        con = connect('item.db');
        cs = con.cursor();
        cs.execute(itemsql.ITEM_SELECT);
        results = cs.fetchall();
    except:
        raise Exception;
    finally:
        close(cs, con);
    return results;

def selectui():
    try:
        con = connect('item.db');
        cs = con.cursor();
        cs.execute(itemsql.ITEM_SELECT);
        results = cs.fetchall();
    except:
        raise Exception;
    finally:
        close(cs, con);
    return results;



if __name__ == '__main__':
    #makeTable('item.db');
    # try:
    #     insert(104,'pants',10000,3.4);
    # except:
    #     print('Error');
    try:
        results = select();
        for data in results:
            print('%d %s %d %f' % data);
    except:
        print('Error');

    # try:
    #     result = selectone()
    #
    # try:
    #     update('shirts',20000,5.4,100);
    # except:
    #     print('Error');