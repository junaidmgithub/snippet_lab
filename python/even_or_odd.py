def is_odd_even(x):
    return x & 1

def is_odd_number(x):
    return is_odd_even(x) == 1

def is_even_number(x):
    return is_odd_even(x) == 0

# test
odds = [1, 101, 1001, 12345]
evens = [2, 102, 1002, 123456]
for i in odds:
    assert is_odd_number(i) == True
    assert is_even_number(i) == False
for i in evens:
    assert is_odd_number(i) == False
    assert is_even_number(i) == True
