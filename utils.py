class bstNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


def printTree(node, depth=0):
    if node != None:
        printTree(node.right, depth + 1)
        print(' ' * 4 * depth + '|--' + "({}, {})".format(node.key, node.val))
        printTree(node.left, depth + 1)


