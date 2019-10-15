def bubleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                swap(arr[i], arr[j])
    return arr 



def swap(a, b):
    if a > b:
        a, b= b, a 





print(bubleSort([8,91,4,3,6]))







