from psycopg2 import * # Imports all of MySQL


def user():
    # A user has many accounts

    #TODO Create User Table with Columns (account_id, first_name, last_name, SSN)
    # CREATE TABLE USER (account_id int NOT NULL, first_name varchar(100), last_name var_char(100), SSN, varchar(9), PRIMARY KEY(account_id))
    return


def account():
    # An account belongs to a user
    # An account has many transactions

    #TODO Create Account Table with Columns (account_id, nick_name, interest_rate)
    return


def transaction():
    # A transaction belongs to an account

    #TODO Create Account Table with Columns (account_id, transaction_id, amount, credit/debit)
    return


def main():

    try:
        conn = psycopg2.connect("dbname='banking' user='bankadmin' host='localhost' password='dbpass123'")
    except:

    #check if tables exist
    if
    return
