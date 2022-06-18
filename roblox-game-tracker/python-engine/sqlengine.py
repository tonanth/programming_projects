import psycopg2

class SQLEngine:
    """This is a class to interface with a Postgres database installation on a local machine."""

    def __init__(self,
                 database_name: str,
                 ):
        """Initializes connection to Postgres and saves connection object"""
        self.conn = psycopg2.connect(f'dbname={database_name}')
        self.cur = self.conn.cursor()

    def get_table(self, sql_command):
        """Accepts an SQL command string and returns the result from the database"""
        self.cur.execute(sql_command)
        self.conn.commit()
        return self.cur.fetchall()

    def update_table(self, sql_command):
        """Updates database and does not return anything"""
        self.cur.execute(sql_command)
        self.conn.commit()
        return

    def close(self):
        """Closes the connection to the database"""
        self.cur.close()
        self.conn.close()
        return
