class Sample:
    name = "junaid"

sample = dict(name="junaid dict")
obj = Sample()


def get_attr(obj, attr_name, default=None):
    try:
        if isinstance(obj, dict):
            return obj.__getitem__(attr_name)
        return obj.__getattribute__(attr_name)
    except (KeyError, AttributeError):
        return default

# Usage
print(get_attr(obj, 'name'))
print(get_attr(obj, 'name1'))

print(get_attr(sample, 'name'))
print(get_attr(sample, 'name1'))
