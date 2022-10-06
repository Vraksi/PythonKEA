
###############################################################################
##                                                                           ##
## queue.py: Prototype demonstrating Interface to Classical Queue.           ##
##                                                                           ##
## Written by Keld Kondrup Jensen, Kondrup Invest ApS.                       ##
##                                                                           ##
## Time of creation: Sat Sep 24 11:18:24 2022 (by Keld Kondrup Jensen).      ##
##    Last modified: Sat Sep 24 11:18:24 2022 (by Keld Kondrup Jensen).      ##
##                                                                           ##
###############################################################################

## My first attempt on approaching implementation of a formal Queue.
class adt_queue():
    """FIFO: First-Come-First-Serve Collection"""
    

    def __init__(self, copy = None):
        self.list = []
        self.__x = 2
        """FIFO constructor: Create an 'NILL' element Queue"""

    def enqueue(self, item ):
        self.list.append(item)
        """FIFO constructor: Append 'last' element to Queue"""

    def dequeue(self, item = None):
        self.list.pop(0)
        """FIFO operator: Remove 'first' element from Queue"""

    def q_front(self, item = None):
        print(self.list[0])
        return(self.list[0])
        """FIFO selector: Locate 'first' element from Queue"""

    def q_count(self):
        print(len(self.list))
        return(len(self.list))
        """FIFO procejtor: Provide element Count from Queue"""
        

    def peek(self):
        """FIFO selector: Locate 'first' element from Queue"""
        ## Alias used to 'standardize' my adt_collections ...
        return adt_queue.q_front(self)
    
    def size(self):
        """FIFO procejtor: Provide element Count from Queue"""
        ## Alias used to 'standardize' my adt_collections ...
        return adt_queue.q_count(self)
        

    def __del__(self):
        """FIFO destructor: 'Victimizes' Queue and elements"""
        ## Ignore for now ... yet to come


que = adt_queue()
que.enqueue(2)
que.enqueue(2542)
que.enqueue(23)
que.enqueue(222)
que.enqueue(21)
que.enqueue(23)
que.size()
que.peek()
que.dequeue()
que.dequeue()
que.dequeue()
que.peek()
que.enqueue(21)
que.enqueue(21)
que.enqueue(21)
que.dequeue()
que.dequeue()
que.peek()
