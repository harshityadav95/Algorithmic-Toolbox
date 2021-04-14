def fibo_s(number):
    if number<=1:
        return number
    else:
        
        if number<=60:
            loop=number
        else:
            loop=number%60
        fib_list=[]
        for i in range(0,loop+1):
            if i<=1:
                current=i
            else:
                current=fib_list[i-1]+fib_list[i-2]
            fib_list.append(current)
        return fib_list[-1]%10

if __name__=="__main__":
    n=int(input())
    print(fibo_s(n))