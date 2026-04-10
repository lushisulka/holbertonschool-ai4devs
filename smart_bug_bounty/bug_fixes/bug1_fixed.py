def get_last_items(lst, n):
    if n < 0:
        return []

    return lst[-n:]


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(get_last_items(data, 2))