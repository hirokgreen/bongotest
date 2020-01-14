import unittest
from problems.problem3 import Node, get_lca

class TestLCA(unittest.TestCase):
    def test_lca(self):
        n8 = Node(8)
        n9 = Node(9)
        n6 = Node(6)
        n7 = Node(7)
        n4 = n9.parent = n8.parent = Node(4)
        n5 = Node(5)
        n2 = n4.parent = n5.parent = Node(2)
        n3 = n6.parent = n7.parent = Node(3)
        n1 = n2.parent = n3.parent = Node(1)

        self.assertEqual(get_lca(n3, n7), 3)
        self.assertEqual(get_lca(n6, n7), 3)
        self.assertEqual(get_lca(n8, n5), 2)
        self.assertEqual(get_lca(n5, n6), 1)

if __name__ == '__main__':
    unittest.main()
