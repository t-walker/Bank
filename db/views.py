import sqlite3 as sql

def balance_by_user_id(cursor, u_id):
    data = cursor.execute("SELECT amount FROM accounts where user_id = %s" % u_id)
    data = data.fetchone()
    balance = data[0]
    return balance

def name_by_user_id(cursor, id):
    data = cursor.execute("SELECT * FROM users where user_id = %s" % u_id)
    data = data.fetchone()
    first_name = data[1]
    last_name = data[2]
    return



def main():
    try:
        conn = sql.connect('bank.db')
        cur = conn.cursor()
    except:
        print("Can't connect to the database.")

    print(balance_by_user_id(cur, 11112107))
    if conn:
        conn.close()
    return

if __name__ == "__main__":
    main()
