"""Module that simulates a large number of dice throws"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_dice_throw(num_simulations):
    """Simulates throwing two dice a specified number of times"""
    results = np.random.randint(1, 7, size=(num_simulations, 2))
    sums = np.sum(results, axis=1)
    return sums


def calculate_probabilities(sums):
    """Calculates the probability of each possible sum of two dice"""
    probabilities = {}
    total_simulations = len(sums)

    for i in range(2, 13):
        count = np.sum(sums == i)
        probability = count / total_simulations
        probabilities[i] = probability

    return probabilities


def display_probabilities(probabilities):
    """Displays the probabilities of each possible sum of two dice in a tabular format"""
    print("Sum\tProbability")
    for i in range(2, 13):
        probability_percent = probabilities[i] * 100
        probability_fraction = (
            f"{probability_percent:.2f}% ({int(probabilities[i] * 36)}/36)"
        )
        print(f"{i}\t{probability_fraction}")


# Simulation settings
num_simulations = 1000000

# Perform simulation
sums = simulate_dice_throw(num_simulations)

# Calculate probabilities
probabilities = calculate_probabilities(sums)

# Display probabilities
display_probabilities(probabilities)

# Plotting the results
plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability")
plt.title("Probabilities of Sum of Two Dice")
plt.xticks(range(2, 13))
plt.grid(axis="y")
plt.show()
