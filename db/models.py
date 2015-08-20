import sqlite3 as sql
import test_model
import seed

def user(cursor):
    # A user has many accounts
    # CREATE TABLE USER (account_id int NOT NULL, first_name varchar(100), last_name var_char(100), SSN, varchar(9), PRIMARY KEY(account_id))
    cursor.execute("""CREATE TABLE users (
                                          user_id INT NOT NULL,
                                          first_name VARCHAR(100),
                                          last_name VARCHAR(100),
                                          SSN VARCHAR(11),
                                          PRIMARY KEY(user_id));""")
    if test_model.table_exists(cursor, "users"):
        print("Users Exists.")
    return


def account(cursor):
    # An account belongs to a user
    # An account has many transactions

    cursor.execute("""CREATE TABLE accounts (
                                             account_id INT,
                                             nickname VARCHAR(100),
                                             interest_rate DECIMAL(10,5),
                                             amount DECIMAL(30,2),
                                             user_id INT REFERENCES USERS(user_id),
                                             PRIMARY KEY(account_id));""")
    if test_model.table_exists(cursor, "accounts"):
        print("Accounts Exists.")
    return


def transaction(cursor):
    # A transaction belongs to an account

    cursor.execute("""CREATE TABLE transactions (
                                                 transaction_id INT,
                                                 vendor VARCHAR(100),
                                                 amount DECIMAL(10,5),
                                                 sign BOOLEAN,
                                                 account_id INT REFERENCES accounts(account_id),
                                                 user_id INT REFERENCES users(user_id),
                                                 PRIMARY KEY(transaction_id));""")
    if test_model.table_exists(cursor, "transactions"):
        print("Transactions Exists.")
    return


def main():
    # Connect to the database.
    try:
        conn = sql.connect('bank.db')
        cur = conn.cursor()
    except:
        print("Can't connect to the database.")

    # Create Users table.
    if not test_model.table_exists(cur, "users"):
        user(cur)
    else:
        if test_model.table_exists(cur, "users"):
            print("Users Exists.")

    # Create Accounts table.
    if not test_model.table_exists(cur, "accounts"):
        account(cur)
    else:
        if test_model.table_exists(cur, "accounts"):
            print("Accounts Exists.")

    # Create Accounts table.
    if not test_model.table_exists(cur, "transactions"):
        transaction(cur)
    else:
        if test_model.table_exists(cur, "transactions"):
            print("Transactions Exists.")

    # Close Connection.
    if conn:
        conn.close()
    return

if __name__ == '__main__':
    main()
