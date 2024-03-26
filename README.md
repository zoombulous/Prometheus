# Prometheus

Prometheus is a reinforcement learning (RL) agent that implements various RL algorithms, including Q-learning, DQN, Policy Gradient methods, and Actor-Critic. It provides a flexible and efficient framework for training and evaluating RL agents in different environments.

## Purpose

The purpose of Prometheus is to serve as a versatile RL tool that enables users to experiment with different algorithms and environments, allowing for the development and evaluation of efficient RL agents.

## Features

- Implementation of popular RL algorithms: Q-learning, DQN, Policy Gradient methods, and Actor-Critic.
- Support for various Gym environments compatible with RL tasks.
- Flexible training and testing procedures with customizable parameters.
- Automatic comparison with past results and calculation of improvement percentage.
- Error handling and automatic rerun functionality for robust testing.

## Installation

To install Prometheus, clone the repository and ensure you have the required dependencies installed:

```
git clone <repository_url>
cd Prometheus
pip install -r requirements.txt
```

## Usage

1. Import Prometheus in your Python script:

```python
from prometheus import Prometheus
```

2. Create a Prometheus instance and specify the environment, number of episodes, and other parameters for training and testing:

```python
prometheus = Prometheus()
prometheus.train_and_test(environment="CartPole-v1", episodes=100)
```

3. Run the script to train and test the RL agent.

## Example

```python
from prometheus import Prometheus

# Create Prometheus instance
prometheus = Prometheus()

# Train and test RL agent in CartPole environment for 100 episodes
prometheus.train_and_test(environment="CartPole-v1", episodes=100)
```

## Contributing

Contributions to Prometheus are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
