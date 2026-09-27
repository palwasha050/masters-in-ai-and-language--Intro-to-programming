numbers = []

while True:

    user_input= input("number")

    if user_input=="done":
        break

    try:
        numbers.append(float(user_input))
    except:
        print("invalid")
