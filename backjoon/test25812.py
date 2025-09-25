import sys
input = sys.stdin.readline

n, r = map(int, input().split())

scores = [int(input()) for _ in range(n)]
fixed = sum(1 for s in scores if r > s)
double = sum(1 for s in scores if r < s)

if fixed > double:
    print(1)
elif fixed < double:
    print(2)
else:
    print(0)