import sys
input = sys.stdin.readline

S = input().strip()
ns = "ns"
vowels = "aeiou"
pos1 = max(S.rfind(v) for v in vowels)
pos2 = max(S.rfind(v, 0, pos1) for v in vowels)

res = 1

if not S.endswith(tuple(ns + vowels)):
    res += pos1
else:
    res += pos2

if res <= 0:
    res = -1
print(res)