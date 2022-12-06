#Day 3 Rucksack recognition

from string import ascii_letters

# Getting input data
with open('3dec.in') as file:
    rucksack = [i for i in file.read().strip().split("\n")]

    #print(rucksack)

#iterate the rucksack items
totalSum = 0
for rucksackitems in rucksack:
    #two compartments - half each
    half = len(rucksackitems)//2

    left = set(rucksackitems[:half]) 
    right = set(rucksackitems[half:])

# print (rucksackitems,left,right)
# for key, char in enumerate(ascii_letters):
# print(key,char)

    for prio, char in enumerate(ascii_letters):
      if char in left and char in right:
        totalSum += prio + 1


print("Puzzle answer Part1:", totalSum)

#Part2

totalSum = 0
j = 3
for index in range(0,len(rucksack),3):
    rucksacks = rucksack[index:j]
    j += 3 
    print(rucksacks)

    for prio, char in enumerate(ascii_letters):
      if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
        totalSum += prio + 1


print("Puzzle answer Part2:", totalSum)



