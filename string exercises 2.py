# Write a program to count the number of words in a sentence

# The punctuations are found in string module
import string
sentence = input("Enter a sentence: ")

# Replace all punctuation with ' '
for i in string.punctuation:
    sentence = sentence.replace(i, " ")

# Split the cleaned sentence into list of words
words = sentence.split()

# Display the word count
print(len(words))









