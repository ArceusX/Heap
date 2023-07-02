# 1584 Min Cost to Connect All Points (Prim's Algo)

# Into initially-empty connected component (CC), Prim adds
# each node via lighest edge to unadded node from any node 
# already in CC (that edge's weight as unadded node's cost)

# Track each edge in heap. Get lighest edge from heap,
# then check if that edge connects to unadded node
# Complex.: O(nEdges * ln(nNodes))

# Implement own MinHeap: See Prim 1 of _1584_Prim
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        isAdded = [False] * n
        
        sumCost = 0
        nInMST = 0

        # Store [0: weight] to [1: node]. Heap to sort by [0]
        # Assign points[0] as source node with cost 0
        heap = MinHeap([(0, 0)])
        
        # To iterate over edges gives no guarantee each
        # iteration adds 1 node to connected component
        while nInMST < n:
            weight, toNode = heap.pop()
            
            # Only add nodes not already added. If added, skip
            if isAdded[toNode]: continue
            
            # Lighest newly-scanned edge connects unadded node 
            isAdded[toNode] = True
            nInMST  += 1
            sumCost += weight
            
            # Push edge from newly-added node to each unadded node into heap 
            for nbor in range(n):
                if isAdded[nbor]: continue

                addCost = abs(points[toNode][0] - points[nbor][0]) +\
                                abs(points[toNode][1] - points[nbor][1])
                    
                heap.push((addCost, nbor))
                    
        return sumCost

# edge: (0: weight, 1: toNode). Weight to toNode from node in CC
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
          
    # Steps: Swap vals at [0] and [-1]. In O(1), remove
    # 		val now at [-1]. heapifyDown(..) from [0]
    def pop(self) -> (int, int):
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            prevRoot = self.heap.pop()
            self.heapifyDown(self.heap)
            return prevRoot
        
        return

    # Ensure heapness down from lone index i of arr,
    # default being i = 0 for call by pop(),
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