import unittest

from sqlengine import SQLEngine

class MyTestCase(unittest.TestCase):
    
    def test_something(self):

        sqlengine = SQLEngine(database_name="test")


if __name__ == '__main__':
    unittest.main()
