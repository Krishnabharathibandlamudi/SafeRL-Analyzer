# 🛡️ SafeRL Analyzer

## Comparative Evaluation of Standard, Lagrangian, and Shielding-Based Reinforcement Learning

SafeRL Analyzer is a Safe Reinforcement Learning framework developed to compare different safety-aware learning strategies in autonomous decision-making systems. The project evaluates Standard Q-Learning, Lagrangian Q-Learning, and Shielding-Based Q-Learning in a hazardous grid-world environment and analyzes their performance based on reward optimization, safety compliance, and path efficiency.

---

## 📌 Problem Statement

Traditional Reinforcement Learning algorithms focus on maximizing rewards without considering safety constraints. In real-world applications such as autonomous vehicles, robotics, healthcare systems, and industrial automation, unsafe actions can lead to severe consequences.

This project investigates how different Safe Reinforcement Learning techniques improve decision-making while maintaining high performance and reducing safety violations.

---

## 🎯 Objectives

- Implement Standard Q-Learning as a baseline model.
- Implement Lagrangian Q-Learning using safety penalties.
- Implement Shielding-Based Q-Learning to prevent unsafe actions.
- Compare performance using reward, path efficiency, and hazard metrics.
- Analyze trade-offs between safety and performance.

---

## 🧠 Methodology

### Standard Q-Learning
- Maximizes cumulative rewards.
- Does not consider safety constraints.
- May pass through hazardous regions.

### Lagrangian Q-Learning
- Introduces penalty terms for unsafe actions.
- Learns safer policies through constrained optimization.
- Balances performance and safety.

### Shielding-Based Q-Learning
- Blocks unsafe actions before execution.
- Ensures strict safety compliance.
- Produces the safest navigation strategy.

---

## 🌍 Environment

The framework uses a Grid World Environment where:

- Agent starts at a predefined location.
- Goal state must be reached.
- Hazardous cells represent unsafe regions.
- Rewards and penalties guide learning.
- Safety violations are recorded as hazard hits.

---

## 📊 Performance Comparison

The graph below compares the performance of all three reinforcement learning techniques across Total Reward, Steps Taken, and Hazard Hits.

<p align="center">
  <img src="./images/performance_comparison.png" alt="Performance Comparison" width="800"/>
</p>

### Key Observations

- Shielding-Based Q-Learning achieved the highest safety with zero hazard violations.
- Lagrangian Q-Learning significantly reduced unsafe actions through penalty-based learning.
- Standard Q-Learning achieved faster reward optimization but frequently violated safety constraints.
- Safe Reinforcement Learning techniques improve reliability in safety-critical environments.

---

## 📈 Experimental Results

| Method | Total Reward | Steps Taken | Hazard Hits |
|----------|-------------|-------------|-------------|
| Standard Q-Learning | 1647 | 7698 | 95 |
| Lagrangian Q-Learning | 302 | 8260 | 73 |
| Shielding-Based Q-Learning | 2774 | 6800 | 0 |

---

## 🔍 Comparative Analysis

### Standard Q-Learning
**Advantages**
- Fast learning
- Maximizes rewards efficiently

**Limitations**
- Ignores safety constraints
- High number of hazard violations

### Lagrangian Q-Learning
**Advantages**
- Incorporates safety considerations
- Reduces unsafe actions

**Limitations**
- Lower rewards due to penalties
- Requires tuning of penalty parameters

### Shielding-Based Q-Learning
**Advantages**
- Prevents unsafe actions completely
- Highest safety compliance

**Limitations**
- May take longer paths
- Additional computational overhead

---

## 💻 Technologies Used

- Python
- NumPy
- Flask
- Matplotlib
- Reinforcement Learning
- Q-Learning
- Safe Reinforcement Learning

---

## 📂 Project Structure

```text
SafeRL-Analyzer/
│
├── images/
│   └── performance_comparison.png
│
├── app.py
├── grid_env.py
├── q_learning_agent.py
├── plot_results.py
├── generate_report.py
├── results.json
├── comparison_report.txt
└── README.md
```

---

## 🚀 Applications

- Autonomous Vehicles
- Robotics Navigation
- Healthcare Decision Systems
- Industrial Automation
- Smart Manufacturing
- AI Safety Research
- Intelligent Control Systems

---

## 🔮 Future Enhancements

- Deep Q-Networks (DQN)
- Proximal Policy Optimization (PPO)
- Constrained Policy Optimization (CPO)
- Dynamic Safety Shields
- Multi-Agent Reinforcement Learning
- Real-World Robotic Deployment
- Advanced Safety Benchmarking

---

## 📚 Conclusion

SafeRL Analyzer demonstrates the importance of integrating safety mechanisms into Reinforcement Learning systems. Through a comparative evaluation of Standard, Lagrangian, and Shielding-Based Q-Learning approaches, the framework highlights how safety-aware learning techniques can significantly reduce risk while maintaining effective decision-making performance.

---

## 👨‍💻 Author

Krishna Bharathi Bandlamudi

---

## 🏷️ Keywords

Safe Reinforcement Learning, Q-Learning, AI Safety, Lagrangian Optimization, Shielding, Machine Learning, Autonomous Systems, Robotics, Intelligent Agents, Decision Making
