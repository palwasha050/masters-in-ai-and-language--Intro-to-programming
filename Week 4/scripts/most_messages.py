#Chapter 9 exercise 4

fname=input("Enter file name: ")
fopen = open(fname)

dict={}
for lines in fopen:
    if lines.startswith("From "):
       print(lines)
       words= lines.split()
       mails=words[1]
       print(mails)
       dict[mails]=(dict.get(mails,0)+1)
#print(dict)

largest=-1
largest_email=None

for email in dict:
    if dict[email]>largest:
        largest=dict[email]
        largest_email=email

print(largest_email,largest)