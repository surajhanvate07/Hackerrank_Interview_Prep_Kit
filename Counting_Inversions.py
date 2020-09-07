
def merge(arr,left_part,right_part):
    i=0
    j=0
    k=0
    inversions = 0
    left_length = len(left_part)
    right_length = len(right_part)
    while i < left_length and j < right_length:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            inversions += left_length - i
        k += 1

    while i < left_length:
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < right_length:
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inversions

def mergeSort(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        left_part = arr[:mid]
        right_part = arr[mid:]
        inversions = mergeSort(left_part) + mergeSort(right_part) + merge(arr,left_part,right_part)
        return inversions

    return 0

def countInversions(arr):
    return mergeSort(arr)


arr = list(map(int,input().split()))
result = countInversions(arr)
print(result)
