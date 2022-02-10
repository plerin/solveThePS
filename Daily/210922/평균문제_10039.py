

scores = [int(input()) for _ in range(5)]

print(sum(list(map(lambda x: x if x >= 40 else 40, scores)))//len(scores))
