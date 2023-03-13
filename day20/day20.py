from collections import defaultdict

def day20(filename, p1):
  with open(filename, "r") as f:
    puzzle_input = f.read().split("\n")
  
  initial_positions = []

  for i, v in enumerate(puzzle_input):
    if v == '0':
      zero = (i, int(v))
    initial_positions.append((i, int(v) if p1 else int(v) * 811589153))

  cur = initial_positions[:]

  for i in range(1 if p1 else 10):
    for index, jumps in initial_positions:
      
      if jumps % (len(initial_positions) - 1) == 0:
        continue

      s = cur.index((index, jumps))
      e = (s + jumps) % (len(initial_positions) - 1)

      if s < e:
        cur[s:e] = cur[s+1:e+1]
      else:
        cur[e+1:s+1] = cur[e:s]
      
      cur[e] = (index, jumps)

  zero_index = cur.index(zero)

  res = 0
  for i in range(3):
    res += cur[(zero_index + (i+1) * 1000) % len(cur)][1]

  print('p1' if p1 else 'p2', filename, res)

day20('example.txt', True)
day20('input.txt', True)

day20('example.txt', False)
day20('input.txt', False)