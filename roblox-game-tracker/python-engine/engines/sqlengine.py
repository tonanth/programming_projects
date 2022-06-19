import psycopg2
import getpass


class SQLEngine:
    """Accesses and modifies a Postgres database using psycopg2 module.

    This class opens and stores a connection to a Postgres database on the local machine. The connection is opened in
    the constructor and will remain active and stored in object memory. After an SQLEngine has been created,
    the database can be read using get_table and updated using update_table The connection is provided by the module
    psycopg2. The connection will be maintained until closed by calling the close function.
    """

    def __init__(self,
                 database_name: str,
                 database_user: None):
        """Initializes connection to Postgres and saves connection object.
            Args:
                database_name: The name of the database to use.
                database_user: The name of the user to log into the database as. If None is supplied, it will default to
                    the user calling the program.
                    Default: None
        """
        database_user = getpass.getuser() if database_user is None else database_user
        self.conn = psycopg2.connect(f'dbname={database_name} user={database_user}')
        self.cur = self.conn.cursor()

    def read_col(self, col_name: str):
        """Accepts a column name and will return all rows from column"""
        self.cur.execute("")
        self.conn.commit()
        return self.cur.fetchall()

    def update_table(self, col_names, rows, primary_row):
        """Updates database using primary_row to target desired rows"""

        self.cur.execute()
        self.conn.commit()
        return

    def close(self):
        """Closes the connection to the database"""
        self.cur.close()
        self.conn.close()
        return
