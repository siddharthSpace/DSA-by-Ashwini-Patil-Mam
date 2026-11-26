class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        curr = self.root
        while True:
            if new_node.data < curr.data:
                if curr.left is None:
                    curr.left = new_node
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    break
                curr = curr.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return
        
        arr = [rt]
        cnt = 0
        while cnt < len(arr):
            temp = arr[cnt]
            cnt += 1
            print(temp.data, end=" ")
            if temp.left:
                arr.append(temp.left)
            if temp.right:
                arr.append(temp.right)


b1 = BST()
for val in [100, 10, 450, 4, 65, 300, 500]:
    b1.insert(Node(val))

print("Inorder:")
b1.inorder(b1.root)      

print("\nLevel Order:")
b1.level_order(b1.root)   