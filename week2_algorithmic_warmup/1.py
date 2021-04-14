def fibo(number):
    if number<=1:
        return number
    fib_numbers=[]
    for i in range(0,number+1):
        if i<=1:
            current=i
        else:
            current=fib_numbers[i-1]+fib_numbers[i-2]
        fib_numbers.append(current)
    
    return fib_numbers[-1]

if __name__=="__main__":
    n=int(input())
    print(fibo(n))