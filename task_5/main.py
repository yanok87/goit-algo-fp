import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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


def depth_first_traversal(node):
    if node is not None:
        yield node
        yield from depth_first_traversal(node.left)
        yield from depth_first_traversal(node.right)


def breadth_first_traversal(node):
    if node is None:
        return
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        yield current_node
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def animate_traversal(traversal, tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = ["#1296F0"] * len(tree.nodes())

    fig, ax = plt.subplots(figsize=(8, 5))

    def update(frame):
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

    ani = animation.FuncAnimation(
        fig, update, frames=len(tree.nodes()) * 2, interval=1000
    )
    plt.show()


# Creating the tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Depth-first traversal
# traversal = depth_first_traversal(root)

# Breadth-first traversal
traversal = breadth_first_traversal(root)

# Animating the traversal
animate_traversal(traversal, root)
