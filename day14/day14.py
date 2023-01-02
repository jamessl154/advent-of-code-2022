from collections import defaultdict

def day14():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  p1_rock_points = defaultdict(set)
  p2_rock_points = defaultdict(set)

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
          p1_rock_points[k].add(j)
          p2_rock_points[k].add(j)

  p1_rested_sand = 0
  p2_rested_sand = 0

  infinite_floor = max_depth + 2

  def drop_sand(rock_points, max_depth):
    pos = [500, 0]
    while True:
      down = pos[1] + 1
      left = pos[0] - 1
      right = pos[0] + 1

      if down == max_depth:
        return pos
      
      if down not in rock_points or pos[0] not in rock_points[down]:
        pos[1] += 1
      elif left not in rock_points[down]:
        pos[0] -= 1
        pos[1] += 1
      elif right not in rock_points[down]:
        pos[0] += 1
        pos[1] += 1
      else:
        return pos

  while True:
    x, y = drop_sand(p1_rock_points, max_depth + 1)

    if y == max_depth:
      print("part1", p1_rested_sand)
      break

    # settled sand becomes rock
    p1_rock_points[y].add(x)
    p1_rested_sand += 1
  
  while True:
    x, y = drop_sand(p2_rock_points, infinite_floor)

    p2_rock_points[y].add(x)
    p2_rested_sand += 1

    if x == 500 and y == 0:
      print("part2", p2_rested_sand)
      break

day14()