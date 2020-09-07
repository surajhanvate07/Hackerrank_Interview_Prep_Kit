
def alternatingCharacters(st):
    count = 0
    for i in range(1,len(st)):
        if st[i] == st[i-1]:
            count += 1
    return count

q = int(input())
for i in range(q):
    st = input()
    result = alternatingCharacters(st)
    print(result)
