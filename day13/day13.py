from itertools import zip_longest
from functools import cmp_to_key

def day13():
  with open("input.txt", "r") as f:
  # with open("example.txt", "r") as f:
    puzzle_input = f.read().split("\n")

  def list_parser(list_input):
    stack = []
    parsed = []
    cur = 1
    for i in range(1,len(list_input)-1):
      if list_input[i] == '[':
        stack.append(i)
      elif list_input[i] == ']':
        stack.pop()
      elif list_input[i] == ',' and not stack:
        parsed.append(list_input[cur:i])
        cur = i+1
    parsed.append(list_input[cur:-1])
    return parsed

  def recursive_parser(l, r):
    if not l and not r:
      return 0 # flag for equality
    if not l:
      return 1
    if not r:
      return -1

    if l.isnumeric() and r.isnumeric():
      if int(l) < int(r):
        return 1
      elif int(l) > int(r):
        return -1
      else:
        return 0

    if l.isnumeric():
      l_input, r_input = [l], list_parser(r)
    elif r.isnumeric():
      l_input, r_input = list_parser(l), [r]
    else:
      l_input, r_input = list_parser(l), list_parser(r)

    for l_item, r_item in zip_longest(l_input, r_input):
      cur = recursive_parser(l_item, r_item)
      if cur == 1 or cur == -1:
        return cur

  part1 = 0

  part2_list = []

  for i in range(0, len(puzzle_input), 3):
    first, second = puzzle_input[i], puzzle_input[i+1]
    res = recursive_parser(first, second)
    part1 += (i//3 + 1) if res == 1 else 0
    part2_list.append(first)
    part2_list.append(second)
  print("part1", part1)

  part2_list.append('[[2]]')
  part2_list.append('[[6]]')

  # https://learnpython.com/blog/python-custom-sort-function/
  part2_list.sort(key=cmp_to_key(recursive_parser), reverse=True)

  part2 = [0,0]
  for i,v in enumerate(part2_list):
    if v == '[[2]]':
      part2[0] = i+1
    if v == '[[6]]':
      part2[1] = i+1
  
  print('part2', part2[0] * part2[1])

# 3 cases for item pairs:
#   1. both integers
#   2. 1 item is list
#   3. both lists

day13()

# https://docs.python.org/3/library/itertools.html#itertools.zip_longest
# zip_longest aggregates both iterables defaults to fillvalue=None if not specified
# zip cuts off if iterables are uneven and the result iterable has the length of the shortest iterable input

# bug:
# for i,j in zip_longest('31', ['1','2','4']):
#   print(i,j)
# 3 1
# 1 2
# None 4

# fixed
# for i,j in zip_longest(['31'], ['1','2','4']):
#   print(i,j)