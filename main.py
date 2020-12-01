import pprint
pp = pprint.PrettyPrinter(indent=4)

f = open("day3.txt", "r")
wires = f.read().splitlines()


firstWire = wires[0].split(',')
secondWire = wires[1].split(',')
#print(firstWire)
#print(secondWire)



def addPositionToDict(position, dict):
  if position[0] in dict.keys():
    dict[position[0]].add(position[1])
  else:
    dict[position[0]] = set()
    dict[position[0]].add(position[1])

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
for command in firstWire:
  #print(command)
  amount = int(command[1:])
  direction = command[0]
  for _ in range(amount):
    changePos(direction, currentPosition)
    addPositionToDict(currentPosition, firstWireDict)

# Turn the second wire into a dict
secondWireDict = {}
currentPosition = [0, 0]
for command in secondWire:
  #print(command)
  amount = int(command[1:])
  direction = command[0]
  for _ in range(amount):
    changePos(direction, currentPosition)
    addPositionToDict(currentPosition, secondWireDict)


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
print('currentPosition', currentPosition)
print('first')
pp.pprint(firstWireDict)
print('second')
pp.pprint(secondWireDict)
'''

