from collections import defaultdict

def day24(filename, p1):
  with open(filename, "r") as f:
    puzzle_input = f.read().split("\n")
  """
  1. Finite states for rows and cols, rows repeat every X turns, cols repeat every Y turns
  2. Before recursive call, store our current time, row state, col state, pos in cache
  3. At each subsequent recursive call, if we find key (row state, col state, pos) in cache with a slower time, prune the branch by returning early which prevents endless recursion
  4. If faster time, update cache
  5. Search cache to find fastest time with position at exit

  cache size may not be feasible
  m rows, n cols, for mn total spots there will be mn different combinations for row-col state
  """
  
  rows, cols = len(puzzle_input), len(puzzle_input[0])
  max_row_state = rows - 2
  max_col_state = cols - 2
  directions = [[1,0],[0,1],[0,0],[-1,0],[0,-1]]

  cache = defaultdict(lambda: float("inf"))

  start_r, start_c = 0, 1
  exit_pos = (rows-1, cols-2)

  row_dict = { i: [] for i in range(rows-1) }
  col_dict = { i: [] for i in range(1, cols-1) }

  for r in range(rows):
    for c in range(cols):
      direction = puzzle_input[r][c]
      if direction in '^v':
        col_dict[c].append((r, direction))
      elif direction in '<>':
        row_dict[r].append((c, direction))

  def isEmptySpace(r, c, row_state, col_state):
    for blizzard in row_dict[r]:
      col, direction = blizzard
      if direction == '>':
        new_col = (col - 1 + col_state) % max_col_state + 1
        if c == new_col:
          return False
      elif direction == '<':
        new_col = (col - 1 - col_state) % max_col_state + 1
        if c == new_col:
          return False
    for blizzard in col_dict[c]:
      row, direction = blizzard
      if direction == '^':
        new_row = (row - 1 - row_state) % max_row_state + 1
        if r == new_row:
          return False
      elif direction == 'v':
        new_row = (row - 1 + row_state) % max_row_state + 1
        if r == new_row:
          return False
    return True

  def dfs(r, c, row_state, col_state, t):
    if (r, c, row_state, col_state) in cache and cache[(r, c, row_state, col_state)] <= t:
      return
    cache[(r, c, row_state, col_state)] = t
    
    for dr, dc in directions:
      new_r, new_c = r + dr, c + dc
      if 0 <= new_r < rows and 0 <= new_c < cols and puzzle_input[new_r][new_c] != '#':
        new_row_state = (row_state + 1) % max_row_state
        new_col_state = (col_state + 1) % max_col_state
        # forecast empty space at t+1 using row_dict and col_dict, recursive call after check
        if (new_r, new_c) == exit_pos:
          cache[(new_r, new_c, new_row_state, new_col_state)] = min(cache[(new_r, new_c, new_row_state, new_col_state)], t+1)
        elif isEmptySpace(new_r, new_c, new_row_state, new_col_state):
          dfs(new_r, new_c, new_row_state, new_col_state, t+1)

  dfs(start_r, start_c, 0, 0, 0)
  result = float("inf")
  for key in cache:
    r, c, row_state, col_state = key
    if (r, c) == exit_pos:
      result = min(result, cache[key])
  print('p1', result)

# day24('example.txt', True)
day24('input.txt', True)

# day24('example.txt', False)
# day24('input.txt', False)