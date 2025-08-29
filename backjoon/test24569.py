N = int(input())

gold_team = True
count = 0

for _ in range(N):
    points = int(input())
    fouls = int(input())

    stars = points * 5 - fouls * 3

    if stars > 40:
        count += 1
    else:
        gold_team = False

if gold_team:
    print(f"{count}+")
else:
    print(count)