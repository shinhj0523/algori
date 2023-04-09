T = int(input())
nList =[]
sList = []
for i in range(0,T):

    N = int(input())
    S = input()       
    nList.append(N)
    sList.append(S)


for i,n in enumerate(nList):
    count = 0
    for j in range(0,n-1):

        if sList[i][j] == sList[i][j+1]:
            continue
        else:
            count += 1
               
    print(count)