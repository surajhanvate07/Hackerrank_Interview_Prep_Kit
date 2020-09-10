
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    dict1 = Counter(s)
    set1 = set(dict1.values())

    # Same Frequency as set contains only unique values i.e no repetition
    if len(set1) == 1:
        return 'YES'

    # More than two frequencies in a set
    elif len(set1) > 2:
        return 'NO'

    # two unique frequencies
    else:
        for key in dict1:
            dict1[key] -= 1
            temp = list(dict1.values())

            try:
                temp.remove(0)
            except:
                pass

            if len(set(temp)) == 1:
                return 'YES'
            else:
                dict1[key] += 1
        else:
            return 'NO'


s = input()
result = isValid(s)
print(result)
