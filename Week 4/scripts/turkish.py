def plural_words(lst):
    vowels_a = "aıou"
    vowels_e = "eiöü"
    lst2=[]
    
    for word in lst: 
        for char in reversed(word):
            if char in vowels_a:
               lst2.append(word + "lar")
               break
            elif char in vowels_e:
               lst2.append(word + "ler")
               break
    return lst2

print(plural_words(["deve", "aslan"]))
