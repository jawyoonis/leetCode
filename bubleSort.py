# O(n^2) AND O(1) SPACE
def bubleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j]= arr[j], arr[i]
    return arr








print(bubleSort([8,91,4,3,6]))
