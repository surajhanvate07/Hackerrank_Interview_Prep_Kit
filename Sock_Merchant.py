
def sockMerchant(n,ar):
    c = 0
    for i in set(ar):
        c += ar.count(i) // 2

    return c

n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)
