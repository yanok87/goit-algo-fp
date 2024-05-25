import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation


from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val)
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


def breadth_first_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.val)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    print("result:", result)
    return result


def depth_first_traversal(root):
    if root is None:
        return

    stack = [root]
    result = []

    while stack:
        current_node = stack.pop()
        result.append(current_node.val)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)
    print("result:", result)
    return result


def animate_traversal(traversal, tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = ["#1296F0"] * len(tree.nodes())

    fig, ax = plt.subplots(figsize=(8, 5))

    def update(frame):
        print("frame:", frame)
        if frame < len(colors):
            colors[frame] = "#FF5733"
        else:
            colors[frame - len(colors)] = "#FFFFFF"
        ax.clear()

        nx.draw(
            tree,
            pos=pos,
            with_labels=True,
            arrows=False,
            node_size=2500,
            node_color=colors,
            ax=ax,
        )

    frames = traversal(tree_root)

    ani = animation.FuncAnimation(
        fig, update, frames=frames, interval=1000, repeat=False
    )
    plt.show()


# Example usage:
# Creating the tree
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Performing breadth-first traversal
print("Breadth-First Traversal:")
breadth_first_traversal(root)

# Performing depth-first traversal
print("\nDepth-First Traversal:")
depth_first_traversal(root)


# Animating the breadth-first traversal
# print("Animating Breadth-First Traversal...")
# animate_traversal(breadth_first_traversal, root, "breadth-first")

# Animating the depth-first traversal
print("Animating Depth-First Traversal...")
animate_traversal(depth_first_traversal, root, "depth-first")
