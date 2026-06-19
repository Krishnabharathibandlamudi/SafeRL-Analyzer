import json
import matplotlib.pyplot as plt

# Load results
with open("results.json", "r") as f:
    data = json.load(f)

# Labels
labels = ["Total Reward", "Steps", "Hazard Hits"]
x = range(len(labels))

# Extract data
standard = [
    data["standard"]["total_reward"],
    data["standard"]["steps"],
    data["standard"]["hazard_hits"]
]

lagrangian = [
    data["lagrangian"]["total_reward"],
    data["lagrangian"]["steps"],
    data["lagrangian"]["hazard_hits"]
]

shielding = [
    data["shielding"]["total_reward"],
    data["shielding"]["steps"],
    data["shielding"]["hazard_hits"]
]

# Plot
plt.figure()

plt.plot(x, standard, marker='o', label="Standard Q-Learning")
plt.plot(x, lagrangian, marker='o', label="Lagrangian Q-Learning")
plt.plot(x, shielding, marker='o', label="Shielding Method")

plt.xticks(x, labels)
plt.title("Performance Comparison (All Methods)")
plt.xlabel("Metrics")
plt.ylabel("Values")
plt.legend()

plt.show()