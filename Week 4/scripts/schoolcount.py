#Chapter 9 exercise 5

fname=input("Enter file name: ")
fopen = open(fname)

dict={}
for lines in fopen:
    if lines.startswith("From "):
       #print(lines)
       words= lines.split()
       mails=words[1]
       #print(mails)
       domain=mails.split("@")[1]
       dict[domain]=(dict.get(domain,0)+1)
print(dict)
