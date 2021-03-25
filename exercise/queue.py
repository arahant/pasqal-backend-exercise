from exception import ErrorEmptyQueue, ErrorInvalidData
import heapq

class PriorityQueue():

    self __init__(self):
        self.queue = []
        self.time = 0

    def push(self, item, priority):
        """
        Users can push items with a priority to the queue
        """
        # if item is NULL, throw exception
        if not item:
            raise ErrorInvalidData('Invalid item')

        # if priority is NULL or NEGATIVE, throw exception
        if not priority or priotity < 0:
            raise ErrorInvalidData('Invalid priority')

        self.time += 1
        val = (-priority, self.time, item)
        heapq.heappush(self.queue, val)


    def pop(self):
        """
        When popping an item from the queue, we get the item with the highest priority.
        If there are many with the same priority, we return the oldest.
        """
        # if queue is empty, throw exception
        if not self.queue:
            raise ErrorEmptyQueue("Empty queue")

        priority, time, item = heapq.heappop(self.queue)
        return item
