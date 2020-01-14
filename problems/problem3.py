class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

def get_path_values(node):
    # finding path values of node as list1
    values = []
    while node and node.value:
        values.append(node.value)
        node = node.parent
    return values

def get_lca(node1, node2):
    list1 = get_path_values(node1)
    list2 = get_path_values(node2)

    # finding last common element in the path
    for item in zip(list1[::-1], list2[::-1]):
        if item[0] == item[1]:
            ans = item[0]
    return ans
    
def lca(node1, node2):
    print(get_lca(node1, node2))
    

if __name__ == '__main__':
    n8 = Node(8)
    n9 = Node(9)

    n6 = Node(6)
    n7 = Node(7)

    n4 = n9.parent = n8.parent = Node(4)
    n5 = Node(5)

    n2 = n4.parent = n5.parent = Node(2)
    n3 = n6.parent = n7.parent = Node(3)
    n1 = n2.parent = n3.parent = Node(1)

    lca(n6, n7)
    lca(n3, n7)
