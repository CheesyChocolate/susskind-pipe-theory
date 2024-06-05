# This module holds the classes and functions for Q-learning algorithm

import numpy as np

from pipe_maze import PipeMaze


class QLearningAgent:
    def __init__(self,
                 env: PipeMaze,
                 alpha: float = 0.1,
                 gamma: float = 0.9,
                 epsilon: float = 0.1) -> None:
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
            (self.env.get_state_space_length(), len(self.env.get_action_space()) + 1)
        )

        def update_q_table(self,
                           state: tuple,
                           action: dict,
                           reward: int,
                           next_state) -> None:
            """
               Update the q_table using the Q-learning algorithm

               If the state or next_state is not in the q_table, add them to the
               q_table
               """
            pass
