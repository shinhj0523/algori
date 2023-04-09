import itertools 

def solution(numbers):

    aa = list(map(str,numbers)) 
    result = list(itertools.permutations(aa,len(aa)))


    result = [list(result[x]) for x in range(len(result))]
    re = []

    for i in range(len(result)):
        
        re.append(''.join(result[i]))
        int_list = list(map(int, re))
        int_list.sort()

    return int_list[-1]

print(solution([3, 30, 34, 9, 5]))
