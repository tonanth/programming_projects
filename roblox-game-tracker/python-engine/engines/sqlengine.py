import psycopg2
from psycopg2 import sql
import getpass


class SQLEngine:
    """Accesses and modifies a Postgres database using psycopg2 module.

    This class opens and stores a connection to a Postgres database on the local machine. The connection is opened in
    the constructor and will remain active and stored in object memory. After an SQLEngine has been created,
    the database can be read using get_table and updated using update_table The connection is provided by the module
    psycopg2. The connection will be maintained until closed by calling the close function.
    """

    def __init__(self,
                 table_name,
                 database_name: str,
                 database_user: str = None):
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
        self.table_name = table_name

    def read_col(self, col_name: str):
        """Accepts a column name and will return all rows from column"""
        query = sql.SQL("select {field} from {table}").format(field=sql.Identifier(col_name),
                                                              table=sql.Identifier(self.table_name))
        self.cur.execute(query)
        return self.cur.fetchall()

    def update_row(self, col_names, row, primary_col, primary_value):
        """Updates database using primary_col to target desired row"""
        if len(col_names) != len(row):
            raise ValueError("col_names and row must have the same length")
        for col_name, value in zip(col_names, row):
            query = sql.SQL('update {table} set {field} = %s where {target} = %s').format(
                table=sql.Identifier(self.table_name),
                field=sql.Identifier(col_name),
                target=sql.Identifier(primary_col))
            self.cur.execute(query, (value, primary_value))
        self.conn.commit()
        return

    def rollback(self):
        """Rollback transactions when a bad SQL call has been placed"""
        self.conn.rollback()

    def close(self):
        """Closes the connection to the database"""
        self.cur.close()
        self.conn.close()
        return
