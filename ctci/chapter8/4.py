# 8.4: Power Set

def get_subsets(nums, index):
    if len(nums) == index:
        allSubsets = []
        allSubsets.append([])
    else:
        allSubsets = get_subsets(nums, index + 1)
        item = nums[index]
        moreSubsets = []
        for subset in allSubsets:
            newSubset = []
            newSubset.append(item)
            newSubset.extend(subset)
            moreSubsets.append(newSubset)
        allSubsets.extend(moreSubsets)
    return allSubsets

nums = [1, 2, 3]
print(get_subsets(nums, 0))