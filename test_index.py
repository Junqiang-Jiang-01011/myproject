import unittest
from my_index import get_info

class TestIndex(unittest.TestCase):
    def test_get_info(self):
        self.assertEqual(get_info('Jason'), 'hello world from Jason')

if __name__=="__main__":
    unittest.main()