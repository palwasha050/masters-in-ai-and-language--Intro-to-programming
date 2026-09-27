#this one is only checking number of vowels it has

def count_vowels(word):
    vowels='aeiou'
    count=0
    for char in word:
        if char in vowels:
            count+=1
    return count



def is_monosyllabic(str):
    return count_vowels(str)==0 or count_vowels(str)==1

def is_disyllabic(str):
    return count_vowels(str)==2


def has_even_syllables(str):
    return count_vowels(str) % 2 == 0 


print(is_monosyllabic("pool"))
print(is_monosyllabic("alphabet"))
print(is_disyllabic("pool"))
print(is_disyllabic("monkey"))
print(has_even_syllables("alphabet"))
print(has_even_syllables("complicated"))