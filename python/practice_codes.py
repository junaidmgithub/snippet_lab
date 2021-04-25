# Odd or Even
def is_odd_even(x):
    return x & 1

def is_odd_number(x):
    return is_odd_even(x) == 1

def is_even_number(x):
    return is_odd_even(x) == 0


# retry max-attempt a task
import requests
max_attempts = 5
for _ in range(max_attempts):
    try:
        response = requests.get('https://www.google.co.in')
        break
    except Exception as e:
        pass

#
