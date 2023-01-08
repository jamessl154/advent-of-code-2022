def day15():
  with open("input.txt", "r") as f:
  # with open("example.txt", "r") as f:
    puzzle_input = f.read().split("\n")
  
  num_terminators = set([',', ':'])

  sensors = []
  beacons = []
  
  beacons_y = set()

  for line in puzzle_input:

    sensor = []
    beacon = []
    j = 0
    for i in range(len(line)):
      if line[i] == '=':
        j = i+1
      if line[i] in num_terminators:
        num = int(line[j:i])
        if len(sensor) < 2:
          sensor.append(num)
        else:
          beacon.append(num)
    beacon.append(int(line[j:]))

    beacons_y.add(beacon[1])

    sensors.append(sensor)
    beacons.append(beacon)

  def count_beacon_exclusion_row(y):
  
    # beacons that share row with y
    beacons_sharing_row = set()

    x_ranges_on_row_y = []
    
    for i in range(len(sensors)):

      # diamond height = width
      height = abs(sensors[i][1] - beacons[i][1]) + abs(sensors[i][0] - beacons[i][0])

      if sensors[i][1] - height > y or sensors[i][1] + height < y:
        continue

      # p2 row bounds
      if sensors[i][1] - height > 4000000 or sensors[i][1] + height < 0:
        continue
      
      # p1 col bounds
      if sensors[i][0] - height > 4000000 or sensors[i][0] + height < 0:
        continue

      if beacons[i][1] == y:
        beacons_sharing_row.add(tuple(beacons[i]))

      diff = abs(sensors[i][1] - y)

      # ranges of x on row y where there cannot be a beacon
      x_ranges_on_row_y.append([max(0,sensors[i][0]-height+diff), min(4000000, sensors[i][0]+height-diff)])

    count = 0
    srtd_ranges = sorted(x_ranges_on_row_y)
    start, end = srtd_ranges[0][0], srtd_ranges[0][1]

    if len(srtd_ranges) == 1:
      count += abs(end - start) + 1
    else:
      for i in range(1, len(srtd_ranges)):
        x1, x2 = srtd_ranges[i-1], srtd_ranges[i]

        if x2[0] > end:
          count += abs(end-start) + 1
          start = x2[0]
          print(end+1)
        
        end = max(x2[1], end)
      
      count += abs(end-start) + 1

    return count - len(beacons_sharing_row)

  # y=10 example y=2000000 input
  part1 = 2000000
  print("part1", count_beacon_exclusion_row(part1))

  # part2 answer is some y between 0 and 4000000
  for y in range(4000001):
    res = count_beacon_exclusion_row(y)
    print(y)
    if res != 4000001 and y not in beacons_y:
      print(y) # found y 2628223
      break
  
  count_beacon_exclusion_row(2628223)

  print("part2", 2939043 * 4000000 + 2628223)

  # how many positions cannot contain a beacon? not including current beacons, subtract beacon number after
day15()