```python name=armstrong_check.py
def is_armstrong_number(num):
    """
    Checks whether a given number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    For example: 153 = 1^3 + 5^3 + 3^3

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(num)]
    num_digits = len(digits)
    total = sum(d ** num_digits for d in digits)
    return total == num

# Example usage:
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
```
