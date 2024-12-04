import re

result = 0
regex = r"\d+"
gear = r"\*"

def getLineNumbers(row):
  result = []
  numberMatches = re.finditer(r"\d+", str(row))
  for match in numberMatches:
    matchedNumber = {
      "number": 0,
      "start": 0,
      "end": 0
    }
    matchedNumber["number"] = row[match.span()[0]:match.span()[1]]
    matchedNumber["start"] = match.span()[0]
    matchedNumber["end"] = match.span()[1]
    result.append(matchedNumber)
  return result

def findAdjacentNumbers(gearPos, upperLine, middleLine, lowerLine):
  foundNumbers = []
  # numbersUpper = getLineNumbers(upperLine)
  # numbersMiddle = getLineNumbers(middleLine)
  # numbersLower = getLineNumbers(lowerLine)

  number= {
    "number": 0,
    "start": 0,
    "end": 0
  }
  # Check upperLine
  # Check middleLine
  if any(char.isnumeric() for char in middleLine[gearPos[0] - 1 if gearPos[0] > 0 else gearPos[0] : gearPos[1] + 1]):
    print(gearPos)
  # Check lowerLine

with open('input.txt', newline='', mode="r") as file:
  upperLine = file.readline()
  middleLine = file.readline()
  lowerLine = file.readline()

  positions = re.finditer(gear, middleLine)
  for gear in positions:
    findAdjacentNumbers(gear.span(), upperLine, middleLine, lowerLine)

print(result)