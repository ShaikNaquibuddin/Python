def binarysearch(A, low, high, key):
    while(low <= high):
        mid = (low + high)//2
        if(A[mid] == key):
            return mid + 1
        elif(A[mid] > key):
            binarysearch(A, low, mid - 1, key)
        else:
            binarysearch(A, mid + 1, high, key)
    return -1
# main code
A = []

for _ in range(int(input())):
    A.append(int(input()))

key  = int(input())

pos = binarysearch(A, 0, len(A)-1, key)

print("Not Found" if(pos < 0) else f"Element {key} found at {pos}")
