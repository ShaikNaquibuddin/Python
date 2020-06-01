def mergesort(A):
    if(len(A) < 2):
        return
    else:

        mid = (0 + len(A))//2
        left = A[0:mid]
        right = A[mid:]
        mergesort(left)
        mergesort(right)
        merge(left, right, A)

def merge(left, right, A):
    nl, nr, na = len(left), len(right), len(A)
    i, j, k = [0]*3
    while(i<nl and j<nr):
        if(left[i] <= right[j]):
            A[k] = left[i]
            i += 1
            k += 1
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

# main code
A = []
for _ in range(int(input())):
    A.append(int(input()))

print("Before Sorting")
print(A)

mergesort(A)

print("After Sorting")
print(A)
