#Correction found https://gist.github.com/GuillermoPena/f359216681fd941d4ad8

# Get Fibonacci number n
def nextFibo(n):
    if n<2: return n
    else:   return nextFibo(n-1) + nextFibo(n-2)

def checkio(limit):
    age=0
    lastFibo=1
    indexFibo=2
    opacity=10000
    while opacity!=limit: # While I dont found transparency number...
        age+=1
        if age==lastFibo: # -age if age is a Fibonacci number
            opacity-=age
            indexFibo+=1
            lastFibo=nextFibo(indexFibo)    
        else: # +1 in other case
            if opacity<10000: # Keeping opacity value into the limis
                opacity+=1
    return age
