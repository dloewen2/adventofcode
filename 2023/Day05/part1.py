with open('input.csv', newline='', mode='r') as file:
    seeds = file.readline().split(': ')[1].strip('\r\n').split(' ')
    mappings = file.read().split('\r\n\r\n')
    result = []
    for seed in seeds:
        seedMapping = {
            'seed': int(seed),
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
            lines = mapping.split(':')[1].split('\r\n')
            for line in lines: 
                if(line == ''): continue
                destination, source, length = list(filter(None, line.strip().split(' ')))
                if int(source) <= seedMapping[sourceString.strip()] <= (int(source) + int(length)):
                    seedMapping[destinationString.strip()] = int(destination) + (seedMapping[sourceString.strip()] - int(source))
                    break
                else: 
                    seedMapping[destinationString.strip()] = seedMapping[sourceString.strip()]

        result.append(int(seedMapping["location"]))
    print(min(result))