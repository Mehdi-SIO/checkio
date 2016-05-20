def fibonacci(x):

    List = []
    f = 1
    List.append(f)
    List.append(f) #because the fibonacci sequence has two 1's at first
    while f<=x:
        f = List[-1] + List[-2]   #says that f = the sum of the last two f's in the series
        List.append(f)
    else:
        List.remove(List[-1])  #because the code lists the fibonacci number one past x. Not necessary, but defines the code better
        for i in range(0, len(List)):
            print List[i]  #prints it in series form instead of list form. Also not necessary


fibonacci(100)