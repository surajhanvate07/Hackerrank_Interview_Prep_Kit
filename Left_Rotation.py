
def rotLeft(arr,d):
    a = arr[d:] + arr[:d]
    return a

nd = input().split()
n = int(nd[0])
d = int(nd[1])
arr = list(map(int, input().rstrip().split()))
res = rotLeft(arr,d)
print(res)
