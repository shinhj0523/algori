num1, num2 = (map(str, input().split()))
a = list(num1)
b = list(num2)

# list_1 = list(reversed(num1)) 

A = list(reversed(a))
B = list(reversed(b))

# print(A,B)

result1 = ''.join(A)
result2 = ''.join(B)

# print(result1, result2)

if(result1> result2):
    print(result1)
else:
    print(result2)