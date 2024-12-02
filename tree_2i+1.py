# Tree -- 2i + 1 , 2i + 2

class Tnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create(arr, i, n):
    if i < n:
        temp = Tnode(arr[i])
        root = temp
        root.left = create(arr, 2 * i + 1, n)
        root.right = create(arr, 2 * i + 2, n)
        return root
    return None

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = create(arr, 0, len(arr))

def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value, end=' ')

def pre_order(root):
    if not root:
        return
    print(root.value, end=' ')
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value, end=' ')
    in_order(root.right)

print("Post order:")
post_order(root)

print("\nIn order:")
in_order(root)

print("\nPre order:")
pre_order(root)
