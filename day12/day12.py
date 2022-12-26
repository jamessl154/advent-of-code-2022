import heapq

def day12():
  with open("input.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  rows, cols = len(puzzle_input), len(puzzle_input[0])
  directions = [[1,0],[-1,0],[0,1],[0,-1]]

  def height_converter(letter):
    if letter == 'S':
      return 0
    if letter == 'E':
      return 25
    return ord(letter) - ord('a')

  def mindist_to_E(i,j):
    heap = []
    heap.append([0, (i,j)])
    visit = set()

    while heap:
      dist, point = heapq.heappop(heap)
      x, y = point

      if puzzle_input[x][y] == 'E':
        return dist

      for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx == rows or ny < 0 or ny == cols or (nx, ny) in visit:
          continue
        if height_converter(puzzle_input[x][y]) + 1 < height_converter(puzzle_input[nx][ny]):
          continue
        visit.add((nx, ny))
        heapq.heappush(heap, [dist+1, (nx, ny)])
    return float("inf")

  part2 = float("inf")
  for i in range(rows):
    for j in range(cols):
      if puzzle_input[i][j] == 'S':
        part1 = mindist_to_E(i,j)
        part2 = min(part2, part1)
        print("part1", part1)
      if puzzle_input[i][j] == 'a':
        part2 = min(part2, mindist_to_E(i,j))
  print("part2", part2)

  # could optimise by removing all dead ends in the data i.e. islands of a's surrounded by c's

day12()