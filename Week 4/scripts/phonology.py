def lacks_nasals(str):
    if "m" in str or "n" in str:
        return False
    else:
        return True


def any_nasals(lst):
    for i in lst:
        if not lacks_nasals(i):
            return True
        return False


print(lacks_nasals("amazing"))
print(lacks_nasals("leaves"))
print(any_nasals(["beet", "root"]))
print(any_nasals(["scam", "letter"]))
