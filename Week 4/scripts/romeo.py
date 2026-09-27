#Exercise 4 Chapter 8

#ask user for file name
fname = input("Enter file: ")

#open file using open
fileopen= open(fname)
words=[]

for line in fileopen:
    line_words=line.split()
    for word in line_words:
        if word not in words:
            words.append(word)

words.sort()
print(words)
