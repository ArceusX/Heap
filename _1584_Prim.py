# Leetcode 1584: Min Cost to Connect Points (Prim's Algo)

# Into initially-empty connected component (CC), Prim adds
# each node via lighest edge to unadded node from any node 
# already in CC (that edge's weight as unadded node's cost)

#

# Prim: Track each edge in heap. Get lighest edge from heap,
#       then check if that edge connects to unadded node
# Complex.: O(nEdges * ln(nNodes))

class Solution: # Prim 1
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        isAdded = [False] * n
        
        sumCost = 0
        nInMST  = 0

        # Store [0: weight] to [1: node]. Heap to sort by [0]
        # Assign points[0] as source node with cost 0
        heap = [(0, 0)]
        
        # To iterate over edges gives no guarantee each
        # iteration adds 1 node to connected component
        while nInMST < n:
            weight, toNode = heapq.heappop(heap)
            
            # Skip already added candidate
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
                    
                heapq.heappush(heap, (addCost, nbor))
                    
        return sumCost