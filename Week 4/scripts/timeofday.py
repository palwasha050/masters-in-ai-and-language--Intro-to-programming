#Exercise 2 Chapter 10

fname= input("Enter a file name: ")
fileopen= open(fname)

counts=dict()

for line in fileopen:
    if line.startswith("From "):
       words= line.split()
       time=words[5]
       hour=time.split(":")[0]
       counts[hour]=counts.get(hour,0)+1



for key,val in sorted(counts.items()):
    print(key,val)


#lst=[]
#for key,val in counts.items():
#    lst.append((key,val))
      
#lst.sort()
      
#print(lst)
