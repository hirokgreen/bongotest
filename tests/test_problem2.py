import unittest
from problems.problem2 import travarse_dict, Person

class TestDictDept(unittest.TestCase):
	def test_depth(self):
		person_a = Person("User", "1", None)
		person_b = Person("User", "2", person_a)
		test_data = {"key1": 1,"key2": {"key3": 1,"key4": {"key5": 4, "user": person_b}},}
		res_data = travarse_dict(test_data)
		self.assertEqual(res_data[0][1], 1) #key1 1
		self.assertEqual(res_data[4][1], 3) #key5 3
		self.assertEqual(res_data[8][1], 4) #father 4
		self.assertEqual(res_data[11][1], 5) #father 5

if __name__ == '__main__':
    unittest.main()
