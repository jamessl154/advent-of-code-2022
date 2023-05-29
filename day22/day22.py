from collections import defaultdict

def day22(filename, p1):
  with open(filename, "r") as f:
    puzzle_input = f.read().split("\n")
    directions, grid = puzzle_input[-1], puzzle_input[:-2]

  class Mover:
    def __init__(self, row, col):
      self.direction = 'R'
      self.row = row
      self.col = col

    def rotate(self, direction):
      match self.direction:
        case 'L':
          if direction == 'L':
            self.direction = 'D'
          else:
            self.direction = 'U'
        case 'R':
          if direction == 'L':
            self.direction = 'U'
          else:
            self.direction = 'D'
        case 'U':
          if direction == 'L':
            self.direction = 'L'
          else:
            self.direction = 'R'
        case 'D':
          if direction == 'L':
            self.direction = 'R'
          else:
            self.direction = 'L'

    def move(self, num_steps):
      while num_steps > 0:
        match self.direction:
          case 'U':
            if self.row == vertical_start[self.col]:
              if not p1:
                edge = edges[(self.direction, self.row, self.col)]
                next_row = edge.next_pos[0]
                next_col = edge.next_pos[1]
                next_direction = edge.new_direction
              else:
                next_row = vertical_end[self.col]
                next_col = self.col
                next_direction = self.direction
            else:
              next_row = self.row - 1
              next_col = self.col
              next_direction = self.direction
            
            # look ahead before moving or changing direction
            if grid[next_row][next_col] == '#':
              break
            
          case 'D':
            if self.row == vertical_end[self.col]:
              if not p1:
                edge = edges[(self.direction, self.row, self.col)]
                next_row = edge.next_pos[0]
                next_col = edge.next_pos[1]
                next_direction = edge.new_direction
              else:
                next_row = vertical_start[self.col]
                next_col = self.col
                next_direction = self.direction
            else:
              next_row = self.row + 1
              next_col = self.col
              next_direction = self.direction
            
            if grid[next_row][next_col] == '#':
              break

          case 'L':
            if self.col == horizontal_start[self.row]:
              if not p1:
                edge = edges[(self.direction, self.row, self.col)]
                next_row = edge.next_pos[0]
                next_col = edge.next_pos[1]
                next_direction = edge.new_direction
              else:
                next_row = self.row
                next_col = horizontal_end[self.row]
                next_direction = self.direction
            else:
              next_row = self.row
              next_col = self.col - 1
              next_direction = self.direction
            
            if grid[next_row][next_col] == '#':
              break

          case 'R':
            if self.col == horizontal_end[self.row]:
              if not p1:
                edge = edges[(self.direction, self.row, self.col)]
                next_row = edge.next_pos[0]
                next_col = edge.next_pos[1]
                next_direction = edge.new_direction
              else:
                next_row = self.row
                next_col = horizontal_start[self.row]
                next_direction = self.direction
            else:
              next_row = self.row
              next_col = self.col + 1
              next_direction = self.direction
            
            if grid[next_row][next_col] == '#':
              break
        
        self.row = next_row
        self.col = next_col
        self.direction = next_direction
        
        num_steps -= 1

  def find_start(grid):
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == '.':
          return (i, j)
  
  def parse_directions(directions):
    res = []
    i, j = 0, 0
    while i < len(directions):
      if not directions[i].isnumeric():
        res.append(directions[j:i])
        res.append(directions[i])
        j = i + 1
      i += 1
    res.append(directions[j:i])
    return res
  
  horizontal_start = defaultdict(lambda: float('inf'))
  horizontal_end = defaultdict(lambda: float('-inf'))
  vertical_start = defaultdict(lambda: float('inf'))
  vertical_end = defaultdict(lambda: float('-inf'))

  def initialize_map(map):
    for i in range(len(map)):
      for j in range(len(map[i])):
        if map[i][j] == '.' or map[i][j] == '#':
          horizontal_start[i] = min(horizontal_start[i], j)
          horizontal_end[i] = max(horizontal_end[i], j)
          vertical_start[j] = min(vertical_start[j], i)
          vertical_end[j] = max(vertical_end[j], i)

  start = find_start(grid)
  initialize_map(grid)
  dir_list = parse_directions(directions)

  # for i in sorted(vertical_start):
  #   print('vertical', i,vertical_start[i],vertical_end[i])
  # print("----------")
  # for i in sorted(horizontal_start):
  #   print('horizontal', i,horizontal_start[i],horizontal_end[i])
  
  def initialize_edges(edges):
    for i in range(50):
      # 5 U
      edges[('U', 100, i)] = Edge((i + 50, 50), 'R')
      # 2 L
      edges[('L', i + 50, 50)] = Edge((100, i), 'D')

      # 1 D
      edges[('D', 149, i + 50)] = Edge((i + 150, 49), 'L')
      # 6 R
      edges[('R', i + 150, 49)] = Edge((149, i + 50), 'U')

      # 5 L
      edges[('L', i + 100, 0)] = Edge((49-i, 50), 'R')
      # 3 L
      edges[('L', 49-i, 50)] = Edge((i + 100, 0), 'R')

      # 4 R
      edges[('R', 49-i, 149)] = Edge((i + 100, 99), 'L')
      # 1 R
      edges[('R', i + 100, 99)] = Edge((49-i, 149), 'L')

      # 2 R
      edges[('R', i + 50, 99)] = Edge((49, 100 + i), 'U')
      # 4 D
      edges[('D', 49, 100 + i)] = Edge((i + 50, 99), 'L')

      # 3 U
      edges[('U', 0, i + 50)] = Edge((i + 150, 0), 'R')
      # 6 L
      edges[('L', i + 150, 0)] = Edge((0, i + 50), 'D')

      # 4 U
      edges[('U', 0, 100 + i)] = Edge((199, i), 'U')
      # 6 D
      edges[('D', 199, i)] = Edge((0, 100 + i), 'D')

  class Edge:
    def __init__(self, next_pos, new_direction):
      self.next_pos = next_pos
      self.new_direction = new_direction

  edges = {}

  if not p1:
    initialize_edges(edges)
  
  mover = Mover(start[0], start[1])
  for command in dir_list:
    if command.isnumeric():
      mover.move(int(command))
    else:
      mover.rotate(command)

  def facing_score(direction):
    match direction:
      case 'R':
        return 0
      case 'D':
        return 1
      case 'L':
        return 2
      case 'U':
        return 3

  if p1:
    print('p1', filename, 1000 * (mover.row + 1) + 4 * (mover.col + 1) + facing_score(mover.direction))
  else:
    print('p2', filename, 1000 * (mover.row + 1) + 4 * (mover.col + 1) + facing_score(mover.direction))

# day22('example.txt', True)
day22('input.txt', True)

# day22('example.txt', False)
day22('input.txt', False)