# Words Overlap 

"using string methods"

'''def words_overlap(str1,str2):
    str1= str1.split(", ")
    str2= str2.split(", ")

    for word in str1:
        if word in str2:
            return True
    return False; 

print(words_overlap("one thing, two things", "one, two, three"))
print(words_overlap("one thing, two things", "two things, monkey"))
'''

"using sets"

def words_overlap(str1,str2):
    str1= set(str1.split(", "))
    str2= set(str2.split(", "))
    #print(str1.intersection(str2))
    if str1.intersection(str2)==set():
        return False
    return True

print(words_overlap("one thing, two things", "one, two, three"))
print(words_overlap("one thing, two things", "two things, monkey"))

