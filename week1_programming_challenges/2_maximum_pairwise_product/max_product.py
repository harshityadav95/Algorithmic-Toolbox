def maxProdcut(numbers):

	numbers.sort()
	return(numbers[-1]*numbers[-2])





if __name__== "__main__":
    n=int(input())
    input_numbers=[int(x)  for x in input().split()]
    print(maxProdcut( input_numbers))
