def insertionsort(A, n):
    for i in range(1,n):
        value = A[i]
        hole = i
        while(hole > 0 and A[hole - 1]>value):
            A[hole] = A[hole-1]
            hole = hole - 1
        A[hole] = value

#main code
A = []

for _ in range(int(input())):
    A.append(int(input()))

print("Before Sorting")
print(A)

insertionsort(A, len(A))

print("After Sorting")
print(A)
