from engines.crawlerengine import CrawlerEngine
from engines.sqlengine import SQLEngine
from typing import List


class Driver:
    def __init__(self,
                 database_name: str,
                 table_name: str,
                 url_field: str,
                 attribute_list: List[str],
                 enable_test_game: bool = False):
        self.game_urls = []
        self.database_name = database_name
        self.table_name = table_name
        self.url_field = url_field
        self.attribute_list = attribute_list
        # TODO: Temporary custom port enablement, remove when implement config file
        self.crawler = CrawlerEngine(attribute_list, use_custom_port=True)
        self.sql = SQLEngine(table_name, database_name)
        self.finished = True

    # TODO finish implementing
    def get_test_game(self):
        self.driver.get('https://google.com')
        print('implement this')

    def iterate(self):
        if not self.game_urls:
            self.game_urls.extend(self.sql.read_col(self.url_field))
        if self.game_urls:
            game_url = self.game_urls.pop()
            game_attr = self.crawler.get_attributes_from_url(game_url)
            self.sql.update_row(self.attribute_list, game_attr, self.url_field, game_url)
        return

    def close(self):
        self.crawler.close()
        self.sql.close()
