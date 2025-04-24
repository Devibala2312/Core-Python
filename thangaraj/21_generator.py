nums = [-3, -2, 0, 1, 2, 4, 5, 7]

def getPositiveNumbers(nums):
    max = len(nums)
    for i in range(max):
        if nums[i] > 0:
            yield nums[i]

print(list(getPositiveNumbers(nums)))

