
def pairs(arr,k):
    count = 0
    a_set = set(arr)
    for elem in a_set:
        if elem + k in a_set:
            count += 1

    return count

nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
result = pairs(arr,k)
print(result)
