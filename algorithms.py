# algorithms.py

# Define parameters for popular reinforcement learning algorithms
algorithms_params = {
    "Q-learning": {"learning_rate": 0.1, "discount_factor": 0.99},
    "DQN": {"learning_rate": 0.001, "discount_factor": 0.95},
    "Policy Gradient": {"learning_rate": 0.01, "discount_factor": 0.99},
    "Actor-Critic": {"learning_rate_actor": 0.001, "learning_rate_critic": 0.002, "discount_factor": 0.98}
}

# List of popular reinforcement learning algorithms
popular_algorithms = ["Q-learning", "DQN", "Policy Gradient", "Actor-Critic"]
