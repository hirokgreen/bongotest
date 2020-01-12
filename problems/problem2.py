def travarse_dict(_dict, depth=1, res=[]):
	for key, value in _dict.items():
		if hasattr(value, '__dict__'):
			res.append((key, depth))
			travarse_dict(value.__dict__, depth + 1)
		elif isinstance(value, dict):
			res.append((key, depth))
			travarse_dict(value, depth + 1)
		else:
			res.append((key, depth))
	return res

def print_dept(data):
	for item in  travarse_dict(data):
		print("{} {}".format(item[0], item[1]))

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


if __name__ == '__main__':
	person_a = Person("User", "1", None)
	person_b = Person("User", "2", person_a)

	a = {
		"key1": 1,
		"key2": {
		    "key3": 1,
		    "key4": {
		        "key5": 4,
		        "user": person_b,
		    }
		},
	}
	print_dept(a)
