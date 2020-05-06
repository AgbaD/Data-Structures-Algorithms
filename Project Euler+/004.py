#!/usr/bin/python
# Author:	@BlankGodd


class Llp:

	def __init__(self):
		self.main()

	def is_palindrome(self,num):
		x = str(num)
		a = [i for i in x]
		a.reverse()
		c = ''.join(a)
		if x == c:
			return True
		return False
				
	def main(self):
		a =[i for i in range(10_000, 998_001)]
		count = 0
		u = 1
		while True:
			# get palidromes
			num = a[-u]
			if self.is_palindrome(num):
				# get factors
				b = [str(i) for i in range(1, (num//2)+1) if num%i==0]
				for val in b:
					if len(val) == 3:
						count += 1
					if count == 2:
						break
				if count >= 2:
					break
				else:
					count = 0
					u += 1
			else:
				u += 1
		print("The largest palindrome product of two 3-digit numbers is {}".format(a[-u]))


if __name__ == "__main__":
	Llp()

