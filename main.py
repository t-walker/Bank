import mysql.connector as sql # Imports the proper SQL stuff
import db.models as models
import db.seed as seed

class Connection:
    """This class is used to connect to the database."""
    def __init__(self):
        self.connection = sql.connect(user='bankadmin', password='bankadmin', database='bank')
        return

    def commit(self):
        self.connection.commit()

    def cursor(self):
        cursor = self.connection.cursor(buffered=True)
        return cursor

    def kill(self):
        """Closes the current SQL Connection"""
        self.connection.close()
        print("Connection killed.")

def main():
    connection = Connection()
    cursor = connection.cursor()

    models.create_models(cursor)
    seed.seed_data(cursor)
    connection.commit()

    connection.kill()
    return

if __name__ == "__main__":
    main()
