from collections import deque

def day18(file_name):
  with open(file_name, "r") as f:
    puzzle_input = f.read().split("\n")

  # +6 for each unconnected cube
  # find all connected pieces and -2 for each connection found
  # do not revisit explored cubes

  cubes = set()
  for line in puzzle_input:
    str_x, str_y, str_z = line.split(",")
    cubes.add((int(str_x), int(str_y), int(str_z)))

  directions = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

  surface_area = 0

  min_x = float("inf")
  min_y = float("inf")
  min_z = float("inf")
  max_x = float("-inf")
  max_y = float("-inf")
  max_z = float("-inf")

  for x,y,z in cubes:

    min_x = min(min_x, x)
    min_y = min(min_y, y)
    min_z = min(min_z, z)
    
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)

    for dx, dy, dz in directions:
      next_node = x+dx, y+dy, z+dz
      if next_node not in cubes:
        surface_area += 1

  min_x -= 1
  min_y -= 1
  min_z -= 1
  max_x += 1
  max_y += 1
  max_z += 1

  q = deque()
  start = (min_x, min_y, min_z)
  q.append(start)
  flood_fill = set()
  flood_fill.add(start)

  droplet_boundary = 0
  while q:
    x,y,z = q.popleft()
    for dx, dy, dz in directions:
      next_x, next_y, next_z = x + dx, y + dy, z + dz
      next_node = (next_x, next_y, next_z)

      if next_node in cubes: # every droplet cube side reachable by floodfill
        droplet_boundary += 1
      elif min_x <= next_x <= max_x and min_y <= next_y <= max_y and min_z <= next_z <= max_z and next_node not in flood_fill:
        flood_fill.add(next_node)
        q.append(next_node)

  print('p1', file_name, surface_area)
  print('p2', droplet_boundary)

day18('example.txt')
day18('input.txt')