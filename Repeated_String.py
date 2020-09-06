
def repeatedString(s,n):
    total = 0
    for i in s:
        if i == 'a':
            total += 1

    total *= n // len(s)

    for i in s[:n%len(s)]:
        if i == 'a':
            total += 1

    return total

s = input()
n = int(input())
result = repeatedString(s, n)
print(result)
