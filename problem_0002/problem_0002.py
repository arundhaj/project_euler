# fibonacci series generator, which yields only even numbers
def fibonacci(): 
    a, b = 0, 1
    while True:
        if a % 2 == 0:
            yield a
        a, b = b, a + b
        
start = 0
stop = 4000000         
total = 0
f = fibonacci()

while True:
    nextFib = next(f)
    if(nextFib >= stop):
        break
    total += nextFib
    
print total