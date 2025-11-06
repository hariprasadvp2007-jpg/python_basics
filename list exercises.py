num_list = []
n = int(input("Enter the value of n: "))

for i in range(n):
    num = int(input("Enter num: "))
    num_list.append(num)

large = num_list[0]
small = num_list[0]

for x in range(1, n):
    if num_list[x] > large:
        large = num_list[x]
    if num_list[x] < small:
        small = num_list[x]

print(f"The largest number is {large} and the smallest number is {small}")



