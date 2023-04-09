num1, num2 = map(int, input().split() )
step1 = (num2 % 100) % 10
step2 = (num2 % 100) // 10 
step3 = num2 // 100
print(num1 * step1)
print(num1 * step2)
print(num1 * step3)
print(num1 * num2)