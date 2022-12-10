def day4():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  fully_overlapped = 0
  partial_overlap = 0

  for line in puzzle_input:
    elf1, elf2 = line.split(',')

    elf1_l, elf1_r = elf1.split('-')
    elf2_l, elf2_r = elf2.split('-')

    if (int(elf1_l) >= int(elf2_l) and int(elf1_r) <= int(elf2_r)) or (int(elf2_l) >= int(elf1_l) and int(elf2_r) <= int(elf1_r)):
      fully_overlapped += 1
    
    if int(elf2_l) > int(elf1_r) or int(elf1_l) > int(elf2_r):
      continue
    
    partial_overlap += 1

  print("part1", fully_overlapped)
  print("part2", partial_overlap)

day4()