#프린터 큐

result = 0

t = int(input())
Queue = []
for i in range(t):
    
    # N : 문서의 개수
    # M : 몇 번째로 인쇄되었는지 궁금한 문서가 몇번째에 놓여 있는지
    N, M = map(int, input().split() ) 
    
    #리스트에 우선순위 추가 하기
    for _ in range(N):
        Queue.append(int(input()))


        
    point = M
    while True:
        #리스트 중에 우선순위 제일 높은 인덱스
        P = max(Queue)

        if( P > Queue[0] ):
            Queue.append(Queue.pop(0))
            if point == 0 :
                point = len(Queue) - 1
            else :
                point -= 1
        else:
            if point == 0:
                break
            else:
                result+=1
            Queue.pop(0)
    print(result)
# print(result)
