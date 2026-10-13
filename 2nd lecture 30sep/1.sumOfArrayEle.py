n = int(input("Enter number of array element: "))

arr = [] 

for i in range(0,n):
    ele = int(input(f"Enter element {i+1} : "))

    arr.append(ele)

print(arr)

sum = 0
for j in range(0,n):
    sum = sum + arr[j]
print(f"sum of Array element is : {sum}")

