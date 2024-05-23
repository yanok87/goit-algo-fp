import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time
import random


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)  # Saving a node color in a graph
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2**layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2**layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, traversal):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    plt.figure(figsize=(8, 5))

    # Draw initial tree with random colors
    node_colors = [tree.nodes[node]["color"] for node in tree.nodes()]
    nx.draw(
        tree,
        pos=pos,
        with_labels=True,
        arrows=False,
        node_size=2500,
        node_color=node_colors,
    )
    plt.show()

    # Traverse the tree, updating node colors for each step
    for step, (node, color) in enumerate(traversal, start=1):
        tree.nodes[node.val]["color"] = color
        node_colors = [tree.nodes[node]["color"] for node in tree.nodes()]
        plt.figure(figsize=(8, 5))
        nx.draw(
            tree,
            pos=pos,
            with_labels=True,
            arrows=False,
            node_size=2500,
            node_color=node_colors,
        )
        plt.title(f"Step {step}")
        plt.show()
        time.sleep(1)


def in_order_traversal(root):
    traversal = []

    def _in_order_traversal(node):
        if node:
            _in_order_traversal(node.left)
            node.color = generate_color()
            traversal.append((node, node.color))
            _in_order_traversal(node.right)

    _in_order_traversal(root)
    return traversal


def pre_order_traversal(root):
    traversal = []

    def _pre_order_traversal(node):
        if node:
            node.color = generate_color()
            traversal.append((node, node.color))
            _pre_order_traversal(node.left)
            _pre_order_traversal(node.right)

    _pre_order_traversal(root)
    return traversal


def post_order_traversal(root):
    traversal = []

    def _post_order_traversal(node):
        if node:
            _post_order_traversal(node.left)
            _post_order_traversal(node.right)
            node.color = generate_color()
            traversal.append((node, node.color))

    _post_order_traversal(root)
    return traversal


def breadth_first_traversal(root):
    traversal = []
    if root is None:
        return traversal
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        node.color = generate_color()
        traversal.append((node, node.color))
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return traversal


def generate_color():
    """Generate random RGB color code"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02X}{:02X}{:02X}".format(r, g, b)


# Creating the tree
root = Node(0, color=generate_color())
root.left = Node(4, color=generate_color())
root.left.left = Node(5, color=generate_color())
root.left.right = Node(10, color=generate_color())
root.right = Node(1, color=generate_color())
root.right.left = Node(3, color=generate_color())

# Perform different traversals
in_order_traversal_result = in_order_traversal(root)
pre_order_traversal_result = pre_order_traversal(root)
post_order_traversal_result = post_order_traversal(root)
breadth_first_traversal_result = breadth_first_traversal(root)

# Displaying the tree with different traversals
print("In-order traversal:")
draw_tree(root, in_order_traversal_result)

print("Pre-order traversal:")
draw_tree(root, pre_order_traversal_result)

print("Post-order traversal:")
draw_tree(root, post_order_traversal_result)

print("Breadth-first traversal:")
draw_tree(root, breadth_first_traversal_result)
