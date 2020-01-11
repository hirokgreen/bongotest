def travarse_dict(_dict, depth=1):
    for key, value in _dict.items():
        if hasattr(value, '__dict__'):
            print(key, depth)
            travarse_dict(value.__dict__, depth + 1)
        elif isinstance(value, dict):
            print(key, depth)
            travarse_dict(value, depth + 1)
        else:
            print(key, depth)

def print_dept(data):
    return travarse_dict(data)

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

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
