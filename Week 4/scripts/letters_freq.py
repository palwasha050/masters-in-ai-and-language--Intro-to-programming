#Exercise 3 Chapter 10

fname = input("Enter file: ")

try: 
   fopen = open(fname)
except:
   print("file cannot be opened", fname)
   quit()


letters = dict()

for line in fopen:
   line=line.lower()

   for char in line:
      if char.isalpha():
        letters[char]=letters.get(char,0)+1


lst=[]
for key,val in letters.items():
    lst.append((val,key))

lst.sort(reverse=True)

for val,key in lst:
   print(key,val)
