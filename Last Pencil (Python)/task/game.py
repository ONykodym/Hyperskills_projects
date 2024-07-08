import random

name1 = "John"
name2 = "Jack"

# Get the initial number of pencils
while True:
    number = input("How many pencils would you like to use: ")
    if not number.isdigit():
        print("The number of pencils should be numeric")
    elif int(number) <= 0:
        print("The number of pencils should be positive")
    else:
        pencils = "|" * int(number)
        while True:
            goes_now = input("Who will be the first (John, Jack): ")
            if goes_now == "John" or goes_now == "Jack":
                print(f"""{pencils}
{goes_now}'s turn:""")
                break
            else:
                print("Choose between 'John' and 'Jack'")
        break


def change_turns(current_player):
    return name2 if current_player == name1 else name1


number = int(number)
while True:
    global remove
    if goes_now == name1:
        remove = input()
        if not remove.isdigit():
            print("Possible values: '1', '2' or '3'")
        elif int(remove) > 3:
            print("Possible values: '1', '2' or '3'")
        else:
            temp_number = number - int(remove)
            if temp_number < 0:
                print("Too many pencils were taken")
            else:
                pass
                if not remove.isdigit():
                    print("Possible values: '1', '2' or '3'")
                elif int(remove) in range(1, 4):
                    number -= int(remove)
                    pencils = "|" * number
                    if number == 0:
                        goes_now = change_turns(goes_now)
                        print(f"{goes_now} won!")
                        break
                    else:
                        goes_now = change_turns(goes_now)
                        print(f"""{pencils}
{goes_now}'s turn:""")
                else:
                    print("Possible values: '1', '2' or '3'")

    elif goes_now == name2:
        if number == 1:
            remove = 1
        elif number % 4 == 0:
            remove = 3
        elif number % 4 == 3:
            remove = 2
        elif number % 4 == 2:
            remove = 1
        else:
            remove = random.randint(1, 3)
        print(remove)
        number -= remove
        pencils = "|" * number
        if number == 0:
            goes_now = change_turns(goes_now)
            print(f"{goes_now} won!")
            break
        else:
            goes_now = change_turns(goes_now)
            print(f"""{pencils}
{goes_now}'s turn:""")
