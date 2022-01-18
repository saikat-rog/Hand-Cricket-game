import random

yn = input("Do you want to play?(y/n): ")

if yn.lower() == "n":
    print("Successfully exited from the game.")
else:
    turn = random.randint(1,2)
    if turn == 1:
        turn_of = "You"
        turn_on = "Computer"
    else:
        turn_of = "Computer"
        turn_on = "You"



    print(f"\n\n{turn_of} will bat and {turn_on} will ball.\n\n")



    wkt = 0
    run = 0
    while wkt < 1:
        rand = random.randint(1,6)

        user_rand = int(input("\nEnter your run: "))
        print(f"Your run {user_rand} and Computer's run {rand} ")
        if rand == user_rand:
            print(f"\nShame...{turn_of} out!!!")
            wkt = wkt + 1
            print(f"Total run: {run}| Total wicket: {wkt}")
        else:
            run = run + user_rand
            print(f"Total {turn_of} run: {run}| Total wicket: {wkt}")

    print(f"\n{turn_of}: Total {run} run in {wkt} wicket")



    print(f"\n\n{turn_on} will bat and {turn_of} will ball.\n\n")



    wkt2 = 0
    run2 = 0
    while wkt2 < 1:
        rand = random.randint(1,6)

        user_rand = int(input("Enter your run: "))
        print(f"Your run {user_rand} and Computer's run {rand} ")
        if rand == user_rand:
            print(f"\nShame...{turn_on} out!!!")
            wkt2 = wkt2 + 1
            print(f"Total run: {run2}| Total wicket: {wkt2}")
        else:
            run2 = run2 + rand
            print(f"Total {turn_on} run: {run2}| Total wicket: {wkt2}")

    print(f"\n{turn_on}: Total {run2} run in {wkt2} wicket")


    print(f"\nFinal run of {turn_of}: {run}. \n Final run of {turn_on}: {run2}.")

    if run > run2:
        print(f"\n\n{turn_of} winner!!!")
    else:
        print(f"\n\n{turn_on} winner!!!!")