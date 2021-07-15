# N, M = map(int, input().split() )
# print("=============")
# if( M == 1 ):  
#     for i in range(1, N+1):
#         print(i)       
# else:
#     for i in range(1, N+1):
#         for j in range(1, M+1):
#             if(i == j):
#                 continue
#             else:
#                 print(f'{i} {j}')


N,M = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s) == M:
        # join :  리스트를 문자열로 일정하게 합쳐주는 함수
        print(' '.join( map(str, s) ) )
        return
    
    for i in range( 1, N + 1 ):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()


n = 4
m = 4
arr = [1,2,3,4]
check = [0, 0, 0, 0]
#idx: arr에서 이전에 선택한 인덱스
#r : 숫자가 선택된 순서
#depth : 선택한 숫자의 개수

def df(idx, r, depth):
    if depth == n:
        print(r)
        return

    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            df(i+1, str(r)+" "+str(arr[i]), depth+1)
            check[i] = 0
df(0, "",0)