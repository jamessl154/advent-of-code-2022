# credits: https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day25.py

def day25(filename):
  with open(filename, "r") as f:
    puzzle_input = f.read().split("\n")

  def snafuToDecimal(decimalString):
    cur = 0
    power5 = 1
    for i in range(len(decimalString)-1,-1,-1):
      match decimalString[i]:
        case '2':
          cur += 2 * power5
        case '1':
          cur += power5
        case '-':
          cur -= power5
        case '=':
          cur -= 2 * power5
      power5 *= 5
    return cur

  total = 0
  for line in puzzle_input:
    total += snafuToDecimal(line)
  
  output = ''
  while total:
    rem = total % 5
    total //= 5
    if rem <= 2:
      output = str(rem) + output
    else:
      output = '   =-'[rem] + output
      total += 1
  print(output)

# day25('example.txt')
day25('input.txt')