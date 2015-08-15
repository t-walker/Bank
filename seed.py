import random
import sqlite3 as sql

first_names = ["Tyler", "Jason", "James", "Alice", "Walter", "Grace", "Ada",
               "Erin", "Jacob", "Des", "Heather", "Henry", "Beth", "Emily", "Joe"]

last_names = ["Walker", "Swanby", "Mullen", "Johnson", "Bookwalter", "Hopper", "Lovelace",
               "Jahns", "Jacobs", "Marcum", "Moctezuma", "Smith", "Brown", "Jones", "Wilson",
               "Taylor", "Clark", "Moore", "Taylor", "Clarke", "White", "Martin", "Allen",
               "Stephens", "Hall", "Lewis", "King", "Jackson"]


def SSN_print(ssn):
    return ssn[0:3] + "-" + ssn[3:5] + "-" + ssn[5:]


def drop_table(cursor, table):
    cursor.execute("DELETE FROM %s *" % table)


def users_seed(cursor):
    cursor.execute("DELETE FROM users")
    people = []
    user_id = 11111111
    for i in range(1000):
        first_name = first_names[random.randint(0,len(first_names) - 1)] # Random First Name
        last_name  = last_names[random.randint(0,len(last_names) - 1 )]   # Random Last Name
        SSN = ""
        user_id += 1
        for j in range(9):
            SSN += str(random.randint(0,9))
        SSN = SSN_print(SSN)
        people.append((user_id, first_name, last_name, SSN))

    cursor.executemany('INSERT INTO users(user_id, first_name,last_name,SSN) VALUES (?,?,?,?)', people)
    return


def accounts_seed(cursor):
    user_ids = []
    account_id = 1111
    cursor.execute("DELETE FROM accounts")
    cursor.execute('SELECT * FROM users')
    fetch = cursor.fetchall()
    for user in fetch:
        user_ids.append(user[0])
    for u_id in user_ids:
        a_id_c = account_id
        account_id += 1
        a_id_s = account_id
        account_id += 1
        nickname_c = "Checking"
        nickname_s = "Saving"
        user_id = u_id
        amount = 0
        values = (a_id_c, nickname_c, 0.0, amount, u_id)
        cursor.execute('INSERT INTO accounts(account_id, nickname, interest_rate, amount, user_id) VALUES (?,?,?,?,?)', values)
        amount = 0
        values = (a_id_s, nickname_s, 0.0, amount, u_id)
        cursor.execute('INSERT INTO accounts(account_id, nickname, interest_rate, amount, user_id) VALUES (?,?,?,?,?)', values)

    return


def transactions_seed():
    return


def main():
    try:
        conn = sql.connect('bank.db')
        cur = conn.cursor()
    except:
        print("Can't connect to the database.")

    users_seed(cur)
    accounts_seed(cur)
    conn.commit()
    if conn:
        conn.close()
    return

if __name__ == "__main__":
    main()
