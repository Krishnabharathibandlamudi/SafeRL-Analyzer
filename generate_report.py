import json

# Load results
with open("results.json", "r") as f:
    data = json.load(f)

std = data["standard"]
lag = data["lagrangian"]
shield = data["shielding"]

# Generate report
report = f"""
================ RL COMPARISON REPORT ================

STANDARD Q-LEARNING
-------------------
Total Reward: {std['total_reward']}
Steps Taken: {std['steps']}
Hazard Hits: {std['hazard_hits']}

Behavior:
- Chooses shortest path
- Ignores safety
- May pass through hazardous cells


LAGRANGIAN Q-LEARNING
---------------------
Total Reward: {lag['total_reward']}
Steps Taken: {lag['steps']}
Hazard Hits: {lag['hazard_hits']}

Behavior:
- Penalizes unsafe actions
- Avoids hazardous cells
- Takes safer route


SHIELDING-BASED Q-LEARNING
--------------------------
Total Reward: {shield['total_reward']}
Steps Taken: {shield['steps']}
Hazard Hits: {shield['hazard_hits']}

Behavior:
- Blocks unsafe actions before execution
- Avoids hazardous cells almost completely
- Ensures highest safety
- May take longer path


FINAL ANALYSIS
--------------
Standard   : Fastest but unsafe
Lagrangian : Balanced safety and performance
Shielding  : Safest but slowest

=====================================================
"""

# Save report
with open("comparison_report.txt", "w") as f:
    f.write(report)

print("✅ Comparison report generated successfully!")