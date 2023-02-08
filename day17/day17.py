from collections import defaultdict

def day17(file_input, total_falling_rocks):
  with open(file_input, "r") as f:
    puzzle_input = f.read()

  rock_sequence = []

  rock_sequence.append([[2,0],[3,0],[4,0],[5,0]]) # minus
  rock_sequence.append([[2,-1],[3,-1],[4,-1],[3,-2],[3,0]]) # plus
  rock_sequence.append([[2,0],[3,0],[4,0],[4,-1],[4,-2]]) # reverse L
  rock_sequence.append([[2,0],[2,-1],[2,-2],[2,-3]]) # stick
  rock_sequence.append([[2,0],[2,-1],[3,0],[3,-1]]) # rock

  # if move takes piece out of bounds/collides:
  #   if down:
  #     add piece and break
  #   else:
  #     do not move piece, continue to next move

  rocks = defaultdict(set)

  for i in range(7):
    rocks[0].add(i)

  def is_valid_move(shape, direction, fallen_rocks, vertical_accumulation, horizontal_accumulation):
    for x,y in shape:
      if direction == '>':
        right_x = x + 1 + horizontal_accumulation
        if right_x > 6 or (y + vertical_accumulation in fallen_rocks and right_x in fallen_rocks[y + vertical_accumulation]):
          return False
      elif direction == '<':
        left_x = x - 1 + horizontal_accumulation
        if left_x < 0 or (y + vertical_accumulation in fallen_rocks and left_x in fallen_rocks[y + vertical_accumulation]):
          return False
      elif direction == 'v':
        if y + 1 + vertical_accumulation in fallen_rocks and x + horizontal_accumulation in fallen_rocks[y + 1 + vertical_accumulation]:
          return False
    return True

  gas_index = 0
  highest_rock = 4

  last = 0

  for i in range(total_falling_rocks):

    highest_rock = max(highest_rock, abs(min(rocks)) + 4)

    horizontal_accumulation = 0
    vertical_accumulation = -highest_rock

    while True:
      horizontal_direction = puzzle_input[gas_index % len(puzzle_input)]
      
      if is_valid_move(rock_sequence[i % len(rock_sequence)], horizontal_direction, rocks, vertical_accumulation, horizontal_accumulation):
        horizontal_accumulation += 1 if horizontal_direction == '>' else -1
      
      gas_index += 1

      if not is_valid_move(rock_sequence[i % len(rock_sequence)], 'v', rocks, vertical_accumulation, horizontal_accumulation):
        break

      vertical_accumulation += 1
    
    for x,y in rock_sequence[i % len(rock_sequence)]:
      rocks[y + vertical_accumulation].add(x + horizontal_accumulation)

      # found new floor
      if total_falling_rocks == 5000 and len(rocks[y + vertical_accumulation]) == 7:
        print(i, i-last)
        last = i

  return abs(min(rocks))

  # logger
  # for i in sorted(rocks.keys()):
  #   if i == 0:
  #     print(['=' for j in range(7)])
  #   else:
  #     print(['@' if j in rocks[i] else '.' for j in range(7)])

p1 = day17('input.txt', 2022)
print("p1", p1)

print('cycle detection')
day17('input.txt', 5000)

h1 = day17('input.txt', 153)
h2 = day17('input.txt', 1893)

# height accumulated for 1 cycle
height_diff = h2 - h1
# rocks in a cycle
rock_diff = 1893 - 153

remainder = (1000000000000 - 153) % rock_diff
quotient = (1000000000000 - 153) // rock_diff

print("p2", height_diff * quotient + day17('input.txt', 153 + remainder))