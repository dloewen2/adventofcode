import csv,re
result = 0
leftList, rightList = [], []
with open('input.csv', newline='') as inputfile:
  reader = csv.reader(inputfile)
  for row in reader:
    leftList.append(row[0])
    rightList.append(row[1])
  leftList.sort()
  rightList.sort()

counter = 0
for item in leftList:
  distance = int(item) - int(rightList[counter])
  result += distance if distance >= 0 else distance * -1
  counter += 1
print(result)