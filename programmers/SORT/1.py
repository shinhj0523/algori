array = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
i = command[0][0]
j = command[0][1]
k = command[0][2]

for i in range(len(command)):

    firstCut = command[i][0]
    lastCut = command[i][1]
    num = command[i][2]
    temp = sorted(array[firstCut-1:lastCut])
    
    print(temp)
# del array[array.index(i-1)]