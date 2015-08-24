class Account:
    def __init__(self):
        # TODO:
        # POPULATE THE ATTRIBUTES
        self.attributes = {}
        return

    def create(self, attributes):
        # TODO:
        # INSERT INTO DATABASE GIVEN ATTRIBUTES
        sql = ""
        return

    def update(self, account_id, attributes):
        # TODO:
        # UPDATE THE RECORD GIVEN NEW ATTRIBUTES
        sql = ""
        return

    def remove(self, account_id):
        # TODO:
        # REMOVE ACCOUNT
        sql = "DELETE FROM ACCOUNTS WHERE account_id is (%s)" % (account_id)
        return

    def commit(self, connection):
        connection.commit()
