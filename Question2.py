# START

def special_percentile(percent, numbers):
    """
    Returns the special percentile value from a list of numbers.
    """
    numbers.sort()
    position = int((percent / 100) * len(numbers))
    position = min(position, len(numbers) - 1)
    return numbers[position]

# print(special_percentile(25, [40, 10, 30, 20])) -> 20
# print(special_percentile(25, [50, 10, 40, 30, 20])) -> 20
# print(special_percentile(50, [9, 1, 7, 3])) -> 7

# STOP