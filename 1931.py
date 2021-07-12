n = int( input() )
Use = []
for _ in range(0, n):
    S, E = map( int, input().split() )
    Use.append((S,E))

Use.sort(key = lambda x: (x[1], x[0]))

# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14


sum = 1
time = 0
i = 0
j = 1
time = Use[i][1]
if(time <= Use[1][i]):
    sum += 1
    time = Use[][1]
