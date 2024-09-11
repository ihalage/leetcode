import heapq
class MedianFinder:

    def __init__(self):
        ## we are going to keep adding incoming numbers to two heaps
        ## 1. small heap - contains numbers less than or equal to 2. large heap
        ## small heap is going to be a max heap and large heap is a min heap. 
        ## because we want to compare the max of small heap to min of large heap and possibly switch the two if needed
        ## also make sure that the length difference between the two heaps is at most 1
        ## taking the max of max heap and min of min heap is O(1)
        ## removing an element from a heap is O(log(n))
        self.small_heap = []
        self.large_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -1*num)
        if (self.small_heap and self.large_heap and
            (-1*self.small_heap[0])>self.large_heap[0]):
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)

        ## if the sizes become uneven, e.g., their length difference is greater than 1
        if len(self.small_heap)>len(self.large_heap)+1:
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        if len(self.large_heap)>len(self.small_heap)+1:
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -val)

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap): ## we want to take the average of middle values
            val1 = -self.small_heap[0]
            val2 = self.large_heap[0]
            return (val1+val2)/2
        elif len(self.small_heap)>len(self.large_heap):
            return -self.small_heap[0]
        else:
            return self.large_heap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
