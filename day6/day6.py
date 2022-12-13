def day6():
  with open("input.txt", "r") as f:
    puzzle_input = f.read()

  print("part1", find_start_packet_from_size(4, {}, puzzle_input))
  print("part2", find_start_packet_from_size(14, {}, puzzle_input))

def find_start_packet_from_size(size, cnt, puzzle_input):
    for i, char in enumerate(puzzle_input):
      if char not in cnt:
        cnt[char] = 0
      cnt[char] += 1
      if i >= size:
        if cnt[puzzle_input[i-size]] == 1:
          del cnt[puzzle_input[i-size]]
        else:
          cnt[puzzle_input[i-size]] -= 1

      if len(cnt) == size:
        return i+1

day6()