import math
import sys
input = sys.stdin.readline

a, b, h = map(int, input().split())

cnt = max(0, math.ceil((h - a) / (a - b))) + 1
print(cnt)

