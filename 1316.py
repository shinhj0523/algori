N = int(input() )
result = N
for i in range(0, N):
    words = input()
    for j in range(0, len(words)-1 ):
        if words[j] == words[j+1]:
            pass
        elif words[j] in words[ j+1: ]:
            result -= 1
            break
print(result)