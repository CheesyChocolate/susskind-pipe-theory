# This module holds the classes and functions for pipe maze game

from enum import Enum
import random


class PipeMaze:
    """
    This class holds the pipe maze object
    """

    def __init__(self, pipe_map) -> None:
        self.pipe_map: set = pipe_map
        self.nodes: dict = {}  # key: node_id, value: Node object
        self.input_nodes: list = []
        self.input_water: dict = {}
        self.output_nodes: list = []
        self.expected_output: dict = {}
        # the following keeps track of the output water in output nodes
        # this is updated after the water is passed through the maze
        self.set_nodes()
        self.random_step()  # set the initial water amount in the input nodes

    def print_water_amount(self) -> None:
        for node in self.nodes:
            if self.nodes[node].node_type != NodeTypes.JUNCTION:
                print(f"{node}: {self.nodes[node].current_water_amount}")

    def set_nodes(self) -> None:
        # set the nodes and their neighbors
        for pipe in self.pipe_map:
            if pipe[0] not in self.nodes:
                self.nodes[pipe[0]] = Node()
                self.nodes[pipe[0]].node_id = pipe[0]
                if pipe[0].startswith("Input"):
                    self.nodes[pipe[0]].node_type = NodeTypes.INPUT
                    self.input_nodes.append(pipe[0])
                if pipe[0].startswith("Output"):
                    self.nodes[pipe[0]].node_type = NodeTypes.OUTPUT
                    self.output_nodes.append(pipe[0])
                if pipe[0].startswith("Junction"):
                    self.nodes[pipe[0]].node_type = NodeTypes.JUNCTION
            if pipe[1] not in self.nodes:
                self.nodes[pipe[1]] = Node()
                self.nodes[pipe[1]].node_id = pipe[1]
                if pipe[1].startswith("Input"):
                    self.nodes[pipe[1]].node_type = NodeTypes.INPUT
                    self.input_nodes.append(pipe[1])
                if pipe[1].startswith("Output"):
                    self.nodes[pipe[1]].node_type = NodeTypes.OUTPUT
                    self.output_nodes.append(pipe[1])
                if pipe[1].startswith("Junction"):
                    self.nodes[pipe[1]].node_type = NodeTypes.JUNCTION
            self.nodes[pipe[0]].add_neighbor(self.nodes[pipe[1]])

    def get_nodes_with_water(self) -> list:
        """
        Get the nodes that have water in them
        """
        nodes_with_water = []
        for node in self.nodes:
            if (
                self.nodes[node].current_water_amount != 0
                and self.nodes[node].node_type != NodeTypes.OUTPUT
            ):
                nodes_with_water.append(node)
        return nodes_with_water

    def flow_water(self) -> None:
        """
        Flow water until all the nodes except output nodes have no water.
        """
        self.reset()
        while len(self.get_nodes_with_water()) != 0:
            nodes_with_water = self.get_nodes_with_water()
            for node in nodes_with_water:
                self.nodes[node].pass_water()

    def reset(self) -> None:
        """
        Reset the water amount in the nodes
        """
        for node in self.nodes:
            self.nodes[node].current_water_amount = 0
        for node in self.input_nodes:
            self.nodes[node].current_water_amount = self.input_water[node]

    def calculate_reward(self) -> int:
        """
        technically punishment function. :D

        Calculate the reward based on the difference between the current water
        amount in the output nodes and the desired water amount
        """
        reward = 0
        for output, desired in self.expected_output.items():
            reward -= abs(self.nodes[output].current_water_amount - desired)
            # TODO: Implement a reward calculation that decreases the reward
            # as the difference between the current water amount and the
            # desired water amount increases. in a exponential way. For now,
            # I am using a simple square of the difference.
            # reward -= abs(self.nodes[output].current_water_amount - desired) ** 2
        return reward

    def random_step(self) -> None:
        """
        Randomly select the water amount for the input nodes
        """
        for node in self.input_nodes:
            self.nodes[node].current_water_amount = random.randint(0, 100)
            self.input_water[node] = self.nodes[node].current_water_amount
        self.flow_water()

    def step(self, action) -> None:
        """
        Take a step in the environment
        action: dict, key: node_id, value: water amount to add
        if the action is not valid, the water amount will not be added
        """
        for input_node, water_amount in action.items():
            new_water_amount = self.input_water[input_node] + water_amount
            if new_water_amount > 0 and new_water_amount < 100:
                self.nodes[input_node].current_water_amount = new_water_amount
                self.input_water[input_node] = new_water_amount
        self.flow_water()

    def get_state(self) -> str:
        """
        State is represented as a list of water amounts in input nodes
        Ensure the state is ordered by sorting the keys of input_water
        """
        # return np.array([self.input_water[node] for node in sorted(self.input_nodes)])
        return ",".join([str(self.input_water[node]) for node in sorted(self.input_nodes)])

    # def get_state_space(self) -> tuple:
    # Since the state space is too large, I am not implementing this method
    # instead, the state space will be added to q_table for the states that
    # are not in the q_table
        """
        Get the state space
        state space is a list of all possible states in the environment

        note that a state is represented as a list.

        the number of states is (100/5) ^ number of input nodes
        this is because the water amount in the input nodes can be 0 to 100
        and the water amount can be increased or decreased by 5
        for each input node
        """

    def get_state_space_length(self) -> int:
        return (100 // 5) ** len(self.input_nodes)

    def get_action_space(self) -> tuple:
        """
        Get the action space
        action space is a list of all possible actions in the environment
        an action is increasing or decreasing the water amount in the input
        nodes by 5, this change is represented by 5 and -5 respectively.
        Only one input node can be changed at a time.

        note that an action is represented as a dict.
        """
        action_space: tuple = []
        change = [-5, 5]
        for node in self.input_nodes:
            for c in change:
                action = {}
                action[node] = c
                action_space.append(action)
        return action_space


class NodeTypes(Enum):
    INPUT = 1
    OUTPUT = 2
    JUNCTION = 3


class Node:
    """
    This class holds the node object.
    Input, output and junctions count as Node
    """

    def __init__(self) -> None:
        self.node_id: str = None
        self.node_type: NodeTypes = None  # input, output, junction
        # set of nodes that are connected using pipes # element type in set: Node
        self.neighbors: set = set()
        self.current_water_amount: int = 0

    def add_neighbor(self, neighbor) -> None:
        self.neighbors.add(neighbor)

    def pass_water(self) -> None:
        """
        Pass the water to the neighbors.
        Divide the water equally among the neighbors
        """
        for neighbor in self.neighbors:
            if self.current_water_amount == 0:
                break
            neighbor.current_water_amount += self.current_water_amount // len(
                self.neighbors
            )
        self.current_water_amount = 0
