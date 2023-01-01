from collections import defaultdict

def day14():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  rock_points_x = defaultdict(set)
  rock_points_y = defaultdict(set)

  max_depth = float("-inf")

  for line in puzzle_input:
    rock_lines = line.split(" -> ")
    for i in range(len(rock_lines)-1):
      from_x, from_y = rock_lines[i].split(",")
      to_x, to_y = rock_lines[i+1].split(",")
      
      from_x, from_y, to_x, to_y = int(from_x), int(from_y), int(to_x), int(to_y)
      max_depth = max(max_depth, from_y, to_y)

      for j in range(min(from_x, to_x), max(from_x, to_x) + 1):
        for k in range(min(from_y, to_y), max(from_y, to_y) + 1):
          rock_points_x[j].add(k)
          rock_points_y[k].add(j)

  p1_rested_sand = 0
  p2_rested_sand = 0

  def p1_drop_sand():
    pos = [500, 0]

    while pos[1] < max_depth:
      down = pos[1] + 1
      left = pos[0] - 1
      right = pos[0] + 1
      if pos[0] not in rock_points_x or down not in rock_points_x[pos[0]]:
        pos[1] += 1
      elif down not in rock_points_x[left]:
        pos[0] -= 1
        pos[1] += 1
      elif down not in rock_points_x[right]:
        pos[0] += 1
        pos[1] += 1
      else:
        break
    
    # returns position of sand either settled or infinitely falling once below the max depth
    return pos

  infinite_floor = max_depth + 2

  def p2_drop_sand():
    pos = [500, 0]

    while True:
      down = pos[1] + 1
      left = pos[0] - 1
      right = pos[0] + 1

      if down == infinite_floor:
        break
      
      if pos[0] not in rock_points_y[down]:
        pos[1] += 1
      elif left not in rock_points_y[down]:
        pos[0] -= 1
        pos[1] += 1
      elif right not in rock_points_y[down]:
        pos[0] += 1
        pos[1] += 1
      else:
        break
    
    return pos
  
  while True:
    x,y = p1_drop_sand()

    if y >= max_depth:
      print("part1", p1_rested_sand)
      break

    # settled sand becomes rock
    rock_points_x[x].add(y)
    p1_rested_sand += 1
  
  while True:
    x,y = p2_drop_sand()

    # settled sand becomes rock
    rock_points_y[y].add(x)
    p2_rested_sand += 1

    if x == 500 and y == 0:
      print("part2", p2_rested_sand)
      break

day14()