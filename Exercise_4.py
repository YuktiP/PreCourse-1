# Python program to insert element in binary tree  
class newNode():  
  
    def __init__(self, data):  
        self.key = data 
        self.left = None
        self.right = None
          
""" Inorder traversal of a binary tree"""
def inorder(temp): 
    if temp:
        inorder(temp.left)
        print(temp.key, end = " ")
        inorder(temp.right)
    
  
  
"""function to insert element in binary tree """
def insert(temp,key): 
    if temp:
        tree = []
        tree.append(temp)
        while(len(tree)):
            node = tree.pop(0)
            if not node.left:
                node.left = newNode(key)
                break
            else:
                tree.append(node.left)

            if not node.right:
                node.right = newNode(key)
                break
            else:
                tree.append(node.right)
    else:
        temp = newNode(key)
        return
       
# Driver code  
if __name__ == '__main__': 
    root = newNode(10)  
    root.left = newNode(11)  
    root.left.left = newNode(7)  
    root.right = newNode(9)  
    root.right.left = newNode(15)  
    root.right.right = newNode(8)  
  
    print("Inorder traversal before insertion:", end = " ") 
    inorder(root)  
  
    key = 12
    insert(root, key)  
  
    print()  
    print("Inorder traversal after insertion:", end = " ") 
    inorder(root) 
