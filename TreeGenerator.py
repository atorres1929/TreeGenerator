import tkinter
import random
from queue import Queue


class TreeGenerator:

    def __init__(self, tree):
        self.root = tkinter.Tk(screenName="Tree Generator")
        self.is_fullscreen = True
        self.root.attributes("-fullscreen", self.is_fullscreen)
        self.WIDTH = self.root.winfo_screenwidth()
        self.HEIGHT = self.root.winfo_screenheight()
        config = {'width': self.WIDTH, 'height': self.HEIGHT}
        self.canvas = tkinter.Canvas(self.root, config)
        self.canvas.pack()
        self.root.bind("<Escape>", self.toggle_fullscreen)
        self.tree = tree

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)
        return "break"

    def generate(self):
        self.tree.add_node(Node(self.tree.weight))
        self.draw()

    def draw(self):
        queue = Queue()

        queue.put(self.tree.root)

        mid_width = self.WIDTH/2

        while queue.qsize() != 0:

            node = queue.get()

            for child in node.children:
                self.canvas.create_line(mid_width, 0, mid_width+10, 10, width=2)


class Tree:

    def __init__(self, weight):
        self.root = Node(weight)
        self.current_node = self.root
        self.weight = weight
        self.root.CHILD_LIMIT = random.randint(1, self.weight)

    def add_node(self, node):
        if not len(self.current_node.children) < self.weight:
            self.current_node = node
        self.current_node.add_child(node)
        self.current_node = node


class Node:
    CHILD_LIMIT = 0

    def __init__(self, length):
        self.children = []
        self.length = length * random.randint(1, length)

    def get_num_children(self):
        return len(self.children)

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)

    def remove_child(self, index):
        self.children.remove(self.children[index])


if __name__ == '__main__':
    form = TreeGenerator(Tree(1))
    form.generate()
    form.root.mainloop()
