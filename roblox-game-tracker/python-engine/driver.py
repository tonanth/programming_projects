from engine import CrawlerEngine, SQLEngine
from config import attribute_xpath_dict
import time

from typing import Tuple, List
import time

loop_infinitely = False  # Check games continuously instead of just a single pass


class Driver:
    def __init__(self,
                 database_name: str,
                 table_name: str,
                 url_key: str,
                 attribute_selector_mapping: List[str],
                 page_change_delay: int = 10):
        self.database_name = database_name
        self.table_name = table_name
        self.url_key = url_key
        self.attribute_selector_mapping = attribute_selector_mapping
        self.page_change_delay = page_change_delay
        self.crawler = CrawlerEngine()
        self.sql = SQLEngine(database_name)

    # TODO finish implementing
    def get_test_game(self):
        self.driver.get('https://google.com')
        print('implement this')

    def execute(self):
        games = self.sql.get_table(f'SELECT {self.url_key} FROM {self.table_name}')
        for

    def close(self):
        self.crawler.close()
        self.sql.close()
