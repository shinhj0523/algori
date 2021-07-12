# cash = int(input())

# change = 1000 - cash
# sum = 0
# sum += change//500
# change = change % 500

# sum += change//100
# change = change % 100

# sum += change//50
# change = change % 50

# sum += change//10
# change = change % 10

# sum += change//5
# change = change % 5

# sum += change//1
# change = change % 1
# print(sum)


n = 1000 - int(input() )

sum = 0
coin = [500, 100, 50, 10, 5, 1]
for co in coin:
    sum += n // co
    if n==0:
        break
    n %= co
print(sum)