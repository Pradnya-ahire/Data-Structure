n = int(input("Enter number of array elements: "))
arr = []


for i in range(0,n):
    ele = int(input(f"Enter {i+1} Ele :"))
    arr.append(ele)

print(arr)


search = int(input("Enter number u want to search: "))

for i in range(0,n):
    if arr[i] == search :
        print(f"Element found...Present at array index arr[{i}]")

    if search not in arr:
        print("Element is not present in the array")
