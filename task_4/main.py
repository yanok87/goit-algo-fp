import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node


def is_valid_binary_heap(node):
    """
    Checks if a given node is the root of a valid binary heap.

    Args:
        node: The root node of the binary heap to be checked.

    Returns:
        True if the node is the root of a valid binary heap, False otherwise.
    """
    if node is None:
        return True

    # Check if children exist
    left_child = node.left
    right_child = node.right

    # Base case: No children, valid heap
    if not left_child and not right_child:
        return True

    # Check if left child exists and its value is less than or equal to the parent
    if left_child and left_child.val <= node.val:
        # Recursively check left subtree
        return is_valid_binary_heap(left_child)
    else:
        return False

    # If left child is valid, check right child (if it exists)
    if right_child and right_child.val <= node.val:
        # Recursively check right subtree
        return is_valid_binary_heap(right_child)
    else:
        return False


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


def draw_tree(tree_root):
    """
    Draws the tree and checks if it's a valid binary heap before displaying.

    Args:
        tree_root: The root node of the tree to be drawn.
    """
    if not is_valid_binary_heap(tree_root):
        print("Invalid binary heap! Cannot visualize.")
        return

    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [
        node[1]["color"] for node in tree.nodes(data=True)
    ]  # Collect node colors to display

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


# Creating a valid binary heap
root = Node(10)
root.left = Node(5)
root.left.left = Node(4)
root.left.right = Node(1)
root.right = Node(8)
root.right.left = Node(3)
root.right.right = Node(2)

# Displaying the valid binary heap
draw_tree(root)
