def count_syllables(word):
    vowels = "aeiouy"
    count = 0
    previous_vowel = False

    for char in word.lower():
        if char in vowels:
            # Count only when a new vowel group starts
            if not previous_vowel:
                count += 1
            previous_vowel = True
        else:
            previous_vowel = False

    return count


def is_monosyllabic(word):
    return count_syllables(word) == 1


def is_disyllabic(word):
    return count_syllables(word) == 2


def has_even_syllables(word):
    return count_syllables(word) % 2 == 0


print(is_monosyllabic("pool"))
print(is_monosyllabic("alphabet"))
print(is_disyllabic("pool"))
print(is_disyllabic("monkey"))
print(has_even_syllables("alphabet"))
print(has_even_syllables("complicated"))