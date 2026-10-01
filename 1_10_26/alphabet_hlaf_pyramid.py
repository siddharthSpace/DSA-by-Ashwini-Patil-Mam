#    A
#    A  B
#    A  B  C
#    A  B  C  D




n = int(input("Enter the number of rows :"))
for i in range(n):
    for j in range(i):
        print(chr(65+j ), end=" ")
    print()