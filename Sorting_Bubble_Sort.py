
def countSwaps(a):
    length = len(a)
    total_swap = 0
    for i in range(length-1):
        swaps = 0
        for j in range(length-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swaps += 1

        total_swap += swaps

        if swaps == 0:
            break

    print('Array is sorted in {} swaps.'.format(total_swap))
    print('First Element:',a[0])
    print('Last Element:',a[-1])

n = int(input())
a = list(map(int, input().rstrip().split()))
countSwaps(a)
