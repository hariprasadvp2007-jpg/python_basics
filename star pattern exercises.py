# Write a program to construct pattern of stars
# Type 1 :  *                       Type 2 :        *               Type 3 :       *
#           * *                                    * *                            * *
#           * * *                                 * * *                          * * *
#           * * * *                              * * * *                          * *
#           * * * * *                           * * * * *                          *

n = int(input("Enter the number of rows: "))

# Pattern Type 1 :

for i in range(n+1):
    print("* " * i)


print()
# Pattern Type 2 :

for i in range(1, n+1):
    print((n-i) * " ", end = "")
    print(i * "* ")

print()
# Pattern Type 3 : (Only executed when n is odd)

if n % 2 == 1:
    x = ((n//2)+1)
    for i in range(1, n+1):
        if i < x:
            print((x-i) * " ", end = "")
            print(i * "* ")
        elif i == x:
            print(i * "* ")
        else:
            print((i-x) * " ", end="")
            print((2*x-i) * "* ")











