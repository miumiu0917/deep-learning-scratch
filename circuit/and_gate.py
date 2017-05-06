def AND(x, y):
  bynary = [0, 1]
  if not (x in bynary and y in bynary):
    raise ValueError('Invalid arguments. x and y must be 0 or 1.')
  w1, w2, theta = 1, 1, 1.2
  tmp = w1 * x + w2 * y
  if tmp <= theta:
    return 0
  else:
    return 1