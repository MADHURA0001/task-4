import random

def detect_winner( user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user win!"
    else:
        return "user lose!"


def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user = input("Enter rock, paper, or scissors: ").lower()
        if user not in ['rock', 'paper', 'scissors']:
            print("Please choose 'rock', 'paper', or 'scissors'.")
            continue
        

        computer = random.choice(['rock', 'paper', 'scissors'])
        

        result = detect_winner(user, computer)
        print(f"Your choice: {user}")
        print(f"Computer's choice: {computer}")
        print(result)
        
        if result == "user win":
            user_score += 1
        elif result == "user lose":
            computer_score += 1
        
       
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()