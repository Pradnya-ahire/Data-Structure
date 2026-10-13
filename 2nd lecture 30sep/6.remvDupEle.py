n = int(input("Enter number of array element: "))

arr = [] 


for i in range(0,n):
    ele = int(input(f"Enter {i+1} Ele :"))
    arr.append(ele)


print(arr)

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)
