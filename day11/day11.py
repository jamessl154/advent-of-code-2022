def day11():

  inspections = [0] * 8

  monkeys = {
    0: {
      'items': [91, 58, 52, 69, 95, 54],
      'op': lambda x: x * 13,
      'test': lambda x: monkey_test(x, 7, 1, 5),
    },
    1: {
      'items': [80, 80, 97, 84],
      'op': lambda x: pow(x, 2),
      'test': lambda x: monkey_test(x, 3, 3, 5)
    },
    2: {
      'items': [86, 92, 71],
      'op': lambda x: x + 7,
      'test': lambda x: monkey_test(x, 2, 0, 4)
    },
    3: {
      'items': [96, 90, 99, 76, 79, 85, 98, 61],
      'op': lambda x: x + 4,
      'test': lambda x: monkey_test(x, 11, 7, 6)
    },
    4: {
      'items': [60, 83, 68, 64, 73],
      'op': lambda x: x * 19,
      'test': lambda x: monkey_test(x, 17, 1, 0)
    },
    5: {
      'items': [96, 52, 52, 94, 76, 51, 57],
      'op': lambda x: x + 3,
      'test': lambda x: monkey_test(x, 5, 7, 3)
    },
    6: {
      'items': [75],
      'op': lambda x: x + 5,
      'test': lambda x: monkey_test(x, 13, 4, 2)
    },
    7: {
      'items': [83, 75],
      'op': lambda x: x + 1,
      'test': lambda x: monkey_test(x, 19, 2, 6)
    }
  }

  def monkey_test(worry_level, divisible_by, success, failure):
    if worry_level % divisible_by == 0:
      return success
    return failure

  for _ in range(20): # rounds
    for i in range(8):
      for j in monkeys[i]['items']:
        inspections[i] += 1
        worry_level = monkeys[i]['op'](j) // 3
        destination_monkey = monkeys[i]['test'](worry_level)
        monkeys[destination_monkey]['items'].append(worry_level)
      monkeys[i]['items'] = []

  inspections.sort(reverse=True)
  print("part1", inspections[0] * inspections[1])

  part2_inspections = [0] * 8

  part2_monkeys = {
    0: {
      'items': [91, 58, 52, 69, 95, 54],
      'op': lambda x: x * 13,
      'test': [1, 5],
      'divisible': 7
    },
    1: {
      'items': [80, 80, 97, 84],
      'op': lambda x: pow(x, 2),
      'test': [3, 5],
      'divisible': 3
    },
    2: {
      'items': [86, 92, 71],
      'op': lambda x: x + 7,
      'test': [0, 4],
      'divisible': 2
    },
    3: {
      'items': [96, 90, 99, 76, 79, 85, 98, 61],
      'op': lambda x: x + 4,
      'test': [7, 6],
      'divisible': 11
    },
    4: {
      'items': [60, 83, 68, 64, 73],
      'op': lambda x: x * 19,
      'test': [1, 0],
      'divisible': 17
    },
    5: {
      'items': [96, 52, 52, 94, 76, 51, 57],
      'op': lambda x: x + 3,
      'test': [7, 3],
      'divisible': 5
    },
    6: {
      'items': [75],
      'op': lambda x: x + 5,
      'test': [4, 2],
      'divisible': 13
    },
    7: {
      'items': [83, 75],
      'op': lambda x: x + 1,
      'test': [2, 6],
      'divisible': 19
    }
  }

  # 2,3,5,7,11,13,17,19
  p2_prod_divisible_by = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

  for round_num in range(10000): # rounds
    for i in range(8):
      for j in part2_monkeys[i]['items']:
        part2_inspections[i] += 1
        worry_level = part2_monkeys[i]['op'](j) % p2_prod_divisible_by
        test_index = 0 if worry_level % part2_monkeys[i]['divisible'] == 0 else 1
        destination_monkey = part2_monkeys[i]['test'][test_index]
        part2_monkeys[destination_monkey]['items'].append(worry_level)
      part2_monkeys[i]['items'] = []

  part2_inspections.sort(reverse=True)
  print("part2", part2_inspections[0] * part2_inspections[1])

  example_inspections = [0] * 4

  example_monkeys = {
    0: {
      'items': [79, 98],
      'op': lambda x: x * 19,
      'test': [2, 3],
      'divisible': 23
    },
    1: {
      'items': [54, 65, 75, 74],
      'op': lambda x: x + 6,
      'test': [2, 0],
      'divisible': 19
    },
    2: {
      'items': [79, 60, 97],
      'op': lambda x: pow(x, 2),
      'test': [1, 3],
      'divisible': 13
    },
    3: {
      'items': [74],
      'op': lambda x: x + 3,
      'test': [0, 1],
      'divisible': 17
    }
  }

  example_prod_divisible_by = 23 * 19 * 13 * 17

  for m_round in range(10000): # rounds
    for i in range(4):
      for j in example_monkeys[i]['items']:
        example_inspections[i] += 1
        worry_level = example_monkeys[i]['op'](j) % example_prod_divisible_by
        test_index = 0 if worry_level % example_monkeys[i]['divisible'] == 0 else 1
        destination_monkey = example_monkeys[i]['test'][test_index]
        example_monkeys[destination_monkey]['items'].append(worry_level)
      example_monkeys[i]['items'] = []

  example_inspections.sort(reverse=True)
  print("example", example_inspections[0] * example_inspections[1])

  # part2 inspections without calculating worry levels

  # binary divisible by check https://stackoverflow.com/questions/33084908/verify-divisibility-rules-using-bitwise-operations

  # for each worry level, hold a list of what its divisible by, all numbers are prime
  # i.e. if it passes through monkey 0 the worry level is divisible by 19 until other operations change that

  # modulo of smallest common divisible factor => product

day11()