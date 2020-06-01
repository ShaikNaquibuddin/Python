def bubblesort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

A = []
for _ in range(int(input())):
    A.append(int(input()))

print("Before Sorting")
print(A)

bubblesort(A)

print("After Sorting")
print(A)
