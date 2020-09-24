# 8.8: Permutations with Dups

def print_perms(input):
    results = []
    freq_map = {}
    for i in input:
        freq_map[i] = freq_map.get(i, 0) + 1
    helper("", len(input), freq_map, results)
    return results

def helper(prefix, remaining, freq_map, results):
    if remaining == 0:
        results.append(prefix)
        return
    for c in freq_map:
        count = freq_map[c]
        if count > 0:
            freq_map[c] = count - 1
            helper(prefix + c, remaining - 1, freq_map, results)
            freq_map[c] = count

s = "abc"
ans = print_perms(s)
print(ans)
