import random
from typing import Literal
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END

class State(BaseModel):
    graph_state: str

class Node:
    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text

    def process(self, state: State):
        print(f"------{self.name}------")
        return {"graph_state": state.graph_state + " " + self.text}

class GraphBuilder:
    def __init__(self):
        self.graph = StateGraph(State)
        self.nodes = {}

    def add_node(self, name: str, text: str):
        node = Node(name, text)
        self.nodes[name] = node
        self.graph.add_node(name, node.process)

    def add_edge(self, start: str, end: str):
        self.graph.add_edge(start, end)

    def add_conditional_edge(self, start: str, condition_func):
        self.graph.add_conditional_edges(start, condition_func)

    def build(self):
        return self.graph.compile()

def decide_mood(state: State) -> Literal["node_4", "node_5"]:
    return "node_4" if random.random() < 0.5 else "node_5"

# # Usage example:
# builder = GraphBuilder()

# # Add nodes
# builder.add_node("node_1", "This")
# builder.add_node("node_2", "is")
# builder.add_node("node_3", "really")
# builder.add_node("node_4", "awesome")
# builder.add_node("node_5", "bad")

# # Add edges
# builder.add_edge(START, "node_1")
# builder.add_edge("node_1", "node_2")
# builder.add_edge("node_2", "node_3")
# builder.add_conditional_edge("node_3", decide_mood)
# builder.add_edge("node_4", END)
# builder.add_edge("node_5", END)

# graph = builder.build()

