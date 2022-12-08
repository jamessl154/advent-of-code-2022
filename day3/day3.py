import string

def day3():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  part1_priority_sum = 0

  for rucksack in puzzle_input:
    first_compartment = set()
    for i in range(len(rucksack)):
      if i < len(rucksack) / 2:
        first_compartment.add(rucksack[i])
      elif rucksack[i] in first_compartment:
        part1_priority_sum += priority_summer(rucksack[i])
        break
  
  print("part1", part1_priority_sum)

  part2_priority_sum = 0

  for i in range(0, len(puzzle_input), 3):
    ruckset1, ruckset2 = set(puzzle_input[i]), set(puzzle_input[i+1])

    for j, character in enumerate(puzzle_input[i+2]):
      if character in ruckset1 and character in ruckset2:
        part2_priority_sum += priority_summer(character)
        break
  
  print("part2", part2_priority_sum)

def priority_summer(character):
  if character in string.ascii_lowercase:
    return 1 + ord(character) - ord('a')
  else:
    return 27 + ord(character) - ord('A')

day3()