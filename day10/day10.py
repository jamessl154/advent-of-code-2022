def day10():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  cycle_numbers = set([20,60,100,140,180,220])
  
  signal_strength_sum = 0

  cycle, register = 1, 1

  for command in puzzle_input:
    if command == 'noop':
      cycle += 1
    else:
      _, str_value = command.split(" ")

      cycle += 1

      if cycle in cycle_numbers:
        signal_strength_sum += register * cycle

      cycle += 1

      register += int(str_value)
    
    if cycle in cycle_numbers:
      signal_strength_sum += register * cycle

  print("part1", signal_strength_sum)

  CRT = [[0] * 40 for i in range(6)]

  cycle, register = 0, 1

  for command in puzzle_input:

    row, col = cycle // 40, cycle % 40

    if abs(register - col) <= 1:
      CRT[row][col] = '#'
    else:
      CRT[row][col] = '.'

    if command == 'noop':
      cycle += 1
    else:
      _, str_value = command.split(" ")

      cycle += 1

      row, col = cycle // 40, cycle % 40

      if abs(register - col) <= 1:
        CRT[row][col] = '#'
      else:
        CRT[row][col] = '.'

      cycle += 1

      register += int(str_value)
  
  print("part2")
  for line in CRT:
    print(line)


day10()