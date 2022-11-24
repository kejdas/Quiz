def quiz_game():
    print("Hi, do you wanna start our math Quiz Game?")
    playing = str(input('Only "yes" or "no" :) '))

    if playing == 'yes':
        name = str(input("Cool :), How is your name? "))
        print(f"Nice to meet you {name}, let's start :)")
        counter = 0

        try:
            while playing:
                answer1 = float(input("How much is π: "))
                if answer1 == 3.14:
                    print("That's correct answer!")
                    counter += 1
                    pass
                else:
                    print("That's incorrect answer :(! The answer is 3.14")

                answer2 = float(input("How much is e: "))
                if answer2 == 2.71:
                    print("That's correct answer!")
                    counter += 1
                    pass
                else:
                    print("That's incorrect answer :(! The answer is 2.71")

                answer3 = float(input("How much is √2: "))
                if answer3 == 1.41:
                    print("That's correct answer!")
                    counter += 1
                    pass
                else:
                    print("That's incorrect answer :(! The answer is 1.41")

                answer4 = float(input("How much is Ω: "))
                if answer4 == 0.56:
                    print("That's correct answer!")
                    counter += 1
                    pass
                else:
                    print("That's incorrect answer :(! The answer is 0.56")

                answer5 = float(input("How much is L: "))
                if answer5 == 0.5:
                    print("That's correct answer!")
                    counter += 1
                    break
                else:
                    print("That's incorrect answer :(! The answer is 0.5")
                    break
        except ValueError:
            print("You should pass only float numbers! Start agian!")
            quit()

        print(f"You collect {counter} / 5")

        if 0 < counter <= 2:
            print("You need to practice more")
        if 2 < counter <= 4:
            print(f"Not bad {name}!")
        if counter == 5:
            print(f"Damn! {name} you are beast!")

    elif playing == 'no':
        print("That's sad :( cy@")
        quit()


quiz_game()
