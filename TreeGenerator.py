import tkinter
import random

from queue import Queue


class TreeGenerator:

    def __init__(self):
        self.root = tkinter.Tk(screenName="Tree Generator")
        self.is_fullscreen = True
        self.root.attributes("-fullscreen", self.is_fullscreen)
        self.WIDTH = self.root.winfo_screenwidth()
        self.HEIGHT = self.root.winfo_screenheight()
        config = {'width': self.WIDTH, 'height': self.HEIGHT}
        self.canvas = tkinter.Canvas(self.root, config)
        self.canvas.pack()
        self.root.bind("<Escape>", self.__toggle_fullscreen)
        self.tree = None

    def create_tree_middle_top(self, weight):
        self.tree = Tree(weight, self.WIDTH / 2, 0)

    def generate(self):
        current_node = self.tree.current_node
        self.tree.add_node(Node(current_node.CHILD_LIMIT, current_node.x+10, current_node.y+10))
        self.tree.add_node(Node(current_node.CHILD_LIMIT, current_node.x-10, current_node.y+10))
        self.draw()

    def draw(self):
        queue = Queue()

        queue.put(self.tree.root)

        delay = 500
        while queue.qsize() != 0:

            node = queue.get()

            for child in node.children:
                self.canvas.after(delay, self.canvas.create_line, node.x, node.y, child.x, child.y, {'width': 2})
                delay += 500

    def __toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)
        return "break"


class Tree:

    def __init__(self, child_limit, x, y):
        self.root = Node(child_limit, x, y)
        self.current_node = self.root
        self.root.CHILD_LIMIT = child_limit

    def add_node(self, node):
        if not len(self.current_node.children) < self.current_node.CHILD_LIMIT:
            self.current_node = node
        self.current_node.add_child(node)


class Node:

    def __init__(self, child_limit, x, y):
        self.children = []
        self.CHILD_LIMIT = child_limit
        self.x = x
        self.y = y

    def get_num_children(self):
        return len(self.children)

    def add_child(self, node):
        self.children.append(node)

    def remove_child_node(self, node):
        self.children.remove(node)

    def remove_child_index(self, index):
        self.children.remove(self.children[index])


if __name__ == '__main__':
    form = TreeGenerator()
    form.create_tree_middle_top(3)
    form.generate()
    form.root.mainloop()
