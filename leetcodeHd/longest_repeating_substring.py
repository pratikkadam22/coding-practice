# 1062. Longest Repeating Substring

# Given a string s, find out the length of the longest repeating substring(s). Return 0 if no repeating
# substring exists.

# Example 1:
# Input: "abcd"
# Output: 0
# Explanantion: There is no repeating substring

# Example 2:
# Input: "abbaba"
# Output: 2
# Explanantion: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

# Examle 3:
# Input: "aabcaabdaab"
# Output: 3
# Explanation: "aab" occurs three times

# Examle 3:
# Input: "aaaaa"
# Output: 4
# Explanation: "aaaa" occurs twice

def LRS(inputString):
    results = [[0 for j in range(len(inputString))] for i in range(len(inputString))]
    max_len = 0

    for i in range(0, len(inputString)-1):
        for j in range(i+1, len(inputString)):
            if i == 0:
                results[i][j] = 1 if inputString[i] == inputString[j] else 0
            else:
                results[i][j] = results[i-1][j-1] + 1 if inputString[i] == inputString[j] else 0
            max_len = max(max_len, results[i][j])
    return max_len 

print(LRS("abcd"))
print(LRS("abbaba"))
print(LRS("aabcaabdaab"))
print(LRS("aaaaa"))
