input = ["AAA","BBB","CCC","DDD"]
answer = []
for i in range(len(input)):
    if i % 2 == 0:
        answer.append(input[i].lower())
    else:
        answer.append(input[i].upper())

print(answer)