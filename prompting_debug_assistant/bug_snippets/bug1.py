def get_last_n_items(items, n):
    """
    Returns the last n items from a list.
    """
    result = []
    for i in range(len(items) - n, len(items) - 1):
        result.append(items[i])
    return result


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(get_last_n_items(data, 5))