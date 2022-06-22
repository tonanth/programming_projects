import time
from driver import Driver

driver = Driver('test', 'test2', 'url', ['name', 'date_updated', 'description'])

while True:
    driver.iterate()
    time.sleep(10)

driver.close()
