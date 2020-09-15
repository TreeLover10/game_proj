#Written by @Anthony Castro-Flores
#Initial Start Date: 9/11/2020
#Last Update/Worked on: 9/15/2020

import random

money = 100

#Game of chance functions:

#Coin flip function:
def coin_flip(choice,bet):
	winning_amount = bet
	losing_amount = -bet
	flip = random.randint(1,2)
	#Check if player has enough money to continue with selected bet: 
	if(bet > money):
		print("Bet exceeds amount of money currently available! Lower bet to continue!\nMoney currently available: $" + str(money) + "\n")
		return False
	#Check if player choice matches what is allowed:
	if(choice != "Heads") and (choice != "Tails"):
		print('Please choose between "Heads" or "Tails" to continue!\n')
		return False
	#Game code:
	if(flip == 1) and (choice == "Heads"):
		print("You won the coin flip!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	elif(flip == 2) and (choice == "Tails"):
		print("You won the coin flip!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	else:
		print("You lost the coin flip!\nAmount lost: $" + str(winning_amount) + "\n")
		return losing_amount
	

#Cho-Han function:
def cho_han(choice, bet):
	winning_amount = bet
	losing_amount = -bet
	dice_one = random.randint(1,6)
	dice_two = random.randint(1,6)
	total = dice_one + dice_two
	#Check if player has enough money to continue with selected bet:
	if(bet > money):
		print("Bet exceeds amount of money currently available! Lower bet to continue!\nMoney currently available: $" + str(money) + "\n")
		return False
	#Check if player choice matches what is allowed:
	if(choice != "Odd") and (choice != "Even"):
		print('Please choose between "Odd" or "Even" to continue!\n' )
		return False
	#Game code:
	if(total%2 == 0) and (choice == "Even"):
		print("You won Cho-Han!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	elif(total%2 != 0) and (choice == "Odd"):
		print("You won Cho-Han!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	else:
		print("You lost Cho-Han!\nAmount lost: $" + str(winning_amount) + "\n")
		return losing_amount

#Card Picker function (This simple ver. will return to update) :
def card_pick(bet):
	winning_amount = bet
	losing_amount = -bet
	player_card = random.randint(1,13)
	ai_card = random.randint(1,13)
	#Check if player has enough money to continue with selected bet:
	if(bet > money):
		print("Bet exceeds amount of money currently available! Lower bet to continue!\nMoney currently available: $" + str(money) + "\n")
		return False
	#Game code:
	if(player_card > ai_card):
		print("You have the higher card! You win!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	elif(player_card < ai_card):
		print("You have the lower card! You lose!\nAmount lost: $" + str(losing_amount) + "\n")
		return losing_amount
	else:
		print("You drew the same card as bot! It's a tie!\nNo money was lost or won!\n")
		return 0 

#Roulette function (Not full simulation or Roulette):
def roulette(choice, bet):
	winning_amount = bet
	losing_amount = -bet
	roulette_spin = random.randint(0,36)
	#Check if player has enough money to continue with selected bet:
	if(bet > money):
		print("Bet exceeds amount of money currently available! Lower bet to continue!\nMoney currently available: $" + str(money) + "\n")
		return False
	#Game code:
	if(choice == "Even") and (roulette_spin%2 == 0) and (roulette_spin != 0):
		print("The number was: " + str(roulette_spin) + "\nResult is even! You won!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	elif(choice == "Odd") and (roulette_spin%2 != 0) and (roulette_spin != 0):
		print("The number was: " + str(roulette_spin) + "\nResult is odd! You won!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	elif(choice == roulette_spin):
		winning_amount *= 35
		print("The number was: " + str(roulette_spin) + "\nYour chosen number matches! You won!\nAmount won: $" + str(winning_amount) + "\n")
		return winning_amount
	else:
		print("The number was: " + str(roulette_spin) + "\nYour choice did not win!\nAmount lost: $" + str(winning_amount) + "\n")
		return losing_amount






#Call your game of chance functions here:

money += coin_flip("Heads", 5)
money += cho_han("Even", 15)
money += card_pick(10)
money += roulette("Odd", 10)
money += roulette(20, 30)

print(money)
