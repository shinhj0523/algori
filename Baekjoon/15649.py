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