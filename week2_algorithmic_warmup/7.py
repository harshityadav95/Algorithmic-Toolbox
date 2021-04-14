def fibo(n,m):
    counter = 1
    old_num = 0
    new_num = 1
    sum_fib = 1
    tot=0
    while counter < n:
        fib = old_num + new_num
        if counter < n:
            old_num = new_num
            new_num = fib
            sum_fib = sum_fib + fib
            counter = counter + 1
            if(counter>=m):
                tot+=fib
    return (tot)
    
if __name__=="__main__":
    m,n=map(int,input().split())
    print(fibo(n,m))