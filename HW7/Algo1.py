def Algorithm1(numbers, n):
	Max = numbers[0]
	Min = numbers[0]
	Sum = 0
	for i in range(0, n):
		if (numbers[i] >= Max):
			Max = numbers[i]
		if (numbers[i] <= Min):
			Min = numbers[i]
		Sum = Sum + numbers[i]
	Mean = float(Sum)/float(n)
	print("Sum: " + str(Sum) + ", n: " + str(n)) 
	print("Mean: " + str(Mean))
	print("Min: " + str(Min))
	print("Max: " + str(Max))

if __name__ == "__main__":
	test = [1,2,3,4,5]
	Algorithm1(test, len(test))