N = input()
N = [int(n)  for n in N]

M = sorted(N, reverse=True)

for n in M : 
    print(f'{n}', end="")
