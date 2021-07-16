# Alpa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# S = input()
# list(S)
# sum=[0 for i in range(26)]

# for s in S:
#     for i in Alpa:
#         if( s == i ):
#             sum[Alpa.index(s)] += 1
#         else:
#             continue

# print(sum)   

#아스키 코드
S = input()
Alpha = [0]*26
for i in S:
    print(i)
    Alpha[ord(i)-97]+=1
for i in Alpha:
    print(i, end=" ")