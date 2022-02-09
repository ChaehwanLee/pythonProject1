# itemsql.py

MAKE_TABLE = """
    CREATE TABLE IF NOT EXIST tb_item(
        id int PRIMARY KEY,
        name CHAR(20),
        price INT,
        rate REAL    
    )
""";

# 한 번 테이블을 만들어 놨으면 안 만들어도 된다.
#spl문만 관리

ITEM_INSERT = """
    INSERT INTO tb_item VALUES (%d, "%s", %d, %f)
""";

ITEM_UPDATE = """
    UPDATE tb_item SET name="%s", price=%d, rate=%f WHERE id=%d
""";

ITEM_DELETE = """
    DELETE FROM tb_item WHERE id=%d
""";
ITEM_SELECT_ONE = """
    SELECT * FROM tb_item WHERE id=%d
""";
ITEM_SELECT = """
    SELECT * FROM tb_item
""";