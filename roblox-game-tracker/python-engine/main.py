import time
from driver import Driver

driver = Driver('test', 'test2', 'url', ['name', 'date_updated', 'description'])

# TODO: Add SIGINT and SIGTERM handlers
while True:
    driver.iterate()
    time.sleep(10)

driver.close()
