# Censoring Text

def censor(str,forbidden):
    str=str.split()
    new_str=[]
    for i in str:
        if i not in forbidden:
            new_str.append(i)

    return " ".join(new_str)   #it will join the list elements by adding space in them. 


print(censor("I have a stupid teacher", {"dumb", "stupid"}))