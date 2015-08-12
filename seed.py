import random

first_names = ["Tyler", "Jason", "James", "Alice", "Walter", "Grace", "Ada",
               "Erin", "Jacob", "Des", "Heather", "Henry", "Beth", "Emily", "Joe"]

last_names = ["Walker", "Swanby", "Mullen", "Johnson", "Bookwalter", "Hopper", "Lovelace",
               "Jahns", "Jacobs", "Marcum", "Moctezuma", "Smith", "Brown", "Jones", "Wilson",
               "Taylor", "Clark", "Moore", "Taylor", "Clarke", "White", "Martin", "Allen",
               "Stephens", "Hall", "Lewis", "King", "Jackson"]


def drop_table(cursor, table):
    cursor.execute("DELETE FROM %s *" %s table)


def users_seed(cursor):
    names = []
    for i in range(1000):
        first_name = first_names[random.randint(0,len(first_names) - 1)] # Random First Name
        last_name  = last_names[random.randint(0,len(last_names) - 1 )]   # Random Last Name

        names.append((first_name, last_name))
    for first, last in names:
        cursor.execute("""INSERT INTO users
                          (first_name, last_name, SSN)
                          VALUES (?,?,?)
                       """, (first_name, last_name, SSN))

    return


def accounts_seed():
    return


def transactions_seed():
    return

users_seed()
