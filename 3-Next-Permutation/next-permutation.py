def permute(arr):
    n=len(arr)
    # get position of pivot
    for i in reversed(range(n-1)):
        if arr[i] < arr[i+1]:
            break
    else:
        arr[:] = reversed(arr[:])
        return arr
    # get position of next candidate
    for j in reversed(range(i,n)):
        if arr[i] < arr[j]:
            #candidate found, swap
            arr[i], arr[j] = arr[j], arr[i]
            #reverse longest decreasing sequence
            arr[i+1:] = reversed(arr[i+1:])
    return arr

print(permute(list('FADE')))