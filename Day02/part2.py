import csv, re

result = 0

with open('input.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=';')
  for row in reader:
    firstDraw = row[0].split(':')[1]
    del row[0]
    row.insert(0, firstDraw)
    countPossibleCubes = {
      "red": 0,
      "blue": 0,
      "green": 0
    }
    for draw in row:
      for cubes in draw.split(','):
        count = cubes.strip().split(' ')[0]
        color = cubes.strip().split(' ')[1]
        countPossibleCubes[color] = countPossibleCubes[color] if countPossibleCubes[color] > int(count) else int(count)
    result += countPossibleCubes["red"] * countPossibleCubes["green"] * countPossibleCubes["blue"]
print(result)