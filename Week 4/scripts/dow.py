#Chapter 9 exercise 2


fname=input("Enter file name: ")
fopen = open(fname)

dict={}
for lines in fopen:
    if lines.startswith("From "):
       #print(lines)
       words= lines.split()
       day=words[2]
       #print(day)
       dict[day]=(dict.get(day,0)+1)
print(dict)


