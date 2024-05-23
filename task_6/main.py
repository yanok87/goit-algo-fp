"""Module that uses two approaches — greedy algorithm and dynamic programming algorithm"""


def greedy_algorithm(items, budget):
    """Greedy algorithm that selects dishes, maximizing the ratio of calories to cost without exceeding the specified budget"""
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected_items, total_calories


def dynamic_programming(items, budget):
    """Dynamic programming algorithm, that calculates the optimal set of dishes to maximize calorie content within a given budget"""
    items_list = list(items.values())
    n = len(items_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if items_list[i - 1]["cost"] <= j:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - items_list[i - 1]["cost"]]
                    + items_list[i - 1]["calories"],
                )
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items_list[i - 1]["cost"]
        i -= 1

    return selected_items, dp[n][budget]


# Test the functions with the provided data
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100

print("Greedy Algorithm:")
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Selected items:", selected_items_greedy)
print("Total calories:", total_calories_greedy)

print("\nDynamic Programming Algorithm:")
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Selected items:", selected_items_dp)
print("Total calories:", total_calories_dp)
