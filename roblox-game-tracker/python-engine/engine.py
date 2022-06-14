from selenium import webdriver
from selenium.webdriver.common.by import By
import psycopg2

# Configuration variables
use_custom_port = True
custom_port = 1234;
database_name = 'test'


class CrawlerEngine:

    def __init__(self):
        options = webdriver.ChromeOptions()
        if use_custom_port:
            options.add_argument(f'--remote-debugging-port={custom_port}')
        self.driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

    def get_text_of_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def navigate_to_page(self, url):
        self.driver.get(url)
        return

    def close(self):
        self.driver.close()
        return


class SQLEngine:
    """This is a class to interface with a Postgres database installation on a local machine."""
    def __init__(self):
        """Initializes connection to Postgres and saves connection object"""
        self.conn = psycopg2.connect(f'dbname={database_name}')
        self.cur = self.conn.cursor()

    def get_table(self, sql_command):
        """Accepts an SQL command string and returns the result from the database"""
        self.cur.execute(sql_command)
        return self.cur.fetchall()

    def close(self):
        """Closes the connection to the database"""
        self.cur.close()
        self.conn.close()
