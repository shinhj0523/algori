#스택
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack)==0:
            print(f'-1')
        else:
            print(f'{stack.pop()}')

    elif command[0] == 'size':
        print(f'{len(stack)}')

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(f'1')
        else:
            print(f'0')

    elif command[0] == 'top':
        if len(stack) == 0:
            print(f'-1')
        else:
            print(f'{stack[-1]}')