n = int(input())
votes = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    dasom = votes[0]
    others = votes[1:]
    count = 0

    while True:
        max_vote = max(others)
        if dasom > max_vote:
            break
        max_idx = others.index(max_vote)
        others[max_idx] -= 1
        dasom += 1
        count += 1

    print(count)
