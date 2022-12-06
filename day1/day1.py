from collections import Counter

def day1():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  max_calories = float("-inf")
  cur_calories = 0
  for i in range(len(puzzle_input)):
    if not puzzle_input[i]:
      max_calories = max(max_calories, cur_calories)
      cur_calories = 0
      continue
    cur_calories += int(puzzle_input[i])
  
  print("part1", max_calories)

  calories = Counter()
  elf_num = 0
  for i in range(len(puzzle_input)):
    if not puzzle_input[i]:
      elf_num += 1
      continue
    calories[str(elf_num)] += int(puzzle_input[i])

  top3_calories = 0
  for elf_num, calories in calories.most_common(3):
    top3_calories += calories

  print("part2", top3_calories)

day1()