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
	print("Round:",round)
	
	
	
	
	
	play = False
	round++
