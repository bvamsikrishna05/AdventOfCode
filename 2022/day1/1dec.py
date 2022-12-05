#getting the input data

with open('1dec.in') as file:
    data = [i for i in file.read().strip().split("\n")]

    print(data)

    #Travering each string in the input data
    max = 0
    max2 = 0  #Second highest calories 
    max3 = 0  #Third highest calories
    count = 0
    for item in data:
        if item == '':
           count = 0 #reset calorie count
        else:
            num = int(item)
            count += num

        if count > max:
           max = count
        elif count > max2:
             max2 = count
        elif count > max3:
             max3 = count

print ("Puzzle answer Part1:", max)
print ("Puzzle answer Part2:", max+max2+max3)

      