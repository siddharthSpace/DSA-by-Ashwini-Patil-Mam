    #        *
    #        *
    #    * * * * *
    #        *
    #        * 
        
        

 
n = int(input("Enter no of rows:"))
mid = (n+1)/2 
for i in range(n):
    for j in range(n):
        if(j==mid or i==mid):
            print("*" , end=" ")
        else:
            print(" ", end=" ")
    print()



# n = int(input("Enter no of rows : "))

# for i in range(n):
#     for j in range(n):
#         if i == n // 2 or j == n // 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
   
       