import operator

class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child

    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child

    def insert_left(root, child_val):
        subtree = root.pop(1)
        if(len(subtree) > 1):
            root.insert(1, [child_val, subtree, []])
        else:
            root.insert(1, [child_val, [], []])
        return root

    def insert_right(root, child_val):
        subtree = root.pop(2)
        if len(subtree) > 1:
            root.insert(2, [child_val, [], subtree])
        else:
            root.insert(2, [child_val, [], []])
        return root

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left(root, child_val):
    subtree = root.pop(1)
    if(len(subtree) > 1):
        root.insert(1, [child_val, subtree, []])
    else:
        root.insert(1, [child_val, [], []])
    return root

def insert_right(root, child_val):
    subtree = root.pop(2)
    if len(subtree) > 1:
        root.insert(2, [child_val, [], subtree])
    else:
        root.insert(2, [child_val, [], []])
    return root

def build_parse_tree(expression):
    tree = {}
    stack = [tree]
    node = tree
    for token in expression:
        if(token in OPERATORS):
            node["val"] = token
            node["right"] = {}
            stack.append(node)
            node = ["right"]
        else:
            node["val"] = int(token)
            parent = stack.pop()
            node = parent
    return tree

def evaluate(tree):
    try:
        operate = OPERATORS[tree["val"]]
        return operate(evaluate(tree["left"]), evaluate(tree["right"]))
    except KeyError:
        return tree["val"]

math = "2+3*2-2/2"

tree = build_parse_tree(math)
print(tree)
result = evaluate(tree)
print(result)
'''
root = [3, [], []]
insert_left(root, 4)
insert_left(root, 5)
insert_right(root, 6)
insert_right(root, 7)

left = get_left_child(root)
print(left)
set_root_val(left, 9)
print(left)
insert_left(left, 11)
print(left)

print(get_right_child(get_right_child(root)))
'''