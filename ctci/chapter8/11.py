# 8.11: Coins

def change(amount, coins):
    if len(coins) == 1 and amount % coins[0] != 0:
        return 0
    memo = [[0 for j in range(len(coins))] for i in range(amount + 1)]
    coins.sort(reverse = True)
    ans = make_change(amount, coins, 0, memo)
    # print(memo)
    return ans
    
def make_change(amount, coins, index, memo):
    if amount == 0:
        return 1
    if index >= len(coins):
        return 0
    if memo[amount][index] > 0:
        return memo[amount][index]
    curr_coin = coins[index]
    ways, i = 0, 0
    while (i * curr_coin) <= amount:
        amount_rem = amount - (i * curr_coin)
        ways += make_change(amount_rem, coins, index + 1, memo)
        i += 1
        memo[amount][index] = ways
    return ways

amount = 100
coins = [25, 10, 5, 1]
print(change(amount, coins))

