import sqlite3 as sql

def table_exists(cur, table_name):
    try:
        cur.execute("SELECT * from %s" % table_name)
    except:
        return 0
    return 1
