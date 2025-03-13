def find_common(set1: set, set2: set) -> set:
    result: set = set1.intersection(set2)
    return result


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

answer = find_common(set1, set2)
print(answer)