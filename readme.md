Here's an explanation of the code in `sample.py`:

### Purpose
The code defines a function to check whether a given number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number of digits.

### Breakdown

#### Function Definition
```python
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
```
- Converts the number to a list of its digits.
- Calculates how many digits the number has.
- Sums each digit raised to the power of the number of digits.
- Returns `True` if the sum equals the original number; otherwise, returns `False`.

#### Usage Example
```python
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
```
- Asks the user to enter a number.
- Checks if the entered number is an Armstrong number using the function.
- Prints the result.

### Example
For input `153`:
- Digits: 1, 5, 3
- Number of digits: 3
- Calculation: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
- Output: `153 is an Armstrong number.`

Let me know if you want a more detailed, line-by-line explanation!
