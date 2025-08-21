import random


list = ["snake", "water", "gun"]

user_score = 0

computer_score = 0

n = 3
for i in range (1, n+1):

    user_object = input(f"Enter your choice between {list} : ").lower()
    print("User has choosen: ", user_object)
    computer = random.choice(list)
    print("Computer has choosen: ", computer)


    if (user_object == computer):
        print("It's a tie!")
    elif (user_object == "snake" and computer == "water") \
        or (user_object == "gun" and computer == "snake")\
            or(user_object == "water" and computer == "gun"):
        print("Congrats! You have won!!!")
        user_score += 1
    else:
        print("Computer has won!!")
        computer_score += 1

    print(f"Scores after each round: user =>{user_score} | computer => {computer_score}")
print("Game Over!!!")
print(f"Scores after final round: user =>{user_score} | computer => {computer_score}")

if user_score > computer_score:
    print("Congratulations!!! You Won the game")
elif user_score < computer_score:
    print("Computer has won the game")
else:
    print("It is a tie!")