import copy


def intcode(numb):
  i = 0
  for n in numb:
    if i % 4 != 0:
      i += 1
      continue
    if n == 99:
      break
    if n == 1:
      first = numb[numb[i+1]]
      second = numb[numb[i+2]]
      numb[numb[i+3]] = first + second
      i += 1
    if n == 2:
      first = numb[numb[i+1]]
      second = numb[numb[i+2]]
      numb[numb[i+3]] = first * second
      i += 1
  #print(numb)

f = open("day2.txt", "r")
numbers = f.read().split(',')


i = 0
for n in numbers:
  numbers[i] = int(n)
  i += 1

print(numbers)
#Day 2 part 1
'''
i = 0
for n in numbers:
  if i % 4 != 0:
    i += 1
    continue
  if n == 99:
    break
  if n == 1:
    first = numbers[numbers[i+1]]
    second = numbers[numbers[i+2]]
    numbers[numbers[i+3]] = first + second
    i += 1
  if n == 2:
    first = numbers[numbers[i+1]]
    second = numbers[numbers[i+2]]
    numbers[numbers[i+3]] = first * second
    i += 1
print(numbers)
'''

#Day 2 part 2
originalNumbers = copy.deepcopy(numbers)
for noun in range(0, 100):
  for verb in range(0, 100):
    numbers = copy.deepcopy(originalNumbers)
    numbers[1] = noun
    numbers[2] = verb
    intcode(numbers)
    if numbers[0] == 19690720:
      print('noun', noun)
      print('verb', verb)
      print(numbers)
   
