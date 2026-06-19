from flask import Flask, render_template, jsonify, request
import threading
import time
import json

from grid_env import GridEnvironment
from q_learning_agent import QLearningAgent

app = Flask(__name__)

# ENVIRONMENTS
env_std = GridEnvironment()
env_lag = GridEnvironment()
env_shield = GridEnvironment()

# AGENTS
agent_std = QLearningAgent()
agent_lag = QLearningAgent()
agent_shield = QLearningAgent()

# UI positions
pos_std = [0, 0]
pos_lag = [0, 0]
pos_shield = [0, 0]

training = False


def train():
    global pos_std, pos_lag, pos_shield, training

    training = True

    lambda_penalty = 10  # for Lagrangian

    print("\n===== TRAINING STARTED =====\n")

    # Tracking
    std_hazard_hits = 0
    lag_hazard_hits = 0
    shield_hazard_hits = 0

    std_path = []
    lag_path = []
    shield_path = []

    std_total_reward = 0
    lag_total_reward = 0
    shield_total_reward = 0

    episodes = 200

    for episode in range(episodes):

        state_std = env_std.reset()
        state_lag = env_lag.reset()
        state_shield = env_shield.reset()

        done_std = False
        done_lag = False
        done_shield = False

        while not done_std or not done_lag or not done_shield:

            # -------- STANDARD --------
            if not done_std:
                action_std = agent_std.choose_action(state_std)
                next_state_std, reward_std, cost_std, done_std = env_std.step(action_std)

                agent_std.update(state_std, action_std, reward_std, next_state_std)

                std_total_reward += reward_std
                std_path.append(list(state_std))

                if cost_std == 1:
                    std_hazard_hits += 1

                state_std = next_state_std

            # -------- LAGRANGIAN --------
            if not done_lag:
                action_lag = agent_lag.choose_action(state_lag)
                next_state_lag, reward_lag, cost_lag, done_lag = env_lag.step(action_lag)

                modified_reward = reward_lag - (lambda_penalty * cost_lag)

                agent_lag.update(state_lag, action_lag, modified_reward, next_state_lag)

                lag_total_reward += modified_reward
                lag_path.append(list(state_lag))

                if cost_lag == 1:
                    lag_hazard_hits += 1

                state_lag = next_state_lag

            # -------- SHIELDING --------
            if not done_shield:
                action_shield = agent_shield.choose_action(state_shield)

                next_state, reward, cost, done_temp = env_shield.step(action_shield)

                # 🚫 BLOCK unsafe move
                if cost == 1:
                    safe_found = False
                    for a in range(4):
                        temp_env = GridEnvironment()
                        temp_env.agent_pos = state_shield
                        ns, r, c, d = temp_env.step(a)

                        if c == 0:
                            action_shield = a
                            next_state, reward, cost, done_temp = env_shield.step(action_shield)
                            safe_found = True
                            break

                agent_shield.update(state_shield, action_shield, reward, next_state)

                shield_total_reward += reward
                shield_path.append(list(state_shield))

                if cost == 1:
                    shield_hazard_hits += 1

                state_shield = next_state
                done_shield = done_temp

        agent_std.decay()
        agent_lag.decay()
        agent_shield.decay()

        # LOG
        if (episode + 1) % 10 == 0:
            print(f"\nEpisode {episode+1} Summary:")
            print(f"Standard -> Reward: {std_total_reward}, Hazards: {std_hazard_hits}")
            print(f"Lagrangian -> Reward: {lag_total_reward}, Hazards: {lag_hazard_hits}")
            print(f"Shielding -> Reward: {shield_total_reward}, Hazards: {shield_hazard_hits}")

    print("\n===== TRAINING COMPLETE =====\n")

    # FINAL PRINT
    print("\nFINAL VALUES:")
    print("STANDARD:", std_total_reward, len(std_path), std_hazard_hits)
    print("LAGRANGIAN:", lag_total_reward, len(lag_path), lag_hazard_hits)
    print("SHIELDING:", shield_total_reward, len(shield_path), shield_hazard_hits)

    # -------- VISUAL RUN --------
    state_std = env_std.reset()
    state_lag = env_lag.reset()
    state_shield = env_shield.reset()

    done_std = False
    done_lag = False
    done_shield = False

    while not done_std or not done_lag or not done_shield:

        if not done_std:
            x, y = state_std
            action = int(agent_std.q_table[x, y].argmax())
            next_state, _, _, done_std = env_std.step(action)
            state_std = next_state
            pos_std = [state_std[0], state_std[1]]

        if not done_lag:
            x, y = state_lag
            action = int(agent_lag.q_table[x, y].argmax())
            next_state, _, _, done_lag = env_lag.step(action)
            state_lag = next_state
            pos_lag = [state_lag[0], state_lag[1]]

        if not done_shield:
            x, y = state_shield
            action = int(agent_shield.q_table[x, y].argmax())
            next_state, _, _, done_shield = env_shield.step(action)
            state_shield = next_state
            pos_shield = [state_shield[0], state_shield[1]]

        time.sleep(0.1)

    # -------- SAVE JSON --------
    results = {
        "standard": {
            "total_reward": std_total_reward,
            "steps": len(std_path),
            "hazard_hits": std_hazard_hits,
            "path": std_path
        },
        "lagrangian": {
            "total_reward": lag_total_reward,
            "steps": len(lag_path),
            "hazard_hits": lag_hazard_hits,
            "path": lag_path
        },
        "shielding": {
            "total_reward": shield_total_reward,
            "steps": len(shield_path),
            "hazard_hits": shield_hazard_hits,
            "path": shield_path
        }
    }

    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)


# -------- ROUTES --------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start")
def start():
    thread = threading.Thread(target=train)
    thread.start()
    return "Training started"


@app.route("/position_std")
def position_std():
    return jsonify(pos_std)


@app.route("/position_lag")
def position_lag():
    return jsonify(pos_lag)


@app.route("/position_shield")
def position_shield():
    return jsonify(pos_shield)


@app.route("/set_env", methods=["POST"])
def set_env():
    data = request.json

    for env in [env_std, env_lag, env_shield]:
        env.start = tuple(data["start"])
        env.goal = tuple(data["goal"])
        env.hazards = [tuple(h) for h in data["hazards"]]
        env.obstacles = [tuple(o) for o in data["obstacles"]]

    return "Environment set"


if __name__ == "__main__":
    app.run(debug=True)