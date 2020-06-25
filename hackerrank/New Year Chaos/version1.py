def minimumBribes(q):
    bribes = 0
    con = True
    i = 0

    while i < len(q):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            con = False

        for j in range(q[i]-2,i):
            if q[j] > q[i]:
                bribes += 1
        i += 1

    if con:
        print(bribes)


minimumBribes([2, 1, 5, 3, 4]) # 3
minimumBribes([2, 5, 1, 3, 4]) # Too Chaotic
minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]) # Too chaotic
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) # 7
minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]) # 4