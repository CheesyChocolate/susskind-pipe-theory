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
        self.set_nodes()
        self.random_step()

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
                if pipe[0].startswith("Output"):
                    self.nodes[pipe[0]].node_type = NodeTypes.OUTPUT
                if pipe[0].startswith("Junction"):
                    self.nodes[pipe[0]].node_type = NodeTypes.JUNCTION
            if pipe[1] not in self.nodes:
                self.nodes[pipe[1]] = Node()
                self.nodes[pipe[1]].node_id = pipe[1]
                if pipe[1].startswith("Input"):
                    self.nodes[pipe[1]].node_type = NodeTypes.INPUT
                if pipe[1].startswith("Output"):
                    self.nodes[pipe[1]].node_type = NodeTypes.OUTPUT
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
        self.random_step()

    def calculate_reward(self, desired_output) -> int:
        """
        technically punishment function. :D

        Calculate the reward based on the difference between the current water
        amount in the output nodes and the desired water amount
        """
        reward = 0
        for output, desired in desired_output.items():
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
        for node in self.nodes:
            if self.nodes[node].node_type == NodeTypes.INPUT:
                self.nodes[node].current_water_amount = random.randint(0, 20)
        # TODO: for testing purpose. Remove this hardcoded values
        self.nodes["Input1"].current_water_amount = 10
        self.nodes["Input2"].current_water_amount = 20
        self.nodes["Input3"].current_water_amount = 30
        # TODO: for testing purpose. Remove this hardcoded values


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


pipe_map: set = {
    ("Input1", "Junction1"),
    ("Input1", "Junction2"),
    ("Input2", "Junction3"),
    ("Input2", "Junction4"),
    ("Junction1", "Junction5"),
    ("Junction2", "Junction5"),
    ("Junction3", "Junction5"),
    ("Junction4", "Junction5"),
    ("Junction5", "Output1"),
    ("Junction5", "Output2"),
    ("Junction5", "Output3"),
    ("Junction5", "Output4"),
}
"""
Input1 -> Junction1 -> Junction5 -> Output1
       -> Junction2 -> Junction5 -> Output2

Input2 -> Junction3 -> Junction5 -> Output3
       -> Junction4 -> Junction5 -> Output4
"""

input_water: dict = {
    "Input1": 10,
    "Input2": 20,
    "Input3": 30,
}

pipe_map: set = {
    ("Input1", "Junction1"), ("Input1", "Junction2"), ("Input1", "Junction3"),
    ("Input2", "Junction3"), ("Input2", "Junction4"), ("Input2", "Junction5"),
    ("Input3", "Junction5"), ("Input3", "Junction6"), ("Input3", "Junction7"),
    ("Junction1", "Junction8"),
    ("Junction2", "Junction8"),
    ("Junction3", "Junction8"),
    ("Junction4", "Junction9"),
    ("Junction5", "Junction9"),
    ("Junction6", "Junction9"),
    ("Junction7", "Junction10"),
    ("Junction8", "Output1"),
    ("Junction9", "Output2"),
    ("Junction10", "Output3"),
    ("Junction11", "Output4"),
}


pm: PipeMaze = PipeMaze(pipe_map)
pm.print_water_amount()
pm.flow_water()
print("========================")
pm.print_water_amount()

expected_output = {
    "Output1": 15,
    "Output2": 30,
    "Output3": 10,
    "Output4": 0,
}
print(pm.calculate_reward(expected_output))
