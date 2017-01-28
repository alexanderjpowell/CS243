'''
summ = 0
n = int(input("Enter a number: "))
for i in range(1, n+1):
	for j in range(1, n+1):
		if (i * j >= n):
			for k in range(1, n+1):
				summ = summ + 1

print("Sum: " + str(summ))
print("n^3: " + str(n ** 3))
'''




summ = 0
n = int(input("Enter a number: "))
for i in range(0, n):
	for j in range(0, i+1):
		for k in range(1, 1 + int(float(n)/float(2 ** j))):
			summ = summ + 1
print("Sum1: " + str(summ))


summ2 = 0
for i in range(0, n):
	for j in range(0, i+1):
		summ2 = summ2 + int(float(n)/float(2 ** j))
print("Sum2: " + str(summ2))









'''
summ2 = 0
for i in range(0, n):
	for j in range(0, i+1):
		summ2 = summ2 + 2 ** (-j)
		#summ2 = summ2 + float(1 / float(2 ** j))
	summ2 = summ2 * n
print("Sum2: " + str(summ2))
'''