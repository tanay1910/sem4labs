class Node:
    def __init__(self, data):
        self.data  = data
        self.left= None
        self.right = None


def createBST(root,num):
        if root==None:
            root=Node(num)
        else:
            if num > root.data:
                root.right=createBST(root.right,num)
            elif num< root.data:
                root.left=createBST(root.left,num)

        
        return root
    
def inorder(root):
     if root:
          inorder(root.left)
          print(root.data)
          inorder(root.right)

root = None
root = Node(5)
createBST(root,5)
createBST(root,3)
createBST(root,7)
createBST(root,2)
createBST(root,4)
createBST(root,6)
createBST(root,8)
inorder(root)