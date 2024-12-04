import re

result = 0
regex = r"\d+"
specialCharacters = ['+','*','#','$','%','&','/','=','-','@']

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

def checkNeighborLineForSpecials(row, numbers):
  result = []
  for number in numbers:
    startIndex = number.get('start') - 1 if number.get('start') > 0 else number.get('start')
    endIndex = number.get('end') + 1
    if any(item in row[startIndex:endIndex] for item in specialCharacters):
      result.insert(0, number)
  return result

def checkLineForSpecials(row, numbers):
  result = []
  for number in numbers:
    if specialCharacters.count(row[number.get('start') - 1 if number.get('start') > 0 else number.get('start')]) > 0 or specialCharacters.count(row[number.get('end')]) > 0:
      result.append(number)
  return result

with open('input.txt', newline='', mode="r") as file:
  upperLine = file.readline()
  middleLine = file.readline()
  lowerLine = file.readline()

  numbersUpperLine = getLineNumbers(upperLine)
  # Check the first line if numbers have special characters left or right next to them
  for number in numbersUpperLine:
    if specialCharacters.count(upperLine[number.get('start') - 1 if number.get('start') > 0 else number.get('start')]) > 0 or specialCharacters.count(upperLine[number.get('end')]) > 0:
      result += int(number.get('number'))
      array.append(int(number.get('number')))
      numbersUpperLine.remove(number)
  # Check if the numbers in the first line have adjacent special characters
  foundNumbers = checkNeighborLineForSpecials(middleLine, numbersUpperLine)
  for number in foundNumbers:
    result += int(number.get('number'))
  
  # Check middleLine for adjacent characters in above, below line and next to numbers
  while middleLine != '':
    numbersMiddleLine = getLineNumbers(middleLine)
    foundUpperLineNumbers = checkNeighborLineForSpecials(upperLine, numbersMiddleLine)
    for number in foundUpperLineNumbers:
      result += int(number.get('number'))
      numbersMiddleLine.remove(number)

    foundLowerLineNumbers = checkNeighborLineForSpecials(lowerLine, numbersMiddleLine)
    for number in foundLowerLineNumbers:
      result += int(number.get('number'))
      numbersMiddleLine.remove(number)

    foundMiddleLineNumbers = checkLineForSpecials(middleLine, numbersMiddleLine)
    for number in foundMiddleLineNumbers:
      result += int(number.get('number'))

    upperLine = middleLine
    middleLine = lowerLine
    lowerLine = file.readline()

print(result)