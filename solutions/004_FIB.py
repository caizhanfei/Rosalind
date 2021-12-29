n = 33
k = 4


def getCount(n):
    if n == 1 or n == 2:
        return 1
    return getCount(n-1)+getCount(n-2)*k


print(getCount(n))
