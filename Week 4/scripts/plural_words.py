def plural_word(word):
    vowels_a = "aıou"
    vowels_e = "eiöü"

    for char in reversed(word):
        if char in vowels_a:
            return word + "lar"
        elif char in vowels_e:
            return word + "ler"

def plural_words(words):
    result = []
    for word in words:
        result.append(plural_word(word))
    return result