# Checking if student can enter exam

ans = input("Do you have an medical cause(y / n): ")

if ans == "y":
    print(" You are allowed ")

else:
    at = int(input(" Please enter you attendence "))
    if at>75:
        print("You are allowed")

    else:
        print("You are not allowed")
