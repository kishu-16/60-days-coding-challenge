def runningSum(nums):
    result = []
    current_sum = 0

    for num in nums:
        current_sum += num
        result.append(current_sum)

    return result


nums = [1,2,3,4,5]
print(runningSum(nums))
