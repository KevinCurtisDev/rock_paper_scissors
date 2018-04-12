import random

#Rock #Paper #Scissors

#Promt user for input
player_one = input("Pick Rock, Paper, or scissors: ").lower()

#Get a random integer between 0 and 2 inclusive
ai = random.randint(0,2)

#Set the AI's choice depending on the random integer generated
if ai == 0:
	ai_move = "Rock"
elif ai == 1:
	ai_move = "Scissors"
else:
	ai_move = "Paper"


#Game logic selecting output result based on user and AI choices
if player_one == ai_move:
	print(f"AI chooses {player_one}")
	print("It's a draw! Play again.")
elif player_one == "rock":
	if ai_move == "Scissors":
		print("AI chooses Scissors")
		print("Rock smashes scissors. You win!")
	else:
		print("AI chooses Paper")
		print("Paper wraps rock. AI wins! The Machines are coming :-|")
elif player_one == "paper":
	if ai_move == "Scissors":
		print("AI chooses Scissors")
		print("Scissors cuts paper. AI wins! The Machines are coming :-|")
	else:
		print("AI chooses Rock")
		print("Paper wraps rock. You win!")
elif player_one == "scissors":
	if ai_move == "Paper":
		print("AI chooses Paper")
		print("Scissors cuts paper. You win!")
	else:
		print("AI chooses Rock")
		print("Rock smashes scissors.  AI wins! The Machines are coming :-|")
else:
	print("oops, something went wrong. Must be a glitch in the Matrix!")