def twoSum(nums, target):
    s1 = set()
    s2 = set()
    for n in nums:
        s1.add(n)
    for x in s1:
        y = target - x
        if y in s1:
            s2.add((min(x, y), max(x, y)))
    return s2

nums = [2,7,11,17,-6,15,1,-8]
target = -4
print(twoSum(nums, target))