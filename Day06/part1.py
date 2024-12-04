raceTimes = []
recordDistances = []
result = 1

def getWinningCombos(time, winningCondition):
    winningCombos = 0
    for counter in range(0, time):
        winningCombos = winningCombos + 1 if (counter * (time - counter)) > winningCondition else winningCombos
    return winningCombos

with open('input.txt', newline='', mode='r') as file:
    raceTimes = list(filter(None, file.readline().split(':')[1].strip().split(' ')))
    recordDistances = list(filter(None, file.readline().split(':')[1].strip().split(' ')))

for counter in range(0, len(raceTimes)):
    result *= getWinningCombos(int(raceTimes[counter]), int(recordDistances[counter]))
    print(result)
    