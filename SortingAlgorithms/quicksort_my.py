def quicksort(A, start, end):
    if(start >= end):
        return
    p = partition(A, start, end)
    quicksort(A, start, p-1)
    quicksort(A, p+1, end)

def partition(A, start, end):
    pivot = A[start]
    i, j = start + 1, end
    while(i<= j):
        while(i<=j and A[i] <= pivot):
            i += 1
        while(i<=j and A[j] >= pivot):
            j -= 1
        if(i<=j):
            A[i], A[j] = A[j], A[i]
    A[start], A[j] = A[j], A[start]
    return j

A = []
for _ in range(int(input())):
    A.append(int(input()))

print("Before Sorting")
print(A)

quicksort(A, 0, len(A)-1)

print("After Sorting")
print(A)
