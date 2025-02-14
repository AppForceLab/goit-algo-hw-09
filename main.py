import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result


def compare_algorithms(amount):
    start = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start
    
    start = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start
    
    return {
        "greedy": (greedy_result, greedy_time),
        "dp": (dp_result, dp_time)
    }


if __name__ == "__main__":
    test_amount = 113
    comparison = compare_algorithms(test_amount)
    print("Greedy Algorithm Result:", comparison["greedy"][0], "Time:", comparison["greedy"][1])
    print("DP Algorithm Result:", comparison["dp"][0], "Time:", comparison["dp"][1])