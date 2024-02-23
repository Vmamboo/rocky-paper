import random

def validate():
    while True:
        user_input = input("Please choose 1, 2, or 3. Enter q to quit:\n1) rock \n2) paper \n3) scissors\n")
        if user_input.lower() == "q":
            return None  # Returning None to signal quitting
        if user_input in valid_inputs:
            return user_input
        print("Invalid input! Try again.")

valid_inputs = {"1": "rock", "2": "paper", "3": "scissors"}
user_score = 0
computer_score = 0

while True:
    user_input = validate()
    if user_input is None:
        break  # Break out of the loop if user_input is None (quitting)

    random_number = str(random.randint(1, 3))
    computer_input = valid_inputs[random_number]

    result_message = f"\nYou entered {valid_inputs[user_input]}. Computer entered {computer_input}."

    if valid_inputs[user_input] == computer_input:
        print(f"{result_message} You Tied!\n")
        computer_score += 1
        user_score += 1 
    else:
        user_wins = (valid_inputs[user_input] == "rock" and computer_input == "scissors") or \
                    (valid_inputs[user_input] == "paper" and computer_input == "rock") or \
                    (valid_inputs[user_input] == "scissors" and computer_input == "paper")

        print(f"{result_message} You {'Won' if user_wins else 'Lost'}!\n")
        if user_wins:
            user_score += 1
        else:
            computer_score += 1

print(f"You won {user_score} times. The computer won {computer_score} times.")
