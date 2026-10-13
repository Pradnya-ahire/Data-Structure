n = int(input("Enter number of array elements: "))
arr = []


for i in range(0,n):
    ele = int(input(f"Enter {i+1} Ele :"))
    arr.append(ele)

print(arr)

revArr = []
for i in range(0,n):
    temp = arr[i].pop()

    revArr.append(temp)

print(revArr)
