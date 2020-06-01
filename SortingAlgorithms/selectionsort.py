def selectionsort(A):
    for i in range(0, len(A)-1):
        minindex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minindex]:
                minindex = j
        if i != minindex:
            A[i], A[minindex] = A[minindex], A[i]

A = []
for _ in range(int(input())):
    A.append(int(input()))

print("Before Sorting")
print(A)

selectionsort(A)

print("After Sorting")
print(A)
