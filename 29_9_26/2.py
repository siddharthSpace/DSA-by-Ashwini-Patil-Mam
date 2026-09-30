

n = int(input("How many integers? "))

arr = []
for i in range(n):
    number = int(input("Enter an integer: "))
    arr.append(number)

arr = sorted(set(arr))

if len(arr) < 2:
    print("Enter at least two distinct integers.")
else:
    print("Largest :", arr[-1])
    print("Second largest :", arr[-2])
    print("Smallest :", arr[0])
    print("Second smallest :", arr[1])