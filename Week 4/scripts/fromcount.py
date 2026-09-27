#Exercise 5 Chapter 8

fname= input("Enter a file name: ")
fileopen= open(fname)

count=0

for line in fileopen:
    if line.startswith("From "):
       words= line.split()
       #print(words[1])
       count=count+1
    

print("There were",count, "lines in the file with From as the first word")