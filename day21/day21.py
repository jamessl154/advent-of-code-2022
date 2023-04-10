from collections import Counter

def day21(filename, p1):
  with open(filename, "r") as f:
    puzzle_input = f.read().split("\n")
    cnt = Counter()
    monkeys = {}

    for line in puzzle_input:
      monkey_name, yell = line.split(': ')
      monkeys[monkey_name] = yell
      
      if not yell.isnumeric():
        l,m,r = yell.split(' ')
        if not l.isnumeric():
          cnt[l] += 1
        if not r.isnumeric():
          cnt[r] += 1
      cnt[monkey_name] += 1
    
    # proof that each monkey is defined once and used once
    for k, v in cnt.items():
      if k != 'root' and v != 2:
        print(k, v)

    def dfs1(monkey):
      if monkeys[monkey].isnumeric():
        return int(monkeys[monkey])
      
      l, sign, r = monkeys[monkey].split(' ')

      if sign == '+':
        return dfs1(l) + dfs1(r)
      elif sign == '-':
        return dfs1(l) - dfs1(r)
      elif sign == '/':
        return dfs1(l) / dfs1(r)
      elif sign == '*':
        return dfs1(l) * dfs1(r)

    # return False if humn in tree or returns number
    def dfs2(monkey):
      if monkey == 'humn':
        return False
      if monkeys[monkey].isnumeric():
        return int(monkeys[monkey])
      
      l, sign, r = monkeys[monkey].split(' ')

      dfs_l, dfs_r = dfs2(l), dfs2(r)

      if not dfs_l or not dfs_r:
        return False
      
      if sign == '+':
        return dfs_l + dfs_r
      elif sign == '-':
        return dfs_l - dfs_r
      elif sign == '/':
        return dfs_l / dfs_r
      elif sign == '*':
        return dfs_l * dfs_r

    if p1:
      print(int(dfs1('root')))
    
    if not p1:
      l, sign, r = monkeys['root'].split(' ')

      dfs_l, dfs_r = dfs2(l), dfs2(r)
      res = dfs_r if dfs_l == False else dfs_l
      node = r if dfs_r == False else l

      while True:
        l, sign, r = monkeys[node].split(' ')
        dfs_l, dfs_r = dfs2(l), dfs2(r)
        node = r if dfs_r == False else l
        num = dfs_r if dfs_l == False else dfs_l

        if l == 'humn' or r == 'humn':
          print('p2', l if dfs_l == False else dfs_l, sign, r if dfs_r == False else dfs_r, '=', int(res))
          break
        
        if sign == '+':
          res -= num
        elif sign == '*':
          res /= num
        elif sign == '-':
          if dfs_l == num:
            res = num - res
          else:
            res += num
        elif sign == '/':
          if dfs_l == num:
            res = num / res
          else:
            res *= num

day21('example.txt', True)
day21('input.txt', True)

day21('example.txt', False)
day21('input.txt', False)