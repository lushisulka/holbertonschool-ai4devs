# Intended: Remove duplicates while preserving order

def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return sorted(result)  # BUG


if __name__ == "__main__":
    data = [3, 1, 2, 3, 2]
    print(remove_duplicates(data))  # Expected: [3,1,2]