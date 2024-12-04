with open('input.csv', newline='', mode='r') as file:
    seedInput = file.readline().split(': ')[1].strip('\n').split(' ')
    seeds = seedInput[::2]
    seedLengths = seedInput[1::2]

    mappings = file.read().split('\n\n')
    result = []
    counter = 0
    while counter < len(seeds):
      seed = int(seeds[counter])
      seedCounter = 0
      while seedCounter < int(seedLengths[counter]):
        seedMapping = {
            'seed': int(seed + seedCounter),
            'soil': 0, 
            'fertilizer': 0, 
            'water': 0, 
            'light': 0, 
            'temperature': 0, 
            'humidity': 0, 
            'location': 0
        }

        for mapping in mappings:
            sourceString, destinationString = mapping.split(':')[0].split(' ')[0].split('-to-')
            lines = mapping.split(':')[1].split('\n')
            for line in lines: 
                if(line == ''): continue
                destination, source, length = list(filter(None, line.strip().split(' ')))
                if int(source) <= seedMapping[sourceString.strip()] <= (int(source) + int(length)):
                    seedMapping[destinationString.strip()] = int(destination) + (seedMapping[sourceString.strip()] - int(source))
                    break
                else: 
                    seedMapping[destinationString.strip()] = seedMapping[sourceString.strip()]
        seedCounter += 1
        result.append(int(seedMapping["location"]))

      counter +=1
    print(min(result))