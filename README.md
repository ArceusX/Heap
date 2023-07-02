## Summary
- Extend MaxHeap functionality to Python's heapq
- Show usage of Heap class to solve Leetcode Problem 1584

## Functions
### Core
```diff 
+ heapify(arr,      isMin = True) -> None
- push   (arr, val, isMin = True) -> None
! pop    (arr,      isMin = True) -> V
+ replace(arr, val, isMin = True) -> V
- pushpop(arr, val, isMin = True) -> V
! nlargest (n, iterable)          -> List
+ nsmallest(n, iterable)          -> List
- isHeap (arr,      isMin = True) -> bool
```

### Helper
```diff
+ setKey     (arr, i, newVal, isMin = True) -> T that was overwritten
- heapifyUp  (arr, i = None , isMin = True) -> None
! heapifyDown(arr, i = None , isMin = True) -> None
```

### In-Depth
| Function    | Explain                                              |
|-------------|------------------------------------------------------|
| heapify     | Arrange arr into (Min\|Max) heap of isMin's order    |
| push        | Keep same heapness as isMin's heap order             |
| pop         | Pop val--(low\|high)est--matching isMin's heap order |
| replace     | Pop, then push val. Return val popped                |
| pushpop     | Push, then pop, and return popped val                |
| nlargest    | Get n largest  vals in iterable as MinHeap           |
| nsmallest   | Get n smallest vals in iterable as MaxHeap           |
| isHeap      | True if arr matches isMin's heap order               |
| setKey      | Set arr[i] = newVal. Return prev arr[i]              |
| heapifyUp   | Ensure heapness up   from lone index i of arr        |
| heapifyDown | Ensure heapness down from lone index i of arr        |

## Leetcode
For minimum spanning tree, use Heap to get subsequent min-weight edge