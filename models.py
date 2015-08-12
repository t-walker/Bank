import sqlite3 as sql
import test_model


def user(cursor):
    # A user has many accounts
    # CREATE TABLE USER (account_id int NOT NULL, first_name varchar(100), last_name var_char(100), SSN, varchar(9), PRIMARY KEY(account_id))
    cursor.execute("""CREATE TABLE users (account_id int NOT NULL, first_name CHAR(100), last_name CHAR(100), SSN CHAR(9), PRIMARY KEY(account_id));""")
    return


def account(cursor):
    # An account belongs to a user
    # An account has many transactions

    cursor.execute("""CREATE TABLE accounts (account_id int NOT NULL, nickname CHAR(100), interest_rate DECIMAL(10,5));""")
    if test_model.table_exists(cursor, "accounts"):
        print("Accounts Exists.")
    return


def transaction(cursor):
    # A transaction belongs to an account

    #TODO Create Account Table with Columns (account_id, transaction_id, amount, credit/debit)
    return


def main():

    try:
        conn = sql.connect('bank.db')
        cur = conn.cursor()
    except:
        print("Can't connect to the database.")

    # Create Users table.
    if not test_model.table_exists(cur, "users"):
        user(cur)
    else:
        if test_model.table_exists(cursor, "users"):
            print("Users Exists.")

    # Create Accounts table. 
    if not test_model.table_exists(cur, "accounts"):
        account(cur)
    else:
        if test_model.table_exists(cursor, "accounts"):
            print("Accounts Exists.")

    if conn:
        conn.close()
    return

if __name__ == '__main__':
    main()