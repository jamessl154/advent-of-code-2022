from collections import defaultdict

def day5():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")

  stack_input = puzzle_input[:8]
  step_input = puzzle_input[10:]

  stacks = defaultdict(list)

  for i in range(len(stack_input)-1,-1,-1):
    for j in range(1,len(stack_input[0]),4):
      if stack_input[i][j] == ' ':
        continue
      stacks[1 + j//4].append(stack_input[i][j])

  for step in step_input:
    commands = []
    i = 0
    while i < len(step):
      if step[i].isnumeric():
        if i+1 < len(step) and step[i+1].isnumeric():
          commands.append(int(step[i:i+2]))
          i += 1
        else:
          commands.append(int(step[i]))
      i += 1

    cur = []
    for _ in range(commands[0]):

      # part1
      # stacks[commands[2]].append(stacks[commands[1]].pop())

      # part2
      cur.append(stacks[commands[1]].pop())
    
    while cur:
      stacks[commands[2]].append(cur.pop())

  ans = []
  for key in stacks:
    ans.append(stacks[key][-1])
  print ("".join(ans))

day5()