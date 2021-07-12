# P = input()
# sum = 0
# for i in P:
#     if(ord(i)>= 65 and ord(i) <=67):
#         sum += 3
#     elif(ord(i)>= 68 and ord(i) <=70):
#         sum+=4
#     elif(ord(i)>= 71 and ord(i) <=73):
#         sum+=5
#     elif(ord(i)>= 74 and ord(i) <=76):
#         sum+=6
#     elif(ord(i)>= 77 and ord(i) <=79):
#         sum+=7
#     elif(ord(i)>= 81 and ord(i) <=83):
#         sum+=8
#     elif(ord(i)>= 84 and ord(i) <=86):
#         sum+=9
#     else:
#         sum+=10

# print(sum)


words = input()
s = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

time = 0
for i in range(len(words)):
    for j in s:
        if(words[i] in j):
            time += s.index(j) + 3
print(time)
