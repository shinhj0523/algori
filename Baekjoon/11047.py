#동전 0
n, k = map(int, input().split() )
#입력 받을 동전 리스트 생성
N = []
for i in range(0, n):
    # n번 반복해서 입력받기
    N.append( int(input() ) )
#리스트 뒤집기
N.reverse()
sum = 0
for i in N:
    # [50000,10000,5000,1000,500,100,50,10,5,1]
    sum = sum + k // i  # 4200 / 50000 
    if n == 0:
        break
    k = k % i
print(sum)