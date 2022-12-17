def touching(head, tail):
  return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def day9():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  part1_tail_positions = set()
  part1_tail_positions.add((0,0))

  head = [0,0]
  tail = [0,0]

  for command in puzzle_input:

    direction, str_distance = command.split(" ")
    distance = int(str_distance)

    for _ in range(distance):

      old_head = [head[0],head[1]]

      # move head
      if direction == 'U':
        head[0] -= 1
      if direction == 'D':
        head[0] += 1
      if direction == 'L':
        head[1] -= 1
      if direction == 'R':
        head[1] += 1

      # tail moving rule:
      # if no longer touching after move, tail moves to old headpos

      if touching(head,tail):
        continue
      
      tail[0] = old_head[0]
      tail[1] = old_head[1]

      part1_tail_positions.add((tail[0], tail[1]))

  print("part1", len(part1_tail_positions))

  #p2

  part2_tail_positions = set()
  part2_tail_positions.add((0,0))

  snake = [[0,0] for _ in range(10)]

  for command in puzzle_input:

    direction, str_distance = command.split(" ")
    distance = int(str_distance)

    for _ in range(distance):
      # move head
      if direction == 'U':
        snake[0][0] -= 1
      if direction == 'D':
        snake[0][0] += 1
      if direction == 'L':
        snake[0][1] -= 1
      if direction == 'R':
        snake[0][1] += 1
      
      for i in range(1, 10):
        if touching(snake[i-1], snake[i]):
          continue
        
        vertical_move = snake[i-1][0] - snake[i][0]
        horizontal_move = snake[i-1][1] - snake[i][1]

        if vertical_move > 0:
          snake[i][0] += 1
        elif vertical_move < 0:
          snake[i][0] -= 1

        if horizontal_move > 0:
          snake[i][1] += 1
        elif horizontal_move < 0:
          snake[i][1] -= 1
      
      part2_tail_positions.add((snake[9][0], snake[9][1]))

  print("part2", len(part2_tail_positions))

day9()