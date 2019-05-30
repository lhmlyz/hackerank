a = int(input())
b = int(input())

try:
	def calc(a, b):
	    if 1<=a<=10**10 and 1<=b<=10**10:
	        return "{}\n{}\n{}".format(a+b, a-b, a*b)
except:
	print("Invalid char")
print(calc(a,b))