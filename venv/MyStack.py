class MyStack:
   # Constants
   MAX_SIZE = 100000
   DEFAULT_SIZE = 10

   def __init__(self, default_item, capacity=DEFAULT_SIZE):
      # If the capacity is bad, fail right away
      if not self.valid_capacity(capacity):
         raise Exception("Capacity " + str(capacity) + " is invalid")
      self.capacity = capacity
      self.default_item = default_item

      # Make room in the stack and make sure it's empty to begin with
      self.clear()

   def push(self, item_to_push):
      if self.is_full():
         raise Exception("Push failed - capacity reached")

      self.stack[self.top_of_stack] = item_to_push
      self.top_of_stack += 1

   def pop(self):
      if self.is_empty():
         raise Exception("Pop failed - stack is empty")

      self.top_of_stack -= 1
      return self.stack[self.top_of_stack]

   def clear(self):
      # Allocate storage the storage and initialize top of stack
      self.stack = np.array([self.default_item for _ in range(self.capacity)])
      self.top_of_stack = 0

   def is_empty(self):
      return self.top_of_stack == 0

   def is_full(self):
      return self.top_of_stack == self.capacity

   def get_capacity(self):
      return self.capacity

   # class methods ------------------------
   @classmethod
   def valid_capacity(cls, test_capacity):
      return 0 <= test_capacity <= cls.MAX_SIZE
