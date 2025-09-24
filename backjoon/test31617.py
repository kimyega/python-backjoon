from collections import Counter
import sys
input = sys.stdin.readline

K = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

B_counter = Counter(B)
cnt = sum(B_counter[a + K] for a in A)
print(cnt)