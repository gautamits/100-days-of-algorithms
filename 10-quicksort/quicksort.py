import random

def swap(data, i, j):
    data[i], data[j] = data[j], data[i]

def qsort3(data, left, right):
    # sorted
    if left >= right:
        return
    # select pivot
    i = random.randint(left, right)
    swap(data, left, i)
    pivot = data[left]
    # i ~ points behind left partition
    # j ~ points ahead of right partition
    # k ~ current element
    i, j, k = left, right, left + 1
    # split to [left] + [pivot] + [right]
    while k <= j:
        if data[k] < pivot:
            swap(data, i, k)
            i += 1
        elif data[k] > pivot:
            swap(data, j, k)
            j -= 1
            k -= 1
        k += 1
    # recursion
    qsort3(data, left, i - 1)
    qsort3(data, j + 1, right)

def qsort(data):
    return qsort3(data, 0, len(data) - 1)
data = [random.randint(1,1000) for i in range(1000)]
qsort(data)
print(data)