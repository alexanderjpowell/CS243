import math

def Algorithm2(numbers, n):
	#print(numbers)
	for i in range(0, n - 1):
		for j in range(i + 1, n - 1):
			if (numbers[j] < numbers[i]):
				tmp = numbers[j]
				numbers[j] = numbers[i]
				numbers[i] = tmp
	#print(numbers)
	if (n % 2 == 1):
		#print("odd")
		#print(int(math.ceil(float(n)/float(2))))
		#print(n)
		#print(float(n))
		#print(int(math.ceil(float(n)/2)))
		#print(numbers[int(math.ceil(float(n)/2))])
		median = numbers[int(math.ceil(float(n)/2)) - 1]
	if (n % 2 == 0):
		#print("even")
		median = numbers[n/2 - 1] + numbers[n/2]
		median = float(median) / 2
	print median


if __name__ == '__main__':
	test = [3,6,2,9,44,100]
	Algorithm2(test, len(test))