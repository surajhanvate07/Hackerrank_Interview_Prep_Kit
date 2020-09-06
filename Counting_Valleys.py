
def countingValleys(n,s):
    valley = 0
    level = 0
    for i in s:
        if i == 'U':
            level += 1
        else:
            level -= 1

        if i == 'U' and level == 0:
            valley += 1
    return valley

n = int(input())
s = input()
result = countingValleys(n, s)
print(result)
