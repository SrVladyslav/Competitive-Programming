def climbingLeaderboard(scores, alice):
	scores = list(set(scores))
	scores.sort()
	ind = 0
	rank = []

	s = len(scores)
	for a in alice:
		while(s > ind and a >= scores[ind]):
			ind += 1
		rank.append(s-ind+1)
	return rank


print(climbingLeaderboard([100,90,90,80,75,60], [50,65,77,90,102]))