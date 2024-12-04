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
  similarCount = 0
  for rightItem in rightList:
    if int(item) > int(rightItem): continue
    else:
      if int(item) == int(rightItem):
        similarCount += 1
  result += int(item) * similarCount
print(result)