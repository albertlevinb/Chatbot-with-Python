def greet(bot_name, birth_year):
    """
    Greets the user with the bot's name and birth year.

    Args:
        bot_name (str): The name of the bot.
        birth_year (str): The year the bot was created.
    """
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')

def remind_name():
    """
    Prompts the user to input their name and responds with a compliment.
    """
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')
    return name

def guess_age():
    """
    Asks the user for the remainders of their age when divided by 3, 5, and 7,
    then uses the Chinese Remainder Theorem to guess their age.
    """
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    try:
        rem3 = int(input())
        rem5 = int(input())
        rem7 = int(input())
    except ValueError:
        print("Please enter valid integers.")
        return

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

def programming_quiz():
    """
    Asks the user a series of multiple-choice programming questions.
    Loops until all are answered correctly.
    """
    questions = [
        {
            "question": "Why do we use methods?",
            "options": [
                "1. To repeat a statement multiple times.",
                "2. To decompose a program into several small subroutines.",
                "3. To determine the execution time of a program.",
                "4. To interrupt the execution of a program."
            ],
            "answer": 2
        },
        {
            "question": "What is the output of: print(2 ** 3)?",
            "options": [
                "1. 6",
                "2. 8",
                "3. 9",
                "4. 5"
            ],
            "answer": 2
        },
        {
            "question": "Which data type is used to store True or False?",
            "options": [
                "1. int",
                "2. str",
                "3. bool",
                "4. float"
            ],
            "answer": 3
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        while True:
            try:
                user_answer = int(input())
                if user_answer == q["answer"]:
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("Please, try again.")
                    if score > 0:
                        score -= 1  # Decrement score safely
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"\nFinal Score: {score}/{len(questions)}")
    end()

def end():
    """
    Prints a farewell message to the user.
    """
    print("Thank you for chatting with me 😊")

def main():
    """
    Runs the main sequence of the bot interaction.
    """
    greet('PyAid', '2025')
    name = remind_name()
    guess_age()
    programming_quiz()
    print(f"Goodbye, {name}!")

if __name__ == "__main__":
    main()