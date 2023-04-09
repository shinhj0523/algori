#동전 0
n, k = map(int, input().split() )
N = []
for i in range(0, n):
    N.append( int(input() ) )
N.reverse()
sum = 0
for i in N:

    sum = sum + k // i  # 420 / 100 
    if n == 0:
        break
    k = k % i
print(sum)