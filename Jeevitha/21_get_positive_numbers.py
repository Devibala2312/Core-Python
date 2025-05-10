nums = [-3, -2, 0, 1, 2, 4, 5, 7]
def yield_positive_num(nums):
    for i in nums:
        if i > 0:
            yield i
print(list(yield_positive_num(nums)))