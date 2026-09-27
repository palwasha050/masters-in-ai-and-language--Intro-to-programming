items=["bag","apple","cat","pineapple"]
new_list= list()

for word in items:
    new_list.append((len(word),word))

new_list.sort()
print(new_list)

res=list()
for length,word in new_list:
    res.append(word)

print(res) # if you want only word in sorted order