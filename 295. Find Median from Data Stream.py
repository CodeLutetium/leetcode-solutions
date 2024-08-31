class MedianFinder:
    # Space complexity: O(n)
    def __init__(self):
        self.min_heap = []  # Store low numbers
        self.max_heap = []  # Store high numbers

    # Time complexity: O(log n)
    def addNum(self, num: int) -> None:
        # num smaller than largest number in min_heap: Add to min_heap
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the two heaps if they differ by more than 1 
        if len(self.max_heap) > len(self.min_heap) + 1:
            moved_value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, moved_value)
        elif len(self.min_heap) > len(self.max_heap):
            moved_value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved_value)

    # Time complexity: O(1)
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()