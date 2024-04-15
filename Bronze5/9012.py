text = int(input())
for _ in range(text):
    stack = []
    s = input()
    isVPS = True

    for i in s:
        if i == '(':
            stack.append('(')
        if i == ')':
            if stack:
                stack.pop()
            else:
                isVPS = False
                break
    if not stack and isVPS:
        print('YES')
    elif stack or not isVPS:
        print('NO')