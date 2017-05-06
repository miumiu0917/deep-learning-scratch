from not_gate import NOT
from or_gate import OR
from and_gate import AND

def XOR(x, y):
  bynary = [0, 1]
  if not (x in bynary and y in bynary):
    raise ValueError('Invalid arguments. x and y must be 0 or 1.')
  
  return OR(AND(x, NOT(y)), AND(NOT(x), y))


print(XOR(1, 1))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(0, 0))
