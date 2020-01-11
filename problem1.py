a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
        }
    },
}

def travarse_dict(_dict, depth=1):
    for key, value in _dict.items():
        if isinstance(value, dict):
            print(key, depth)
            travarse_dict(value, depth + 1)
        else:
            print(key, depth)

def print_dept(data):
    return travarse_dict(data)

print_dept(a)
