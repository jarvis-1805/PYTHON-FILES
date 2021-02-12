'''
Construct Tree Using Inorder and Preorder

For a given preorder and inorder traversal of a Binary Tree of type integer stored in an array/list, create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

Note:
Assume that the Binary Tree contains only unique elements. 

Input Format:
The first line of input contains an integer N denoting the size of the list/array. It can also be said that N is the total number of nodes the binary tree would have.

The second line of input contains N integers, all separated by a single space. It represents the preorder-traversal of the binary tree.

The third line of input contains N integers, all separated by a single space. It represents the inorder-traversal of the binary tree.

Output Format:
The given input tree will be printed in a level order fashion where each level will be printed on a new line. 
Elements on every level will be printed in a linear fashion. A single space will separate them.

Constraints:
1 <= N <= 10^4
Where N is the total number of nodes in the binary tree.

Time Limit: 1 sec

Sample Input 1:
7
1 2 4 5 3 6 7 
4 2 5 1 6 3 7 

Sample Output 1:
1 
2 3 
4 5 6 7 

Sample Input 2:
6
5 6 2 3 9 10 
2 6 3 9 5 10 

Sample Output 2:
5 
6 10 
2 3 
9
'''

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTreeFromPreIn(pre, inorder) :
	#Your code goes here
    if len(pre) == 0:
        return None
    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndexInorder = i
            break
    if rootIndexInorder == -1:
        return None
    leftInorder = inorder[0:rootIndexInorder]
    rightInorder = inorder[rootIndexInorder +1:]

    lenLeftSubtree = len(leftInorder)

    leftPreorder = pre[1:lenLeftSubtree + 1]
    rightPreorder = pre[lenLeftSubtree + 1:]

    leftChild = buildTreeFromPreIn(leftPreorder, leftInorder)
    rightChild = buildTreeFromPreIn(rightPreorder, rightInorder)

    root.left = leftChild
    root.right = rightChild
    return root

'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildTreeFromPreIn(preOrder, inOrder)
printLevelWise(root)