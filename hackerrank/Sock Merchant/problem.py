
def sockMerchant(n, ar):
	ar.sort()
	pairs = 0

	i = 1
	while i < n:
		if ar[i - 1] == ar[i]:
			pairs +=1
			i += 2
		else:
			i += 1

	return pairs



print(sockMerchant(9, [10,20, 20, 10, 10, 30, 50, 10, 20]))