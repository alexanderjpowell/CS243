def IsPalindrome(word):
	if (len(word) <= 1):
		return True
	first = word[0]
	last = word[len(word) - 1]
	if (first != last):
		return False
	else:
		print "iteration"
		return IsPalindrome(word[1:len(word)-1])



if __name__ == "__main__":
	'''
	print "testing" + " " + str(IsPalindrome("testing"))
	print "testinggnitset" + " " + str(IsPalindrome("testinggnitset"))
	print "aba" + " " + str(IsPalindrome("aba"))
	'''

	print "aaaaaaaaaaaaaaaaaaaa" + " " + str(IsPalindrome("aaaaaaaaaaaaaaaaaaaa"))