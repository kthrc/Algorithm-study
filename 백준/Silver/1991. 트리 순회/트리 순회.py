# --------------------------------------------
# 트리를 위한 클래스, 함수 구현(Node, BinaryTree, insert, preorder, inorder, postorder)
class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.nodes = {}  # 트리 딕셔너리
        self.root = None 

def insert(tree, parent, left, right):
    # parent 
    if parent not in tree:
        tree[parent] = Node(parent)
    # left
    if left != '.':
        if left not in tree:
            tree[left] = Node(left)
        tree[parent].left = tree[left]
    # right
    if right != '.':
        if right not in tree:
            tree[right] = Node(right)
        tree[parent].right = tree[right]

# 전위 순회 preorder (parent - left - right) 
def preorder(node):
    if node:
        print(node.value, end='') # 띄어쓰기 안 하려면 end 있어야 됨
        preorder(node.left)
        preorder(node.right)

# 중위 순회 inorder (left - parent - right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='') # 띄어쓰기 안 하려면 end 있어야 됨
        inorder(node.right)

# 후위 순회 postorder (left - right - parent)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end='') # 띄어쓰기 안 하려면 end 있어야 됨

# --------------------------------------------
# 이진트리 구현 사용
bt = BinaryTree()

# 노드 개수 입력 받기
n_node = int(input())

# 트리 입력
for node in range(n_node):
    parent, left, right = input().split(' ')
    insert(bt.nodes, parent, left, right)

# 문제에서는 루트 노드가 A로 고정됨
bt.root = bt.nodes['A']

# 전위 순회 출력 preorder
preorder(bt.root)
print()
# 중위 순회 출력 inorder
inorder(bt.root)
print()
# 후위 순회 출력 postorder
postorder(bt.root)
