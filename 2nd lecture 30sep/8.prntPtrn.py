
n = int(input("Enter rows: "))

# for i in range(0,n):
#     for j in range(0,n):
#        if i % 2 == 0 and j %2 !=  0:
#            print("1" ,end = "")

#        else:
#            print("0" ,end = "")

#     print()


mid = (n+1)/2
for i in range(n):
        for j in range(n):
            if j== mid-1 or i == mid-1:
             print("*",end = " ")

            else:
                print(" ",end= " ")

        print()