n = int(input("Enter number of array element: "))

arr = [] 

for i in range(0,n):
    ele = int(input(f"Enter element {i+1} : "))

    arr.append(ele)

print(arr)


result = []
zero =0 
for i in arr:
        if i == 0:
            zero = zero + 1
            

        else:
            result.append(i)

for i in range(zero):
    arr.append(0)

print(arr)
