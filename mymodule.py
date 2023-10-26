# Variable-length arguments (*args):
def calculate_sum(*args):
    """This function calculates the sum of variable-length arguments."""
    total = 0
    for num in args:
        total += num
    return total
