text = " Hello World! "

print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("World", "Python"))
print(text.find("World"))
print(text.count("o"))

words = text.strip().split()
print(words)
print("-".join(words))
