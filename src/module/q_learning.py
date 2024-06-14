# This module holds the classes and functions for Q-learning algorithm

import numpy as np
import random

from .pipe_maze import PipeMaze


class QLearningAgent:
    def __init__(
        self,
        env: PipeMaze,
        alpha: float = 0.1,
        gamma: float = 0.9,
        epsilon: float = 0.1,
    ) -> None:
        self.env: PipeMaze = env
        self.alpha: float = alpha
        self.gamma: float = gamma
        self.epsilon: float = epsilon
        """
        two dimensional array, first dimension is the state space and the
        second dimension is the action space

        |   Q           | Input1 + 5 | Input1 - 5 | Input2 + 5 | Input2 - 5   |
        |---------------|------------|------------|------------|--------------|
        | 10, 20, 30  | 0          | 0          | 0          | 0            |
        | 15, 20, 30  | 0          | 0          | 0          | 0            |
        | 10, 25, 30  | 0          | 0          | 0          | 0            |
        | 10, 20, 35  | 0          | 0          | 0          | 0            |

        |   Q  |   a1 |  a2 |  a3 |  a4 |
        |------|------|-----|-----|-----|
        [
         [  [10, 20, 30]    [0]   [0]   [0]   [0]  ]
         [  [15, 20, 30]    [0]   [0]   [0]   [0]  ]
         [  [10, 25, 30]    [0]   [0]   [0]   [0]  ]
         [  [10, 20, 35]    [0]   [0]   [0]   [0]  ]
        ]

        |   Q  | a1 | a2 | a3 | a4 |
        |------|----|----|----|----|
        | S1   | 0  | 0  | 0  | 0  |
        | S2   | 0  | 0  | 0  | 0  |
        | S3   | 0  | 0  | 0  | 0  |
        | S4   | 0  | 0  | 0  | 0  |
        """
        self.q_table: np.array = np.zeros(
            (self.env.get_state_space_length(),
             len(self.env.get_action_space())), dtype=object
        )
        self.index_of_state_in_q_table: list = []

        # TODO: Test
        # self.q_table[0][0] = '10,11,12'
        # self.q_table[7999][0] = '11,12,13'
        # print(self.env.get_action_space())
        # action = {
        #     "Input1": -5,
        # }
        # print(self.env.get_action_space().index(action))

        # state = '10,20,30'
        # action = {
        #     "Input1": 5,
        # }
        # reward = 10
        # next_state = '15,20,30'
        # print(self.q_table)
        # self.update_q_table(state, action, reward, next_state)
        # print(self.q_table)
        # print(self.get_q_value(state, action))
        # print(self.get_best_action(state))
        self.train(18000)
        print(self.q_table)
        # TODO: Test

    def update_q_table(
        self, state: str, action: dict, reward: int, next_state: str
    ) -> None:
        """
        Update the q_table using the Q-learning algorithm

        If the state or next_state is not in the q_table, add them to the
        q_table
        """
        if state not in self.index_of_state_in_q_table:
            self.index_of_state_in_q_table.append(state)
        if next_state not in self.index_of_state_in_q_table:
            self.index_of_state_in_q_table.append(next_state)

        state_index = self.index_of_state_in_q_table.index(state)
        next_state_index = self.index_of_state_in_q_table.index(next_state)

        action_index = self.env.get_action_space().index(action)
        current_q_value = self.q_table[state_index][action_index]
        next_max_q_value = np.max(self.q_table[next_state_index])
        new_q_value = current_q_value + self.alpha * (
            reward + self.gamma * next_max_q_value - current_q_value
        )
        self.q_table[state_index][action_index] = new_q_value

    def get_q_value(self, state: str, action: dict) -> float:
        """
        Get the q_value for the given state and action
        """
        if state not in self.index_of_state_in_q_table:
            return 0
        state_index = self.index_of_state_in_q_table.index(state)
        action_index = self.env.get_action_space().index(action)
        return self.q_table[state_index][action_index]

    def get_best_action(self, state: str) -> dict:
        """
        Get the best action for the given state
        """
        if state not in self.index_of_state_in_q_table:
            return random.choice(self.env.get_action_space())
        state_index = self.index_of_state_in_q_table.index(state)
        action_index = np.argmax(self.q_table[state_index])
        return self.env.get_action_space()[action_index]

    def train(self, episodes: int = 5000) -> None:
        """
        Train the agent using the Q-learning algorithm
        """
        for _ in range(episodes):
            self.env.reset()
            state = self.env.get_state()
            for _ in range(20):  # episode ends after 20 steps
                if np.random.uniform(0, 1) < self.epsilon:
                    action = random.choice(self.env.get_action_space())
                else:
                    action = self.get_best_action(state)
                self.env.step(action)
                next_state = self.env.get_state()
                reward = self.env.calculate_reward()
                self.update_q_table(state, action, reward, next_state)
                state = next_state

    def get_solution_policy(self) -> dict:
        """
        Get the solution policy
        """
        policy = {}
        for state in self.index_of_state_in_q_table:
            action = self.get_best_action(state)
            policy[state] = action
        return policy

    def run(self) -> None:
        """
        Run the agent to find the optimal policy
        """
        self.env.reset()
        start_state = self.env.get_state()
        for _ in range(20000):
            action = self.get_best_action(start_state)
            self.env.step(action)
            next_state = self.env.get_state()
            reward = self.env.calculate_reward()
            self.update_q_table(start_state, action, reward, next_state)
            start_state = next_state
            if reward > -10:
                break
