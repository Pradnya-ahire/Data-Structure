n = int(input("Enter number of array elements: "))
arr = []

for i in range(0,n):
    ele = int(input(f"Enter {i+1} Ele :"))
    arr.append(ele)

print(arr)

# smt = arr[0]
# for j in range(1,n):
#     if arr[j]<smt:
#         smt = arr[j]

# print(f"smallest element in the array is: {smt}")


# lrg = arr[0]
# for j in range(1,n):
#     if arr[j]>lrg:
#         lrg = arr[j]

# print(f"Largest element in the array is: {lrg}")


max = arr[0]
min = arr[0]
smax=smin=arr[0]
for num in arr:
    if num > max:
        smax = max
        max = num

    elif(num>smax and num!=max):
        smax = num

    if num < min:
        smin = min
        min = num
    
    elif(num<smin and num!=min):
        smin = num


print("Maximun: ",max)
print("second max: ",smax)

print()

print("Minimum: ",min)
print("second min: ",smin)