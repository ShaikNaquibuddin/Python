def linearsearch(A, key):
    for i, j in enumerate(A):
        if(j == key):
            return i+1
    return -1

#main code
A = []
for _ in range(int(input())):
    A.append(input())

key = input()

x = linearsearch(A, key)

print(f"Element {key} found at {x}" if(x != -1) else "Element Not Found")           
