
# Some test fails
def repeatedString_1(s, n):			# O(5n + 5)
	rep = 0							# O(1)
	rep1 = 0						# O(1)
	ls = len(s)						# O(1)
	r = n % ls 						# O(1)
	i = 0							# O(1)
	while i < ls:					
		if s[i] ==  'a':			# O(1)
			rep += 1				# O(1)
		if i <= r:					# O(1)
			rep1 += 1				# O(1)
		i += 1						# O(1)
	return (n // ls) * rep + rep1-1	# O(3)

# Good one
def repeatedString(s, n):			# O(4n +5)
	rep = 0							# O(1)
	ls = len(s)						# O(1)
	for i in s
		if i == 'a':				# O(1)
			rep += 1				# O(1)
	rep = rep * (n // ls)			# O(2)

	for i in s[:n % ls]:			
		if i == 'a':				# O(1)
			rep += 1				# O(1)
	return re 						# O(1)

print(repeatedString('aba', 10)) # 7
print(repeatedString('a', 1000000000000)) # 1000000000000