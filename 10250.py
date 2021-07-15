# T = int(input())


# for i in range(1, T+1):
#     H, W, N = map(int, input().split() )
#     for rnum in range(1, W):
#         if (N  > H):
#             N = N - H
#         else:
#             break
#     if( rnum//10 != 1):
#         print(f'{N}0{rnum}') 
#     else:
#         print(f'{N}{rnum}') 
        

t = int(input())

for i in range(t):
    h, w, n = map( int, input().split() )
    num = n // h + 1
    floor = n % h
    if n % h == 0:
        num = n // h
        floor = h
    
    print(f'{floor*100+num}')
