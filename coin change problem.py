def min_coins_for_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1

coin_denominations = [1, 2, 5]
target_amount = 11
result = min_coins_for_change(coin_denominations, target_amount)

print(f"Minimum coins needed for {target_amount}: {result}")
