#Exercise 1 Chapter 10

fname= input("Enter a file name: ")
fileopen= open(fname)

counts=dict()

for line in fileopen:
    if line.startswith("From "):
       words= line.split()       
       email=words[1]
       counts[email]=counts.get(email,0)+1

lst=[]
for key,val in counts.items():
    lst.append((val,key))

lst.sort(reverse=True)

print(lst[0][1], lst[0][0])

