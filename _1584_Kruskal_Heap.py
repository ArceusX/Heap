# Leetcode 1584: Min Cost to Connect Points (Kruskal's Algo)
# Implement own MinHeap class

# Use heap to get min-weight edge. Use disjoint union set to
# check if that edge joins components not already joined

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # Disjoint union set 
        parent = [x for x in range(n)]
        # Re: root of set holding x and height of path to that root
        # Height lets identify larger set to join other set to
        def find(x: int) -> (int, int):
            height = 1
            while parent[x] != x: # If !points to itself, is !root
                # Point x to its GP to shorten path
                x, parent[x] = parent[x], parent[parent[x]]
                height += 1
            
            return (x, height)
        
        # Heap to sort by distance from every node to every other
        heap = MinHeap()
        for outNode in range(n):
            for inNode in range(outNode + 1, n):
                weight = abs(points[outNode][0] - points[inNode][0]) +\
                         abs(points[outNode][1] - points[inNode][1])
                heap.push((weight, outNode, inNode))
                
        # .. =  1: Self-edge initializes each set with 1 node 
        nInMST  = 1
        sumCost = 0
        
        # To iterate over edges gives no guarantee each
        # iteration adds 1 node to connected component
        while nInMST < n:
            (weight, outNode, inNode) = heap.pop()
            outFind = find(outNode)
            inFind  = find(inNode)

            if (outFind[0] != inFind[0]): # Join sets not joined
                sumCost += weight
                nInMST  += 1
                
                # Root of shorter height to point to longer root
                # To use rank or longest height over any path 
                # would be improved, costlier alternative
                if (outFind[1] > inFind[1]):
                    parent[inFind[0]]  = outFind[0]
                else:
                    parent[outFind[0]] = inFind[0]
                    
        return sumCost

# edge: (0: weight, 1: fromNode, 2: toNode)
class MinHeap:
    def __init__(self, arr = []):
        self.heap = arr[:] # Copy
        for i in range(1, len(self.heap)):
            MinHeap.heapifyUp(self.heap, i)
                
    def push(self, edge) -> None: # Keep heapness
        self.heap.append(edge)
        self.heapifyUp(self.heap, len(self.heap) - 1)
        
    # Ensure heapness up from lone index i of arr, default
    # being arr's final index for call by push()
    @staticmethod
    def heapifyUp(arr, i) -> None:
        if not (0 <= i < len(arr)): return
        
        child = i
        parent = (child - 1) // 2
        
        # Resolve up: Swap to set lower-ordered val as parent 
        # Child's sibling accepts parent swapped lower-ordered val
        while child != 0 and arr[child][0] < arr[parent][0]:
            arr[child], arr[parent] = arr[parent], arr[child]
            child = parent
            parent = (child - 1) // 2
          
    # Algo: Swap vals at [0] and [-1]. In O(1), remove
    #       val now at [-1]. heapifyDown(..) from [0]
    def pop(self) -> (int, int, int):
        if  self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            prevRoot = self.heap.pop()
            self.heapifyDown(self.heap)
            return prevRoot
        
        return None

    # Ensure heapness down from lone index i of arr, default
    # being i = 0 for call by pop(),
    @staticmethod
    def heapifyDown(arr, i = 0) -> None:
        n = len(arr)

        # arr[-1]: As leaf, has no child to swap with
        if not (0 <= i < n - 1): return
        
        parent = i
        child = 2 * parent + 1 # leftChild
        
        # Child's sibling accepts parent swapped lower-ordered val
        while child < n:

            # Set child to lower-val child between left and right
            if (child < n - 1) and arr[child + 1][0] < arr[child][0]:
                child += 1
                
            if arr[child][0] < arr[parent][0]:
                arr[parent], arr[child] = arr[child], arr[parent]

            # If no swap, no longer need to heapifyDown subtree
            else:
                break
                
            parent = child
            child = 2 * parent + 1
      
    # Unused. Set heap[i] = newVal, restore heapness
    def setKey(self, i, newVal) -> None:
        if not (0 <= i < len(self.heap)): return
        
        preVal = self.heap[i][0]
        self.heap[i][0] = newVal
        
        # Push change+ down to leaves
        if newVal > preVal:
            MinHeap.heapifyDown(self.heap, i)
            
        else: # Push change- up to root
            MinHeap.heapifyUp(self.heap, i) 