import random, math

def Play():
	play_item_options = ["R", "P", "S"]
	play_item_dic={"R": "Rock", "P": "Paper", "S": "Scissors"}#Made to enable displaying players choice
	player_input = input("Choose either of 'R', 'P' or 'S': ").upper()
	if (player_input == "R" or player_input == "P" or player_input == "S"):
		comp_input = random.choice(play_item_options)#choose computer's option
		print("Player (" + play_item_dic[player_input] + ")" + ": CPU (" + play_item_dic[comp_input] + ")")#Display both player's choices.
		result = Decision(player_input, comp_input)
		if (result == True):
			print("Player1 Wins!")
		elif(result == False):
			print("Player2 Wins!")
		else:
			Play()# Since neither true or false is returned, restart the game
	else:
		print("Error!. Input must be one of 'R', 'P' or 'S'.")
		Play()

#Used to decide the outcome of two players. Player1 win returns True, Player2 win returns False and a draw returns None
def Decision(player1, player2):
	if (player1 == player2):
		return# Do not return true or false
	elif (player1 == "R"):
		if (player2 == "S"):
			return True
		else:
			# (player2 == "P")
			return False
	else:
		if (player1 == "S"):
			if (player2 == "R"):
				return False
			else:
				# (player2 == "P")
				return True
		else:# (player1 == "P")
			if (player2 == "R"):
				return True
			else:
				# (player2 == "S")
				return False

Play()