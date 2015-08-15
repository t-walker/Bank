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
    people = []
    for i in range(1000):
        first_name = first_names[random.randint(0,len(first_names) - 1)] # Random First Name
        last_name  = last_names[random.randint(0,len(last_names) - 1 )]   # Random Last Name
        SSN = ""
        for j in range(9):
            SSN += str(random.randint(0,9))
        SSN = SSN_print(SSN)
        people.append((first_name, last_name, SSN))

    cursor.executemany('INSERT INTO users(first_name,last_name,SSN) VALUES (?,?,?)', people)
    return


def accounts_seed():
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

    conn.commit()
    if conn:
        conn.close()
    return

if __name__ == "__main__":
    main()
