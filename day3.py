import pprint
pp = pprint.PrettyPrinter(indent=4)

f = open("day3.txt", "r")
wires = f.read().splitlines()

firstWire = wires[0].split(',')
secondWire = wires[1].split(',')


def addPositionToDict(position, dict, distance):
  if position[0] in dict.keys():
    dict[position[0]][position[1]] = distance
    return
  else:
    dict[position[0]] = {position[1]: distance}

def changePos(command, pos):
  # Right command
  if command == 'R':
    pos[1] = pos[1] + 1
  #Left command
  elif command == 'L':
    pos[1] = pos[1] - 1
  #Up command
  elif command == 'U':
    pos[0] = pos[0] + 1
  #Down command
  elif command == 'D':
    pos[0] = pos[0] - 1


# Turn the first wire into a dict
firstWireDict = {}
currentPosition = [0, 0]
distanceGone = 0
for command in firstWire:
  amount = int(command[1:])
  direction = command[0]
  for _ in range(amount):
    distanceGone += 1
    changePos(direction, currentPosition)
    addPositionToDict(currentPosition, firstWireDict, distanceGone)

# Turn the second wire into a dict
secondWireDict = {}
currentPosition = [0, 0]
distanceGone = 0
for command in secondWire:
  amount = int(command[1:])
  direction = command[0]
  for _ in range(amount):
    distanceGone += 1
    changePos(direction, currentPosition)
    addPositionToDict(currentPosition, secondWireDict, distanceGone)



#Day 3 part 2
lowestDistance = 999999999999999999 # Just a very high number
# n = x-axis and key = y-axis
for key in firstWireDict.keys():
  #If the key is not in the second dict we don't need to check that
  if key not in secondWireDict:
    #print('skipped key: ', key) # some debug code
    continue
  # Go throuh all the numbers (x values) for the current key (y value) and check if 
  # that x and y value is also in the second wire, where the wires meet
  # If we find the wires intersection (same x and y values) we check if it is the closest
  # to the starting point (distance the wires have traveled combined) so far and if so we 
  # put it in a variable which will show our answer in the end
  for n in firstWireDict[key]:
    if n in secondWireDict[key]:
      #print('dist', firstWireDict[key][n] + secondWireDict[key][n]) # Print distance of 
      #all intersections
      distance = firstWireDict[key][n] + secondWireDict[key][n]
      if distance < lowestDistance:
        lowestDistance = distance
        #print('dist', distance) # print the current lowest distance

print('LOWEST DISTANCE:')
print(lowestDistance)


#Day 3 part 1
'''
lowestDistance = 999999999999999999 # Just a very high number
# n = x-axis and key = y-axis
for key in firstWireDict.keys():
  #If the key is not in the second dict we don't need to check that
  if key not in secondWireDict:
    #print('skipped key: ', key) # some debug code
    continue
  # Go throuh all the numbers (x values) for the current key (y value) and check if 
  # that x and y value is also in the second wire, where the wires meet
  # If we find the wires intersection (same x and y values) we check if it is the closest
  # to the starting point so far and if so we put it in a variable which will show our
  # answer in the end
  for n in firstWireDict[key]:
    if n in secondWireDict[key]:
      distance = n + key
      if distance < lowestDistance:
        lowestDistance = distance
        #print('dist', distance) # print the current lowest distance

print('LOWEST DISTANCE:')
print(lowestDistance)
'''
