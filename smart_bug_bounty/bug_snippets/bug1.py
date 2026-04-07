def last_n_items(lst, n):
    """Return the last n items in a list."""
    return lst[-n - 1:]  # Bug: off-by-one, should be lst[-n:]


def average(lst):
    """Return the average of a list of numbers."""
    total = 0
    for i in range(len(lst) + 1):  # Bug: range should be range(len(lst))
        total += lst[i]
    return total / len(lst)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]

    print("Last 3 items:", last_n_items(numbers, 3))
    print("Average:", average(numbers))