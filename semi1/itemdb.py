# itemdb.py
from semi1 import itemsql
from semi1.db import Db

class ItemDb(Db):
    def __init__(self,dbname):
        super().__init__(dbname);
        super().makeTableitem();

    def insert(self, item):
        cs = None;
        con = None;
        try:
            con = super().connect();
            cs = con.cursor();
            cs.execute(item.getsql().strip());
            con.commit();
        except:
            raise Exception;
        finally:
            super().close(cs, con);

