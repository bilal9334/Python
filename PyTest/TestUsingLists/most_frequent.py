def most_frequent(numbers: list) -> int:
    result = max(set(numbers), key=numbers.count)
    return result


numbers = [1, 3, 3, 2, 1, 3, 4, 1, 1]
answer = most_frequent(numbers)
print(answer)