
def minimumSwaps(arr):
	swaps = 0

	actual = 0 
	end = len(arr) -1

	while actual < end:
		if arr[actual] != actual +1:
			a = arr[arr[actual] -1]
			arr[arr[actual] -1] = arr[actual]
			arr[actual] = a

			swaps += 1
		else:
			actual += 1

	return swaps

print(minimumSwaps([7, 1, 3, 2, 4, 5, 6])) # 5
print(minimumSwaps([4, 3, 1, 2])) # 3
print(minimumSwaps([2, 3, 4, 1, 5])) # 3
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7])) #3