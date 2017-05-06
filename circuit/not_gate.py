def NOT(x):
  bynary = [0, 1]
  if not x in bynary:
    raise ValueError('Invalid arguments. x and y must be 0 or 1.')
  if x == 0:
    return 1
  else:
    return 0