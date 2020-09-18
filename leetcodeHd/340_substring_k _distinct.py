# 340. Longest Substring with At Most K Distinct Characters
# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

def lengthOfLongestSubstringKDistinct(s, k):
    d = {}
    maxlen, l = 0, 0
    for r in range(len(s)):
        d[s[r]] = r
        if len(d) > k:
            l = min(d.values())
            d.pop(s[l])
            l += 1
        maxlen = max(maxlen, r - l + 1)
    return maxlen

s = "eceba"
k = 2
print(lengthOfLongestSubstringKDistinct(s, k))
