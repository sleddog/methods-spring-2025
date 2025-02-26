import sys



def fizzbuzz(n):
	for i in range(1, n+1):
		if i % 3 == 0 and i % 5 == 0:
			print("BobCat")
		elif i % 3 == 0:
			print("Bob")
		elif i % 5 == 0:
			print("Cat")
		else: 
			print(i)

		
def main():
	number = int(sys.stdin.read().strip())
	
	print("\nOutput: ")
	fizzbuzz(number)



	
main()
	
