#Program to demonstrate insert operation in binary tree
# A utility class that represent an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# A utility function to search a given key in BST
def search(root, key):

    # base cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than roots key
    if root.val < key:
        return search(root.right, key)

    # key is smaller than roots key
    return search(root.left, key)


# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched
def findMin(root):
    current = root

    #loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# function to find the max value in BST
def findMax(root):
    current = root

    #loop down to fint the rightmost leaf
    while(current.right is not None):
        current = current.right

    return current



# Function of deleting
def deleteNode(root, data):
    #Base Case
    if root is None:
        return root
    # if the data is smaller than the roots data then it lies in left subtree
    if data < root.val:
        root.left = deleteNode(root.left, data)
    # if the data is bigger than the roots data then it lies in right subtree
    elif data > root.val:
        root.right = deleteNode(root.right, data)
    # if data is same as roots val then this is our node to be deleted
    else:
        # case 1: no child
        if root.left and root.right is None:
            root = None

        # case 2: node with one child
        elif root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with 2 children:
        # get the inorder successor (smallest in right subtree)
        temp = findMin(root.right)

        # now copy the inorder successor to this node
        root.val = temp.val

        # delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root


#find node function
def find_node(root: Node, data: int) -> Node:
    if root is None: return None
    if root.data == data:
        return root
    elif data < root.data: return find_node(root.left, data)
    else: return find_node(root.right, data)


# function that return node with min value
def find_min(root):
    if root is None: return None
    while root.left:
        root = root.left
    print("found min!", root.data)
    return root


# find successor function
def find_successor(root: Node, data: int):
    current_node = find_node(root, data)
    if current_node is None: return None       # data not found

    if current_node.right:
        # case 1 - there is a right subtree, so get the min of that
        return find_min(current_node.right)

    else:
        #case 2: no right subtree, so we need the closest ancestor
        # where this current node is in the left subtree of that ancestor
        successor = None
        ancestor = root
        while ancestor != current_node: # traverse until we reach the cur node
            if current_node.data < ancestor.data:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

        return successor




# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# function to do preorder tree traversal
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


#function to do postorder tree traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)



# Driver program to test the above functions
# Let us create the following BST
#     50
#   /     \
#  30     70
#  / \   / \
# 20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of the BST
preorder(r)
print("----")
postorder(r)

# Print min value in BST
minValue = findMin(r)
print("The min value in that BST is: ", minValue.val)

# Print max value in BST
maxValue = findMax(r)
print("The max value in that BST is: ", maxValue.val)

# delete a node in BST
print("Before deleting anode")
inorder(r)
print("after deleting a node")
deleteNode(r, 70)
inorder(r)
