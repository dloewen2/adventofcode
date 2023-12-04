import csv,re
result = 0
with open('input.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    regexMatches = re.findall(r"\d", row[0])
    if len(regexMatches) > 1:
      result += int(int(regexMatches[0] + regexMatches[len(regexMatches) - 1]))
    else:
      result += int(regexMatches[0] + regexMatches[0])
print(result)