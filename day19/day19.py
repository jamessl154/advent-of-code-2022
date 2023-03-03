from math import ceil

# choice between 4 robots or wait = 5 choices done 24 times
# 5^24 = 59,604,644,775,390,625
# prune branches/ cache branches

# hyper-neutrino https://www.youtube.com/watch?v=H3PSODv4nf0

# optimizations
# 1. progress towards a type of robot rather than checking every t state
# 2. once we reach a maxspend in a round for a given resource, do not build more of that robot

def day19(filename, is_p1):
  with open(filename, "r") as f:
    puzzle_input = f.read().split("\n")
  
  p1 = 0
  p2 = 1

  for i, line in enumerate(puzzle_input if is_p1 else puzzle_input[:3]):

    robot_costs = line.split("robot costs ")[1:]

    maxspend = [0, 0, 0, 0]

    costs = [
      [int(robot_costs[0][0]), 0, 0, 0],
      [int(robot_costs[1][0]), 0, 0, 0],
      [int(robot_costs[2][0]), int(robot_costs[2].split('and ')[1].split(' ')[0]), 0, 0],
      [int(robot_costs[3][0]), 0, int(robot_costs[3].split('and ')[1].split(' ')[0]), 0]
      ]
    
    for robot_cost in costs:
      for j in range(len(robot_cost)):
        maxspend[j] = max(maxspend[j], robot_cost[j])

    def dfs(maxspend, cache, t, robots, resources):
      if t == 0:
        return resources[3]

      key = tuple([t, *robots, *resources])
      if key in cache:
        return cache[key]

      maxval = resources[3] + robots[3] * t

      # find a robot that we can build given our initial state, jump to the new state at new t, +1 robot, new resources
      for i, robot_cost in enumerate(costs):
        # prune branches where we are already at maxspend
        if i != 3 and robots[i] == maxspend[i]:
          continue
        
        canbuild = True
        ttb = 0
        for j, rsrc_req in enumerate(robot_cost):
          if rsrc_req > 0 and robots[j] == 0:
            canbuild = False
            break
          left_to_build = rsrc_req - resources[j]
          if left_to_build > 0:
            ttb = max(ttb, ceil(left_to_build / robots[j]))

        if not canbuild:
          continue
        
        remaining = t - ttb - 1

        if remaining <= 0:
          continue

        robots_ = robots[:]
        robots_[i] += 1

        resources_ = [x + y * (ttb + 1) for x, y in zip(resources, robots)]
        # spend amount required for this robot
        for j in range(len(robot_cost)):
          resources_[j] -= robot_cost[j]

        # throw excess resources, increases number of same keys in cache
        for j in range(3):
          resources_[j] = min(resources_[j], maxspend[j] * remaining)

        # jump to new state
        maxval = max(maxval, dfs(maxspend, cache, remaining, robots_, resources_))

      cache[key] = maxval
      return maxval

    v = dfs(maxspend, {}, 24 if is_p1 else 32, [1, 0, 0, 0], [0, 0, 0, 0])

    p1 += (i + 1) * v
    p2 *= v

  if is_p1:
    print('p1', p1)
  else:
    print('p2', p2)

# day19('example.txt', True)
# day19('input.txt', True)
# day19('example.txt', False)
# day19('input.txt', False)