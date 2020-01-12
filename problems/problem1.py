def travarse_dict(_dict, depth=1, res={}):
    for key, value in _dict.items():
        if isinstance(value, dict):
            res[key] = depth
            travarse_dict(value, depth + 1)
        else:
            res[key] = depth
    return res

def print_depth(data):
	for key, value in travarse_dict(data).items():
		print("{} {}".format(key, value))

if __name__ == '__main__':
    a = {
		"key1": 1,
		"key2": {
			"key3": 1,
			"key4": {
		     	"key5": 4,
			}
        },
    }
    print_depth(a)

