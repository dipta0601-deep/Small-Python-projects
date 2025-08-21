import random

hint1 = "Too High"
hint2 = "Too low"

comp_score = 0
user_score = 0

attempts = 0

while attempts < 3:
    
    user_guess = int(input("Enter the guess: "))
    computer_guess = random.randint(1, 100) #randint picks a random number between mention in the perethesis)
    print("Computer guessed: ", computer_guess)

    if computer_guess == user_guess:
        print("Correct Guess!! Congrats!!")
        user_score += 1
        attempts += 1
    elif computer_guess < user_guess:
        print("Too High!! Try Again!")
        comp_score += 1
        attempts += 1
    else:
        print("Too Low!! Try again")
        comp_score += 1
        attempts += 1

    print(f"attempt: {attempts}")

print(f"score after final rounds: Computer=> {comp_score} | You: {user_score}")

if comp_score > user_score:
    print("Computer Won")

elif comp_score < user_score:
    print("You won! Congrats!!!")