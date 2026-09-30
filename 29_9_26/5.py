#reverse the array : write a progrma to accept N integer into an array and display the elements in reverse order without changing the original array


n = int(input("how many integers :"))

arr=[]
for i in range(n):
    num = int(input("Enter the integer:"))
    arr.append(num)

rev = arr[::-1]

print(arr)
print(rev)