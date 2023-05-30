print('dfghjkl')

def fib(n):
    f=0
    s=1
    for x in range(1,n+1):
        yield f
        f,s=s,f+s
x=fib(int(input('enter your fib number')))
print(list(x))
print('this is how we can print fib series')

print('line 3 ')
