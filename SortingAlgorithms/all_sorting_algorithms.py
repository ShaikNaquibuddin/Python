# ==============================================================================
# selection sort

def selectionsort(A):
    low, high = 0, len(A) -1 
    for i in range(low, high):
        minindex = i
        for j in range(i+1, high+1):
            if A[j] < A[minindex]:
                minindex = j
        if minindex != i:
            A[i], A[minindex] = A[minindex], A[i]
# ===========================================================================
# bubble sort

def bubblesort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
# ==========================================================================
# quick sort

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
# ================================================================
# insertion sort

def insertionsort(A):
    for i in range(1, len(A)):
        value = A[i]
        hole = i
        while(hole > 0 and A[hole -1] > value):
            A[hole] = A[hole - 1]
            hole = hole - 1
        A[hole] = value
# =====================================================================
# merge sort

def mergesort(A):
    if(len(A) < 2):
        return
    else:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        mergesort(left)
        mergesort(right)
        merge(left, right, A)

def merge(left, right, A):
    nl, nr, n = len(left), len(right), len(A)
    i, j, k = [0]*3
    while(i<nl and j<nr):

        if(left[i] <= right[j]):
            A[k] = left[i]
            k += 1
            i += 1

        elif(right[j] < left[i]):
            A[k] = right[j]
            j += 1
            k += 1
    while(i < nl):
        A[k] = left[i]
        i += 1
        k += 1
    while(j < nr):
        A[k] = right[j]
        j += 1
        k += 1
# =====================================================================
# main code

A = []

for _ in range(int(input())):
    A.append(int(input()))

print("Before Sorting")
print(A)
print()

print("1.Selection Sort\n2.Bubble Sort\n3.Insertion Sort\n4.Quick Sort\n5.Merge Sort\n6.Heap Sort")
op = int(input("Enter option : "))

if(op == 1):
    selectionsort(A)
elif(op == 2):
    bubblesort(A)
elif(op == 3):
    insertionsort(A)
elif(op == 4):
    quicksort(A, 0, len(A)-1)
elif(op == 5):
    mergesort(A)
elif(op == 6):
    pass
else:
    print("Invalid Input")
    exit()

print()
print("After Sorting")
print(A)
# ===================================================================
