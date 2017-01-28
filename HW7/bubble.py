# Bubble Sort Implementation in Python

# numbers is a list
def bubbleSort(numbers): # Bubble Sort Algorithm
    nums = list(numbers)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if numbers[j] < numbers[i]:
                numbers[j], numbers[i] = numbers[i], numbers[j]
        print numbers

    print numbers

if __name__ == "__main__":
	listToSort = [8, 5, 1, 4, 3, 2]

	bubbleSort(listToSort)

'''
# OUTPUT FROM TERMINAL
[1, 8, 5, 4, 3, 2]
[1, 2, 8, 5, 4, 3]
[1, 2, 3, 8, 5, 4]
[1, 2, 3, 4, 8, 5]
[1, 2, 3, 4, 5, 8]
[1, 2, 3, 4, 5, 8]
[1, 2, 3, 4, 5, 8]
'''