from collections import defaultdict

def day23(filename, p1):
  with open(filename, "r") as f:
    puzzle_input = f.read().split("\n")
  
  def initialize_elves():
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    for i in range(rows):
      for j in range(cols):
        if puzzle_input[i][j] == '#':
          elves[i].add(j)

  def calculate_score():
    minCol, maxCol = float("inf"), float("-inf")
    minRow, maxRow = float("inf"), float("-inf")
    for row in elves:
      minRow, maxRow = min(row, minRow), max(row, maxRow)
      for col in elves[row]:
        minCol, maxCol = min(col, minCol), max(col, maxCol)
    
    elfTiles = sum([len(elves[row]) for row in elves])
    groundTiles = (maxRow - minRow + 1) * (maxCol - minCol + 1)

    return groundTiles - elfTiles

  def has_adjacent_elf(row, col):
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for dr, dc in directions:
      if row + dr in elves and col + dc in elves[row + dr]:
        return True
    return False

  def is_north_free(row, col):
    north_dirs = [[-1,-1],[-1,0],[-1,1]]
    for dr, dc in north_dirs:
      if row + dr in elves and col + dc in elves[row + dr]:
        return False
    return True

  def is_south_free(row, col):
    south_dirs = [[1,-1],[1,0],[1,1]]
    for dr, dc in south_dirs:
      if row + dr in elves and col + dc in elves[row + dr]:
        return False
    return True

  def is_west_free(row, col):
    west_dirs = [[-1,-1],[0,-1],[1,-1]]
    for dr, dc in west_dirs:
      if row + dr in elves and col + dc in elves[row + dr]:
        return False
    return True

  def is_east_free(row, col):
    east_dirs = [[-1,1],[0,1],[1,1]]
    for dr, dc in east_dirs:
      if row + dr in elves and col + dc in elves[row + dr]:
        return False
    return True
  
  def check_first_free(start_index, row, col):
    lm_north = lambda x,y: is_north_free(x,y)
    lm_south = lambda x,y: is_south_free(x,y)
    lm_west = lambda x,y: is_west_free(x,y)
    lm_east = lambda x,y: is_east_free(x,y)
    fn_list = [(lm_north, (row-1, col)), (lm_south, (row+1, col)), (lm_west, (row, col-1)), (lm_east, (row, col+1))]
    for i in range(4):
      index = (start_index + i) % 4
      test, new_pos = fn_list[index]
      if test(row, col):
        return new_pos
    return False

  def simulate_rounds(rounds):
    start_index = 0
    for round_num in range(rounds):
      num_elves = sum([len(elves[row]) for row in elves])
      collisions = set()
      proposed_to_initial = {}
      for row in elves:
        for col in elves[row]:
          if has_adjacent_elf(row, col):
            proposed_move = check_first_free(start_index, row, col)
            if proposed_move:
              if proposed_move in proposed_to_initial:
                collisions.add(proposed_move)
              else:
                proposed_to_initial[proposed_move] = [row, col]
          else:
            num_elves -= 1
      
      if not p1 and num_elves == 0:
        print("p2", round_num + 1)
        return

      for proposed in proposed_to_initial:
        if proposed not in collisions:
          old_r, old_c = proposed_to_initial[proposed]
          next_r, next_c = proposed
          elves[old_r].remove(old_c)
          if not len(elves[old_r]): # if last col in row, delete row in elves
            del elves[old_r]
          elves[next_r].add(next_c)
      start_index += 1

  elves = defaultdict(set)
  initialize_elves()
  rounds = 10 # for p2 input.txt 1200
  simulate_rounds(rounds)
  print('p1', calculate_score())

day23('example.txt', True)
day23('input.txt', True)

# day23('example.txt', False)
# day23('input.txt', False)