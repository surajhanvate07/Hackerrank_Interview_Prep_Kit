
def jumpingOnClouds(c):
    length = len(c)
    count = 0
    i = 0
    while i < length-1:
        if i+2 < length and c[i+2] == 0:
            i += 2
            count += 1
        else:
            i += 1
            count += 1
    return count

n = int(input())
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)
print(result)
