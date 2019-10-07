from functools import lru_cache 

@lru_cache(maxsize=100)
def fibbo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)







for i in range(1,1001):
    print("first hunderd numbers: ", fibbo(i))
