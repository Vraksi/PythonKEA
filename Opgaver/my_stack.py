
###############################################################################
##                                                                           ##
## stack.py: Prototype demonstrating Interface to Classical Stack.           ##
##                                                                           ##
## Written by Keld Kondrup Jensen, Kondrup Invest ApS.                       ##
##                                                                           ##
## Time of creation: Sat Sep 24 11:18:24 2022 (by Keld Kondrup Jensen).      ##
##    Last modified: Sat Sep 24 11:18:24 2022 (by Keld Kondrup Jensen).      ##
##                                                                           ##
###############################################################################

## My first attempt on approaching implementation of a formal Stack.
class adt_stack():
    """FILO: First-In-Last-Out Collection"""

    def __init__(self, copy = None):
        self.list = []
        """FILO constructor: Create an 'NILL' element Stack"""

    def push(self, item):
        self.list.append(item)
        """FILO constructor: Append element as end-of Stack"""

    def pull(self, item = None):
        self.list.pop(len(self.list) - 1)
        """FILO operator: Remove an element at end-of Stack"""

    def peek(self, item = None):
        print(self.list[len(self.list)-1])
        return self.list[len(self.list)-1]
        """FILO selector: Locate an element as end-of Stack"""

    def size(self):
        print(len(self.list))
        return(len(self.list))
        """FILO procejtor: Provide element Count from Stack"""
        
    def top(self):
        """FILO selector: Locate an element as end-of Stack"""
        ## The Formal name for what I've chosen as 'peek'
        return adt_stack.peek(self)
        
    def pop(self):
        """FILO operator: Remove an element at end-of Stack"""
        ## The Formal name for what I've chosen as 'pull'
        return adt_stack.pull(self, self.top())

    def join(self, listToJoin):
        for item in listToJoin:
            self.list.append(item)
        print(self.list)
        return(self.list)

    def __del__(self):
        """FILO destructor: 'Victimizes' Stack and elements"""
        ## Ignore for now ... yet to come


stack = adt_stack();
stack.push(2)
stack.push(3)
stack.push(32)
stack.push(3232)
stack.peek()
stack.peek()
stack.top()
stack.pop()
stack.top()
print(stack.list)
stack2 = adt_stack();
stack2.push(1)
stack2.push(2)
stack2.push(21)
stack2.push(89898)

numbers = [2,2,3,4,5,6]

stack.join(numbers)

