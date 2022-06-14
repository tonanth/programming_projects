from engine import CrawlerEngine, SQLEngine
from config import attribute_xpath_dict
import time

page_delay = 10             # Time delay in seconds between each game page load to avoid rate limiting
loop_infinitely = False     # Check games continuously instead of just a single pass

class Driver:
    def __init__(self):
        self.crawler = CrawlerEngine()
        self.sql = SQLEngine()

    # TODO finish implementing
    def get_test_game(self):
        self.driver.get('https://google.com')
        print('implement this')
        # Have the driver test out a sample game place

    # Get table of games
    def get_game_table(self):
        table = self.sql.
