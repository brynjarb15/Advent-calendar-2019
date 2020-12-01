f = open("Day1.1.txt", "r")
numbers = f.read().splitlines()

i = 0
for n in numbers:
  numbers[i] = int(n)
  i += 1

#Day 1 part 1
'''
total = 0
for n in numbers:
  n = n // 3
  n = n - 2
  total += n
print(total)
'''

#Day 1 part 2
'''
total = 0
for n in numbers:
  while n > 8:
    n = n // 3
    n = n - 2
    total += n
print(total)
print(numbers)
'''