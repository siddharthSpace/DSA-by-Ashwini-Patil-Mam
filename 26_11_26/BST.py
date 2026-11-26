class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def del_node(self, rt, val):
        if rt is None:
            return rt

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left

            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    def get_successor(self, temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    def count(self, rt):
        if rt is None:
            return 0
        return 1 + self.count(rt.left) + self.count(rt.right)

    def countleaf(self, rt):
        if rt is None:
            return 0
        elif rt.left is None and rt.right is None:
            return 1
        else:
            return self.countleaf(rt.left) + self.countleaf(rt.right)

    def countnonleaf(self, rt):
        if rt is None or (rt.left is None and rt.right is None):
            return 0
        return 1 + self.countnonleaf(rt.left) + self.countnonleaf(rt.right)

    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        temp = self.root
        while temp.left is not None:
            temp = temp.left
        print("\nMin:", temp.data)

        temp = self.root
        while temp.right is not None:
            temp = temp.right
        print("Max:", temp.data)

    def level_order(self, rt):
        if rt is None:
            print("BST is Empty")
            return

        arr = []
        cnt = 0
        level = 0
        arr.append(rt)

        while cnt < len(arr):
            node_count = len(arr) - cnt   # No of nodes to be visited
            print("\nLevel : ",level,end=" ")
            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1
                print(temp.data, end=" ")

                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)

            level += 1        


b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("\nInorder:")
b1.inorder(b1.root)

print("\nNo of nodes:", b1.count(b1.root))

print("No of leaf nodes:", b1.countleaf(b1.root))

print("No of non-leaf nodes:", b1.countnonleaf(b1.root))

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

b1.findminmax()

b1.root = b1.del_node(b1.root, 10)

print("\nAfter Deletion:", end=" ")
b1.inorder(b1.root)

print("\nLevel Order Traversal : ", end=" ")
b1.level_order(b1.root)

print("\n")