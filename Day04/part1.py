import re
result = 0
with open('input.csv', newline='', mode="r") as file:
  line = file.readline()
  while line != '':
    info, winningNumbers, usedNumbers = re.split(':|\|', line)
    
    winningNumbers = winningNumbers.strip().split(' ')
    winningNumbers = list(filter(None, winningNumbers))

    usedNumbers = usedNumbers.strip().split(' ')
    currentWin = 0
    for number in usedNumbers:
        if(str.isnumeric(number) and number in winningNumbers):
            currentWin = currentWin * 2 if currentWin > 0 else 1
    result += currentWin
    line = file.readline()
print(result)