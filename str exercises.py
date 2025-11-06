str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
concat = str1 + " " + str2
print(concat)
start = int(input("Enter the starting index of the substring required: "))
end = int(input("Enter the ending index of the substring required: "))
step = int(input("Enter the step size of the substring required: "))
substr = concat[start : end+1 : step]
print(substr)