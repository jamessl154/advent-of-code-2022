from collections import defaultdict

def day2():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  rules_map = [[3,0,6],[6,3,0],[0,6,3]] # Rock Paper Scissors (RPS) result against RPS

  part1_score = 0

  for i in range(len(puzzle_input)):

    opponent = ord(puzzle_input[i][0]) - ord('A')
    me = ord(puzzle_input[i][2]) - ord('X')

    part1_score += 1 + me
    part1_score += rules_map[me][opponent]

  print("part1", part1_score)

  outcomes = [0,3,6] # outcome score Lose Draw Win (LDW)

  opponent_result_map = [[3,1,2],[1,2,3],[2,3,1]] # maps opponent (RPS) with result (LDW) to give selected score

  part2_score = 0

  for i in range(len(puzzle_input)):

    opponent = ord(puzzle_input[i][0]) - ord('A')
    result = ord(puzzle_input[i][2]) - ord('X')

    part2_score += outcomes[result]
    part2_score += opponent_result_map[opponent][result]

  print("part2", part2_score)

day2()