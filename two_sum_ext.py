def twoSum(nums, target):
    s1 = set()
    s2 = set()
    for n in nums:
        x = target - n
        if x in s1:
            s2.add((min(x, n), max(x, n)))
        s1.add(n)
    return s2

nums = [2,7,11,17,-6,15,1,-8]
target = -14
print(twoSum(nums, target))