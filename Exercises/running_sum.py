def runningSum(nums: list[int]) -> list[int]:
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result
    

nums = [1, 2, 3, 4]
print(runningSum(nums))