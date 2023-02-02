from heapq import heappush, heappop
from functools import lru_cache
import collections

def day16():
  with open("input.txt", "r") as f:
  # with open("example.txt", "r") as f:
    puzzle_input = f.read().split("\n")

  class Valve:
    def __init__(self, flow_rate, on, num):
      self.flow_rate = flow_rate
      self.on = on
      self.num = num
      self.tunnels = []

  valves = {}

  start_valve =  'AA'

  for i in range(len(puzzle_input)):
    first_half, second_half = puzzle_input[i].split(";")

    valve_name = first_half[6:8]

    flow_rate = int(first_half[23:])

    valves[valve_name] = Valve(flow_rate, True if flow_rate == 0 else False, i)

    for i in range(len(second_half)):
      if second_half[i].isupper() and second_half[i-1].isspace():
        valves[valve_name].tunnels.append(second_half[i:i+2])

  p1_time = 30

  memo = {}
  def dfs1(valve_name, rate, time):
    if (valve_name, rate, time) in memo:
      return memo[(valve_name, rate, time)]
    if time == p1_time:
      return 0

    # once all are on, no further optimisations can be made to the route
    if all([v.on for v in valves.values()]):
      return rate * (p1_time - time)

    time += 1

    open_valve = float("-inf")
    if not valves[valve_name].on:
      valves[valve_name].on = True
      open_valve = dfs1(valve_name, rate + valves[valve_name].flow_rate, time)
      valves[valve_name].on = False

    move = float("-inf")

    for tunnel in valves[valve_name].tunnels:
      move = max(move, dfs1(tunnel, rate, time))

    memo[(valve_name, rate, time)] = max(move, open_valve) + rate
    return memo[(valve_name, rate, time)]

  # print('part1 dfs1', dfs1(start_valve, 0, 1))

  # this dfs pathing takes too long because we don't restrict pathing at any point
  # and paths are two-way which gives lots of permutations

  # --------------------------------------

  # shortest path to branch from current node
  # visit set
  # gain of cost of reaching branch from curr node
  # every branch 1x further away is % amount as valuable


  # choose next node to go to from curr node
  # when comparing going to each node and releasing them 1 time, no paths
  

  # until all valves are open
  # calc shortest path to all closed valves from current valve
  # choose optimal path based on total pressure if opened at time t
  # greedy, choose the next best at every step don't look at path


  # make the observation that the solution is moving ASAP to all closed valves and opening them in some order.
  # shortest path between self and all open valves. DFS to find and compare orderings of opening valves
  # which order of openings gives the most pressure at the end?

  # --------------------------------------

  def dfs2(cur_valve, pressure, time_left):

    if all([v.on for v in valves.values()]):
      return pressure
    
    max_pressure = float("-inf")

    visit = set()

    heap = [(0, cur_valve)]

    visit.add(cur_valve)

    # every single node we find using dijkstra's is in the least cost path to cur_valve and is a dfs branch
    while heap:
      cost, valve_name = heappop(heap)

      if valve_name != cur_valve and not valves[valve_name].on:
        valves[valve_name].on = True
        # cost number of minutes to reach valve from cur, opening subtract an extra minute
        new_time_left = time_left-cost-1
        # starts flowing at new_timeleft
        contribution = new_time_left * valves[valve_name].flow_rate
        max_pressure = max(max_pressure, dfs2(valve_name, pressure + contribution, new_time_left))
        valves[valve_name].on = False

      for tunnel in valves[valve_name].tunnels:
        if tunnel not in visit:
          visit.add(tunnel)
          heappush(heap, (cost+1, tunnel))

    return max_pressure
  
  # print("part1 dfs2", dfs2(start_valve, 0, p1_time))

  # finding costs using a heap and visit set for each call could be optimised by
  # creating an adjacency matrix and accessing it at each dfs call

  adj_matrix = [[float("inf")] * len(puzzle_input) for _ in range(len(puzzle_input))]

  for v in valves:
    cur_valve = valves[v].num

    adj_matrix[cur_valve][cur_valve] = 0

    heap = [(0, v)]

    visit = set()
    visit.add(v)

    while heap:
      dist, valve = heappop(heap)
      
      for tunnel in valves[valve].tunnels:

        if tunnel not in visit:
          visit.add(tunnel)
          tunnel_index = valves[tunnel].num
          adj_matrix[cur_valve][tunnel_index] = dist+1
          heappush(heap, (dist+1, tunnel))

  @lru_cache(maxsize=None)
  def dfs3(cur_valve, pressure, time_left):

    if all([valves[v].on for v in valves]) or time_left == 0:
      return pressure
    
    max_pressure = float("-inf")

    start_index = valves[cur_valve].num

    for v in valves:

      if valves[v].on:
        continue

      valves[v].on = True

      dest_index = valves[v].num
      cost = adj_matrix[start_index][dest_index]
      # (cost + 1) is time in minutes to travel to and open valve
      new_time_left = max(0, time_left - (cost + 1))
      # starts flowing once opened
      contribution = new_time_left * valves[v].flow_rate

      max_pressure = max(max_pressure, dfs3(v, pressure + contribution, new_time_left))
      
      valves[v].on = False

    return max_pressure

  print("p1 my solution", dfs3(start_valve, 0, p1_time))

  # credits to: https://github.com/vinnymaker18/adventofcode/blob/main/2022/day16/program.py

  def parse_input_line(line):
      tokens = line.split()
      node = tokens[1]
      outflow_rate = int(tokens[4].split('=')[1][:-1])
      if 'valves' in tokens:
          i = tokens.index('valves')
      else:
          i = tokens.index('valve')

      outgoing_edges = []
      for j in range(i + 1, len(tokens)):
          adj = tokens[j]
          if adj.endswith(','):
              adj = adj[:-1]
          outgoing_edges.append(adj)
      
      return (node, outflow_rate, outgoing_edges)

  N = 0
  node_id_map = dict()
  def gid(node):
      nonlocal N
      if node in node_id_map:
          return node_id_map[node]
      
      node_id_map[node] = N
      N += 1
      return node_id_map[node]
  
  MAXN = 128
  flow_rates = [0] * MAXN
  graph = [[MAXN + 10] * MAXN for _ in range(MAXN)]
  for i in range(MAXN):
      graph[i][i] = 0

  positive_rate_nodes = []
  for line in puzzle_input:
      node, rate, edges = parse_input_line(line)
      flow_rates[gid(node)] = rate
      if rate > 0 or node == 'AA':
          positive_rate_nodes.append(gid(node))
      for adj_node in edges:
          graph[gid(node)][gid(adj_node)] = min(graph[gid(node)][gid(adj_node)], 1)

  M = len(positive_rate_nodes)

  for i in range(N):
      for j in range(N):
          for k in range(N):
              graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


  def simulate(T):
      queue = collections.deque()
      best = collections.defaultdict(lambda: -1)
      
      aa = positive_rate_nodes.index(gid('AA'))

      def add(i, added, v, t):
          if t >= 0 and (best[(i, added, t)] < v):
              best[(i, added, t)] = v
              queue.append((i, t, added, v))
      
      add(aa, 0, 0, T)

      while queue:
          i, t, added, v = queue.popleft()
          if (added & (1 << i)) == 0 and t >= 1:
              flow_here = (t - 1) * flow_rates[positive_rate_nodes[i]]
              add(i, added | (1 << i), v + flow_here, t - 1)
          
          for j in range(M):
              t_move = graph[positive_rate_nodes[i]][positive_rate_nodes[j]]
              if t_move <= t:
                  add(j, added, v, t - t_move)
  
      return best

  best1 = simulate(30)
  print("p1 vinnymaker", max(best1.values()))
  best2 = simulate(26)

  # best => (end_node, mask_turned, time_left) => max_flow
  table = [0] * (1 << M)
  p1_res = 0
  for (i, added, t), vmax in best2.items():
      table[added] = max(table[added], vmax)
      p1_res = max(p1_res, vmax)

  ret = 0
  for mask in range(1 << M):
      # mask from 00000 to 11111 (all visited)
      # mask 11111 mask3 00000, mask 10111 mask3 01000
      mask3 = ((1 << M) - 1) ^ mask # mask3 is the non-intersecting subset to mask, find it if it exists in table and update our maximum of the sum of flow of both sets
      ret = max(ret, table[mask3])
      mask2 = mask
      while mask2 > 0:
          ret = max(ret, table[mask3] + table[mask2])
          # mask 11011 mask2 all non-intersecting subset combinations 10000 01000 11000 e.t.c.
          
          # mask3 01000
          # mask  10111
          # mask2 10111

          # mask2-1
          # mask2-1 10110
          # mask2-1 10101
          # mask2-1 10100
          # mask2-1 10011
          # mask2-1 10010
          # mask2-1 10001
          # mask2-1 10000
          # mask2-1 01111
          # mask2-1 01110

          # mask 10111
          # -= 1 & mask 10110
          # -= 1 & mask 10101
          # -= 1 & mask 10100
          # -= 1 & mask 10011
          # -= 1 & mask 10010
          # -= 1 & mask 10001
          # -= 1 & mask 10000
          # -= 1 & mask 00111
          # -= 1 & mask 00110
          # -= 1 & mask 00101
          # -= 1 & mask 00100
          # -= 1 & mask 00011
          # -= 1 & mask 00010
          # -= 1 & mask 00001
          # -= 1 & mask 00000

          mask2 = (mask2 - 1) & mask

  print("p2 vinnymaker", ret)

day16()