import unittest
from main import to_upper

class TestMain(unittest.TestCase):
    def test_to_upper(self):
        name = "Chandhana"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "CHANDHANA")

if __name__ == '__main__':
    unittest.main()