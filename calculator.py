# calculator.py

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # ZeroDivisionError if list is empty


def apply_discount(price, discount_percent):
    # Bug: should divide by 100, not multiply
    discount_amount = price * discount_percent * 100
    return price - discount_amount


def find_max(items):
    # Bug: starts at 0, fails for all-negative lists
    max_value = 0
    for item in items:
        if item > max_value:
            max_value = item
    return max_value