import re
result = 0
cards = []

with open('input.csv', newline='', mode="r") as file:
  line = file.readline()
  lineCounter = 1
  while line != '':
    info, winningNumbers, usedNumbers = re.split(':|\|', line)
    winningNumbers = list(filter(None, winningNumbers.strip().split(' ')))
    usedNumbers = list(filter(None, usedNumbers.strip().split(' ')))
    cards.append({"id": lineCounter, "copies": 0, "winNumbers": winningNumbers, "usedNumbers": usedNumbers})
    lineCounter += 1
    line = file.readline()

def getCorrectNumbers(card):
    amountCorrect = 0
    for number in card["usedNumbers"]:
        if str.isnumeric(number) and number in card["winNumbers"]:
            amountCorrect = amountCorrect + 1 
    return amountCorrect

def updateCardCopies(index, amount, cardMultiplier):
    counter = 0
    for i in range(amount):
        cards[index + counter]["copies"] += 1 + cardMultiplier
        counter += 1

for card in cards:
    amount = getCorrectNumbers(card)
    updateCardCopies(card["id"], amount, card["copies"])

for card in cards: 
    result += int(card["copies"] + 1)

print(result)