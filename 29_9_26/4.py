#search an element : write a program to accept N integers into an array and search for a given number . Display an appropriate message indicating whether the number is present in the array or not and also display its position


n = int(input("how many integers :"))
arr = []

for i in range(n):
    num =int(input("Enter an integer :"))
    arr.append(num)

search = int(input("Enter number to search :"))

if search in arr:
    position = arr.index(search)+1
    print("number is present in array :")
    print(position)
else:
    print("number is not present in the array ")