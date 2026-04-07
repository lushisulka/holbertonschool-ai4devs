def factorial(n):
    """Return the factorial of n using recursion."""
    if n == 0:
        return 1
    return n * factorial(n)  # Bug: should be factorial(n - 1), causes infinite recursion


def count_down(n):
    """Print numbers from n down to 1."""
    while n > 0:
        print(n)
        # Bug: n is never decremented — infinite loop
    print("Done!")


def find_max(numbers):
    """Return the maximum number in a list."""
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val == num  # Bug: comparison instead of assignment
    return max_val


if __name__ == "__main__":
    print(find_max([3, 1, 7, 2, 5]))