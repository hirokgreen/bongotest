import unittest
from problems.problem1 import travarse_dict

class TestDictDept(unittest.TestCase):

    def test_depth(self):
        test_data = {"key1": 1,"key2": {"key3": 1,"key4": {"key5": 4,}},}
        res_data = travarse_dict(test_data)
        self.assertEqual(res_data["key1"], 1)
        self.assertEqual(res_data["key3"], 2)
        self.assertEqual(res_data["key5"], 3)

if __name__ == '__main__':
    unittest.main()
