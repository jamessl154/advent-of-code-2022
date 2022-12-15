def day8():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

  rows, cols = len(puzzle_input), len(puzzle_input[0])

  edges = cols * 2 + rows * 2 - 4

  visible_trees = set()

  # L
  for i in range(1, rows-1):

    l_max = puzzle_input[i][0]

    for j in range(1, cols-1):

      if puzzle_input[i][j] > l_max:
        visible_trees.add((i,j))
      
      l_max = max(l_max, puzzle_input[i][j])

  # R
  for i in range(1, rows-1):

    r_max = puzzle_input[i][cols-1]

    for j in range(cols-2, 0, -1):

      if puzzle_input[i][j] > r_max:
        visible_trees.add((i,j))

      r_max = max(r_max, puzzle_input[i][j])
  
  # T
  for j in range(1, cols-1):

    t_max = puzzle_input[0][j]

    for i in range(1, rows-1):

      if puzzle_input[i][j] > t_max:
        visible_trees.add((i,j))
      
      t_max = max(t_max, puzzle_input[i][j])

  # B
  for j in range(1, cols-1):
    
    b_max = puzzle_input[rows-1][j]

    for i in range(rows-2, 0, -1):

      if puzzle_input[i][j] > b_max:
        visible_trees.add((i,j))
      
      b_max = max(b_max, puzzle_input[i][j])
  
  print("part1", len(visible_trees) + edges)

  def find_scenic_score(i, j, puzzle_input):
    height = puzzle_input[i][j]
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    
    up, down, left, right = 0, 0, 0, 0

    # up
    for k in range(i-1, -1, -1):
      up += 1
      if puzzle_input[k][j] >= height:
        break
    
    # down
    for k in range(i+1, rows):
      down += 1
      if puzzle_input[k][j] >= height:
        break
    
    # left
    for k in range(j-1, -1, -1):
      left += 1
      if puzzle_input[i][k] >= height:
        break
    
    # right
    for k in range(j+1, cols):
      right += 1
      if puzzle_input[i][k] >= height:
        break
    
    scenic_score = up * down * left * right
    return scenic_score

  part2 = 0
  for i in range(rows):
    for j in range(cols):
      part2 = max(part2, find_scenic_score(i, j, puzzle_input))
  
  print("part2", part2)

day8()