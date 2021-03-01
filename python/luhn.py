def luhn(card_number):
    """
    Test whether a bankcard number passes the Luhn algorithm.
    """
    card_number = str(card_number)
    sum = 0
    num_digits = len(card_number)
    odd_even = num_digits & 1

    for i in range(0, num_digits):
        digit = int(card_number[i])
        if not ((i & 1) ^ odd_even):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit

    return (sum % 10) == 0
