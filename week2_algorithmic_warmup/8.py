def fibo(n):
    counter = 1
    old_num = 0
    new_num = 1
    sum_fib = 1
    while counter < n:
        fib = old_num + new_num
        if counter < n:
            old_num = new_num
            new_num = fib
            sum_fib = sum_fib + (fib**2)
            counter = counter + 1
    return (sum_fib)%10
    
if __name__=="__main__":
    n=int(input())
    print(fibo(n))