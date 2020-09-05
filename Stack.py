class Stack:
  def __init__(self, *kwargs):
    self.data = list(reversed(list(kwargs)))
  
  def display(self):
    for element in self.data:
      print(f'''
                __________
                |         |
                |{element:^9}|
                |_________|''', end='')
  
  def push(self, value):
    self.data.append(value)
  
  def pop(self):
    self.data.pop()
