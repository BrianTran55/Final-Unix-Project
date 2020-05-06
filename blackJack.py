import random

#function to generated a random card
def randCard(deck,cardList):
	randNum = random.randint(0,12)
	theCard = cardList[randNum]
	for i in deck:
		if i == theCard:
			return deck[i]


print("*****Welcome To Black Jack*****")
print("RULES:")
print("1) The player and the deal both start with two cards.")
print("2) The player must decide if they want to add another card to their total or stand")
print("3) This is done by typing 'stand' or 'hit'")
print("4) If the player goes over 21 they bust")
print("5) After the player stands, if their total is closer to 21 than the dealer, they win.")
print("6) Number cards are worth face value, Ace is worth 1,picture cards are worth ten")
print(" ")


play = True
#keeps track on round number
round = 1
#dictionary thta holds the cards and their values of a deck
cards = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
#list that holds keys of the cards dictionary
cardL = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
playerCount = 0
dealerCount = 0


#main loop for the game
while(play):
	print("**********************************")
	print("Round:",round)
	
	#generate the hand for the dealer
	dealCount = dealerCount + randCard(cards,cardL)
	dealCount = dealerCount + randCard(cards,cardL)
	
	#make your inital hand
	playerCount = playerCount + randCard(cards,cardL)
	playerCount = playerCount + randCard(cards,cardL)
	
	print("Your inital total is:",playerCount)
	
	choice = input("Will you hit or stand? ")
	
	while choice != "hit" and choice != "stand":
		choice = input("Invalid command. Please enter hit or stand: ")

	while choice == "hit":
		playerCount = playerCount + randCard(cards,cardL)
		print("You total is now:",playerCount)
		
		if playerCount > 21:
			print("You busted!")
			choice = "lose"
		else:
			choice = input("Will you hit or stand? ")
			while choice != "hit" and choice != "stand":
				choice = input("Invalid command. Please enter hit or stand: ")
	
	#compare your total to the dealers
	if choice == "stand":
		print("The dealer's hand was:",dealerCount)
		if playerCount < dealerCount:
			print("Sorry you lost!")
		else:
			print("Congrats you won!")
	

	decision = input("Would you like to play again? [y/n]")
	while decision != "y" and decision != "n":
		decision = input("Invalid command. Please enter y or n")
	
	if decision == "n":
		print("Thanks for playing")
		play = False
	else:
		playerCount = 0
		dealerCount = 0
		play = True
		round+=1
	
