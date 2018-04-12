#Rock #Paper #Scissors

player_one = input("Pick Rock, Paper, or scissors: ")

player_two = input("Pick Rock, Paper, or scissors: ")

if player_one == player_two:
	print("It's a draw! Play again.")
elif player_one == "Rock":
	if player_two == "Scissors":
		print("Rock smashes scissors. Player one wins!")
	elif player_two == "Paper":
		print("Paper wraps rock. Player two wins!")
elif player_one == "Paper":
	if player_two == "Scissors":
		print("Scissors cuts paper. Player two wins!")
	elif player_two == "Rock":
		print("Paper wraps rock. Player one wins!")
elif player_one == "Scissors":
	if player_two == "Paper":
		print("Scissors cuts paper. Player one wins!")
	elif player_two == "Rock":
		print("Rock smashes scissors. Player two wins!")
else:
	print("oops, something went wrong")