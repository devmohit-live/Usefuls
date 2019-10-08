# import the cache module
try:
    from functools import lru_cache
except:
    from backports.functools_lru_cache import lru_cache


# lru cache before the function with maxsize= no of items to be cached
@lru_cache(maxsize=1000)
def fab(n):
    if n==1:
        return 1
    if n==2:
        return 1
    elif n>2:
        return fab(n-1)+fab(n-2)


for i in range(1,1002):
    print(i,':',fab(i))

