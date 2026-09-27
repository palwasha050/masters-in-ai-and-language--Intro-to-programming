#Exercise 6 Chapter 8

numbers=[]

while True:
    user_input = input("Enter a number: ")

    if user_input == "done":
       break

    try:
        number=float(user_input)
        numbers.append(number)
    except:
        print("Invalid input")

print("Maximum: " , max(numbers))
print("Minimum" , min(numbers))