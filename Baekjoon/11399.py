n = int(input())
pi = list(map(int, input().split()))
if(len(pi) == n):
    # 5 - 3 1 4 3 2
    pi.sort()
    sum = 0
    total=0
    for i in range(len(pi)):
        sum = sum + pi[i]
        total = total + sum
    # print(sum)
    print(total)
else:
    print("N and Pi not matched")