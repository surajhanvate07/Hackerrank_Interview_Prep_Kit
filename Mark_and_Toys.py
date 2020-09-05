
def maximumToys(prices, k):
    sm,count=0,0
    prices.sort()
    for i in range(len(prices)):
        if sm + prices[i]<=k:
            sm += prices[i]
            count += 1
        else:
            break
    return count

nk = input().split()
n = int(nk[0])
k = int(nk[1])
prices = list(map(int, input().rstrip().split()))
result = maximumToys(prices, k)
print(result)
