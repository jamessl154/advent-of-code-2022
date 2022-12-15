class Node:
  def __init__(self, prev):
    self.dirs = {}
    self.files = []
    self.prev = prev

def day7():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("$")
  
  # recreate filesystem in a data structure, traverse data structure for each dir
  # sum all dirs with total file size less than 100000

  # node.dirs {} of nodes
  # node.files [] of file sizes
  # node.prev

  root = Node(None)
  cur = Node(root)
  root.dirs['/'] = cur

  for i in range(2, len(puzzle_input)):

    command = puzzle_input[i].splitlines()
    
    action = command[0].strip()

    if action == 'ls':
      for item in command[1:]:
        if item[:4] == 'dir ':
          cur.dirs[item[4:]] = Node(cur)
        else:
          fileSize, fileName = item.split(" ")
          cur.files.append(int(fileSize))

    if action[:2] == 'cd':
      if action[3:] == '..':
        cur = cur.prev
      else:
        cur = cur.dirs[action[3:]]

  part1 = 0
  dir_sizes = []

  def dfs(node):
    nonlocal part1
    cur = 0
    if node.files:
      cur += sum(node.files)
    
    for directory in node.dirs.values():
      cur += dfs(directory)

    if cur < 100000:
      part1 += cur
    
    dir_sizes.append(cur)

    return cur
  
  total = dfs(root.dirs['/'])
  print("part1", part1)

  unused = 70000000 - total
  dir_sizes.sort()

  for dir_size in dir_sizes:
    if dir_size + unused >= 30000000:
      print("part2", dir_size)
      break
day7()