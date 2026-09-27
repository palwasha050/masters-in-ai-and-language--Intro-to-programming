#Suffix Replacement

def replace_suffix(word,mapping):

    for key,val in mapping.items():
        if word.endswith(key):
           return word[:-len(key)] + val  
        return word

rules = {"es": "ing", "s": "ing", "ed": "ing"}
for word in ["likes", "sings", "liked", "like", "best", "I"]:
    print(replace_suffix(word, rules))

