from module.pipe_maze import PipeMaze
from module.q_learning import QLearningAgent


def main():
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
    expected_output = {
        "Output1": 15,
        "Output2": 30,
        "Output3": 10,
        "Output4": 0,
    }
    pm.expected_output = expected_output

    q_learning_agent: QLearningAgent = QLearningAgent(pm)
    q_learning_agent.train()

    pm.reset()
    print("initial input water:")
    pm.print_water_amount()
    print("====================================")
    print("initial output water:")
    pm.flow_water()
    pm.print_water_amount()
    pm.reset()
    print("====================================")
    q_learning_agent.run()
    print("input water after q-learning:")
    print(q_learning_agent.input_after_q_learning)
    print("====================================")
    print("output water after q-learning:")
    pm.print_water_amount()
    print("====================================")
    print(f"expected_output: {expected_output}")
    print("====================================")
    print(f"reward: {pm.calculate_reward()}")
    print("====================================")



if __name__ == "__main__":
    main()
