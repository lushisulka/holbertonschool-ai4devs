def concatenate_numbers(numbers):
    """
    Concatenate all numbers into a single string.
    """
    result = ""
    for num in numbers:
        result += num
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(concatenate_numbers(nums))