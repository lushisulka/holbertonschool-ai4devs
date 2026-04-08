def get_last_items(lst, n):
    if n < 0:
        return []

    return lst[-n:]  # FIXED

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(get_last_items(data, 2))  # Expected output: [4, 5]