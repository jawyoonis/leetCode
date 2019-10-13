import Stack as stack 

def kthSmallest(root, k):
    if not root or not k:
        return 



    stack=[]

    while True:
        while root:
            stack.append(root)
            root= root.left 
        root= stack.pop()

        if not k:
            return root.val 
        root= root.right 
print(kthSmallest([3,1,4,None,2],1))
