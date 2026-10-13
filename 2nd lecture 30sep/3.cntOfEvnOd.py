n = int(input("Enter number of array elements: "))
arr = []


for i in range(0,n):
    ele = int(input(f"Enter {i+1} Ele :"))
    arr.append(ele)

print(arr)


even = 0
odd = 0
for i in range(0,n):
    if arr[i] % 2 == 0:
        even += 1

    else:
        odd += 1

print(f"Count of even numbers: {even}")
print(f"count of odd numbers {odd}")

