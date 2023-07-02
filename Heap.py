# If isMin == (T|F), read arr as or heapify arr to
# (Min|Max)Heap, with (low|high)est val at arr[0]
class Heap:

    # Arrange arr into (Min|Max) heap of isMin's order 
    @staticmethod
    def heapify(arr, isMin = True) -> None:
        for i in range(1, len(arr)):
            Heap.heapifyUp(arr, i, isMin)

    # On push, keep same heapness as isMin's heap order
    @staticmethod
    def push(arr, val, isMin = True) -> None:
        arr.append(val)
        Heap.heapifyUp(arr, None, isMin) # From arr[-1]

    # Pop val--(low|high)est--matching isMin's heap order
    # Do: Swap vals at [0] and [-1]. In O(1), remove
    #     val now at [-1]. heapifyDown(..) from [0]
    @staticmethod
    def pop(arr, isMin = True):
        if arr:
            arr[0], arr[-1] = arr[-1], arr[0]
            preRoot = arr.pop()
            if len(arr) > 1:
                Heap.heapifyDown(arr, 0, isMin)
            return preRoot
        
        raise IndexError("Cannot pop from empty heap")

    # Pop, then push val. Return val popped/overwrote
    @staticmethod
    def replace(arr, val, isMin = True):
        return Heap.setKey(arr, 0, val, isMin)

    # Push, then pop, and return popped val. More efficient than 
    # separate push, then pop. If isMin == (T|F) and push of val
    # (high|low)er than arr[0], return same val as replace(..)
    @staticmethod
    def pushpop(arr, val, isMin = True):
        # No change if popped val is same val just pushed
        if not arr or \
            (isMin and val < arr[0]) or (not isMin and arr[0] < val):
            return val
        
        else: # Overwrite arr[0] and return it
            return Heap.setKey(arr, 0, val, isMin)

    # Re: n largest vals in iterable as MinHeap (list) with
    #     nth largest being Re[0]
    @staticmethod
    def nlargest (n, iterable):
        li = []
        it = iter(iterable)
        
        # Push each of first n vals into MinHeap
        for i in range(0, n):
            try:
                Heap.push(li, next(it))
                
            except StopIteration:
                break
            
        if len(li) == n and n > 0: # if iterable has >= n vals 
            # Check if each after first n exceed and 
            # replace li[0], least of current nlargest
            while True:
                try:
                    x = next(it)
                    if  li[0] < x:
                        li[0] = x
                        Heap.heapifyDown(li, 0)
                    
                except StopIteration:
                    break
            
        return li

    # Re: n smallest vals in iterable as MaxHeap (list) with
    #     nth smallest being Re[0]
    # Re: empty list if n <= 0
    @staticmethod
    def nsmallest(n, iterable):
        li = []
        it = iter(iterable)
        
        for i in range(0, n):
            try: # Push each of first n vals into MaxHeap
                Heap.push(li, next(it), False)
                
            except StopIteration:
                break
            
        if len(li) == n and n > 0: # if iterable has >= n vals 
            # Check if each after first n is lesser than and
            # replace li[0], largest of current nsmallest
            while True:
                try:
                    x = next(it)
                    if  x < li[0]:
                        li[0] = x
                        Heap.heapifyDown(li, 0, False)
                    
                except StopIteration:
                    break
            
        return li
        
    # Re: True if arr matches isMin's heap order
    # Check heap property fail between each child and its parent
    def isHeap(arr, isMin = True) -> bool:
        if not arr: return False
        
        if isMin:
            for child in range(len(arr) - 1, 0, -1):
                # Not MinHeap if parent exceeds child
                if arr[child] < arr[(child - 1) // 2]:
                    return False
            
        else:
            for child in range(len(arr) - 1, 0, -1):
                # Not MaxHeap if child exceeds parent
                if arr[(child - 1) // 2] < arr[child]:
                    return False
            
        return True
    
    #------------------------Helper------------------------
    #------------------------------------------------------

    # Re: preVal. Set arr[i] = newVal, restore heapness
    @staticmethod
    def setKey(arr, i, newVal, isMin = True):        
        preVal = arr[i]
        arr[i] = newVal
        
        if isMin:
            if   newVal < preVal: # Push change- up
                Heap.heapifyUp  (arr, i, True)
            elif preVal < newVal: # Push change+ down
                Heap.heapifyDown(arr, i, True)

        else:
            if   newVal < preVal: # Push change- down
                Heap.heapifyDown(arr, i, False)
            elif preVal < newVal: # Push change+ up
                Heap.heapifyUp  (arr, i, False)

        return preVal

    # Ensure heapness up from lone index i of arr, default being
    # arr's final index for call by push(), for isMin's heap order
    @staticmethod
    def heapifyUp(arr, i = None, isMin = True) -> None:
        if i is None: i = len(arr) - 1
        if not (0 <=  i < len(arr)):
            raise IndexError(f"index {i} is out-of-range for len {len(arr)}")
        
        child  = i
        parent = (child - 1) // 2

        # Resolve up: Swap to set lower-ordered val as parent 
        # Child's sibling accepts parent swapped lower-ordered val
        while child != 0:
            if not isMin and arr[parent] < arr[child]:
                arr[parent], arr[child]  = arr[child], arr[parent]

            elif   isMin and arr[child]  < arr[parent]:
                arr[parent], arr[child]  = arr[child], arr[parent]

            else:
                break

            child = parent
            parent = (child - 1) // 2

    # Ensure heapness down from lone index i of arr, default
    # being i = 0 for call by pop(), for isMin's heap order
    @staticmethod
    def heapifyDown(arr, i = 0, isMin = True):
        n = len(arr)
        
        if not (0 <= i < n):
            raise IndexError(f"index {i} is out-of-range for len {len(arr)}")
        
        parent = i
        child  = 2 * parent + 1 # leftChild
        
        # Child's sibling accepts parent swapped lower-ordered val
        while child < n:
            # Set child to lower-ordered child between left and right
            if (child < n - 1):
                if not isMin and arr[child] < arr[child + 1]:
                    child += 1
                elif   isMin and arr[child + 1] < arr[child]:
                    child += 1
                
            if not isMin and arr[parent] < arr[child]:
                arr[parent], arr[child]  = arr[child], arr[parent]

            elif   isMin and arr[child]  < arr[parent]:
                arr[parent], arr[child]  = arr[child], arr[parent]
                
            # If no swap, no longer need to heapifyDown subtree
            else:
                break
            
            parent = child
            child = 2 * parent + 1
   