import sys

n = int(input())
a = [int(input()) for _ in range(n)]
stack = []
m = 0
ans = ''
for x in a:
    if x > m:
        while x > m:
            m += 1
            stack.append(m)
            ans += '+\n'
        stack.pop()
        ans += '-\n'
    else:
        if stack[-1] != x:
            print('NO')
            sys.exit(0) # 프로그램을 강제 종료
        stack.pop()
        ans += '-\n'
print(ans, end='')