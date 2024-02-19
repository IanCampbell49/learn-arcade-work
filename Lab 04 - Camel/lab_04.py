import random


def main():

    miles = 0
    thirst = 0
    camel_tiredness = 0
    native_travel_distance = 0
    native_behind = 20
    canteen_drinks = 3

    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.\n")

    done = False

    while done == False:
        print("A.Drink from your canteen.")
        print("B.Ahead moderate speed.")
        print("C.Ahead full speed.")
        print("D.Stop and rest.")
        print("E.Status check.")
        print("Q.Quit.\n")
        user_choice = input("Your choice? ")

        random_natives = random.randint(7, 14)
        random_miles_full = random.randint(10, 20)
        random_miles_half = random.randint(5, 12)
        random_camel = random.randint(1, 3)

        if user_choice == 'Q':
            print("User has quit.")
            done = True
        elif user_choice == 'E':
            print("Miles Traveled: ", miles)
            print("Drinks in canteen:  ", canteen_drinks)
            print("The natives are ", native_behind, " miles behind you.\n")
        elif user_choice == 'D':
            print("The camel is happy.\n")
            camel_tiredness = (camel_tiredness - camel_tiredness)
            native_travel_distance = (random_natives - native_travel_distance)
        elif user_choice == 'C':
            print('You traveled', random_miles_full, 'miles \n')
            miles = (random_miles_full + miles)
            thirst += 1
            camel_tiredness = (camel_tiredness - random_camel)
            native_travel_distance = (native_travel_distance + random_natives)
            native_behind = (miles - (native_behind - native_travel_distance))
            if random.randrange(21) == 0:
                print('You found an oasis!')
                canteen_drinks = 3
                thirst = 0
                camel_tiredness = 0
        elif user_choice == 'B':
            print('You traveled', random_miles_half, 'miles \n')
            miles = (miles + random_miles_half)
            thirst += 1
            camel_tiredness += 1
            native_travel_distance = (random_natives + native_travel_distance)
            if random.randrange(21) == 0:
                print('You found an oasis!')
                canteen_drinks = 3
                thirst = 0
                camel_tiredness = 0
        elif user_choice == 'A':
            if canteen_drinks > 0:
                canteen_drinks -= 1
                thirst = 0
            else:
                print('Out of water')

        if thirst > 3:
            print('##You are thirsty!##')
        if thirst > 5:
            done = True
            print('You have died of thirst')

        if camel_tiredness > 4:
            print('Your camel is getting tired')
        if camel_tiredness > 7:
            print('Your camel is dead!')
            done = True

        if native_travel_distance < 16:
            print('The natives are getting close \n')
        if native_travel_distance < 1:
            print('The natives have caught you!')
            done = True


        if miles > 199:
            if native_travel_distance > 0:
                if camel_tiredness < 8:
                    if thirst < 6:
                        print('You have won the game!')
                        done = True


main()
