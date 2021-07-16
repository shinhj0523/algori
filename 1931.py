#회의설 배정
n = int( input() )
Use = []
for _ in range(0, n):
    S, E = map( int, input().split() )
    Use.append((S,E))

Use.sort(key = lambda x: (x[1], x[0]))

last = 0
cnt = 0

for i,j in Use:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
