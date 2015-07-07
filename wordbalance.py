import string
def dict():
	a = {"A":1}
	p = string.uppercase
	for i in range(2,27):
		a[p[i-1]] = i
	return a

v = dict()


def wordbalance(word):
	a = []
	le=len(word)
	for i in range(0,le):
		a.append(v[word[i]])
	
	for m in range(1,le):
		r = m-1
		k = m+1
		c = 1
		d =1 
		sum1 = 0
		sum2 = 0 
		while r != -1:
			sum1 = sum1 + (a[r]* c)
			c = c+1
			r= r-1
		
		while k != len(a):
			sum2 = sum2 + (a[k] * d)
			d = d+1
			k= k+1
			
		if sum1 == sum2:
			q = m+1
			print word[:m] + " " + word[m] + " " + word[q:] + " - " + str(sum1)
			return 1
	print word + " DOES NOT BALANCE"


		
wordbalance("STEAD")
wordbalance("CONSUBSTANTIATION")
wordbalance("WRONGHEADED")
wordbalance("UNINTELLIGIBILITY")
wordbalance("SUPERGLUE")