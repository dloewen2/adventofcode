import csv
import re

result = 0

regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
valueMap = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four":4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

with open('input.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    regexMatches = re.findall(regex, row[0])
    if len(regexMatches) > 1:
      indexLast = len(regexMatches) - 1
      firstDigit = regexMatches[0] if regexMatches[0].isnumeric() else valueMap.get(regexMatches[0])
      lastDigit = regexMatches[indexLast] if regexMatches[indexLast].isnumeric() else valueMap.get(regexMatches[indexLast])
      result += int(str(firstDigit) + str(lastDigit))
    else:
      foundNumber = regexMatches[0] if regexMatches[0].isnumeric() else valueMap.get(regexMatches[0])
      result += int(str(foundNumber) + str(foundNumber))
    
print(result)
