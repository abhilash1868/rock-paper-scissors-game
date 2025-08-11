import random
Rock = '''
..OOO..
..O..O.
..OOO..
..O.O..
..O..O.'''

papers = '''
..OOO..
..O..O.
..OOO..
..O....
..O....'''

scissors = '''
..OOO..
..O....
..OOO..
....O..
..OOO..'''
game_images = [Rock, papers, scissors]
user_score = 0
computer_score = 0

print("Rock Paper Scissors - First to 3 Wins")

while user_score < 3 and computer_score < 3:
    user_choice = int(input("Enter your choice: type 0 for rock, 1 for paper, 2 for scissors: "))
    print("user choice:")
    if user_choice >= 3 or user_choice < 0:
        print("You are out of the range")
        continue
    else:
        print(game_images[user_choice])
        computer_choice = random.randint(0, 2)
        print("computer chosen:", computer_choice)
        print(game_images[computer_choice])
    if user_choice == computer_choice:
        print("draw")
    elif computer_choice == 0 and user_choice == 2:
        print("computer wins")
        computer_score += 1
    elif user_choice == 0 and computer_choice == 2:
        print("user wins")
        user_score += 1
    elif computer_choice > user_choice:
        print("computer wins")
        computer_score += 1
    elif user_choice > computer_choice:
        print("user wins")
        user_score += 1
        print(f"Score: You {user_score} - {computer_score} Computer\n")
if user_score > computer_score:
    print("You won the match!")
else:
    print("Computer won the match!")
