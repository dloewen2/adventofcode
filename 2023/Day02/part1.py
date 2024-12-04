import csv, re

bag = {
  "red": 12,
  "green": 13,
  "blue": 14
}
result = 0

with open('input.csv', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=';')
  for row in reader:
    possible = True
    gameId = re.search(r"\d+", row[0]).group(0)
    firstDraw = row[0].split(':')[1]
    del row[0]
    row.insert(0, firstDraw)
    for draw in row:
      for cubes in draw.split(','):
        count = cubes.strip().split(' ')[0]
        color = cubes.strip().split(' ')[1]
        if int(count) > bag.get(color):
          possible = False
    if possible:
      result += int(gameId)

print(result)