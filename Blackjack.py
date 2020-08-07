#Import resources
import random

#Function to work out the total of a players hand
def myFunction(hand):
    counter = 0
    for card in hand:
        if card == "Ace":
            counter = counter + 1
        elif card == "Two":
            counter = counter + 2
        elif card == "Three":
            counter = counter + 3
        elif card == "Four":
            counter = counter + 4
        elif card == "Five":
            counter = counter + 5
        elif card == "Six":
            counter = counter + 6
        elif card == "Seven":
            counter = counter + 7
        elif card == "Eight":
            counter = counter + 8
        elif card == "Nine":
            counter = counter + 9
        elif card == "Ten" or card == "Jack" or card == "Queen" or card == "King":
            counter = counter + 10
        #Checking for 11
        elif card == "Eleven":
            counter = counter + 11
        else:
            counter = counter
    return counter

def aceCheck(hand):
    #Using a for loop to loop through every card in the users hand to see if it is an ace or eleven
    for x in range(len(hand)):
        if hand[x] == "Ace":
            print("You have an Ace, would you like to score 1 or 11")
            res = input()
            if res == "11":
                hand[x] = "Eleven"
        elif hand[x] == "Eleven":
            print("You have an Ace being scored as an eleven, would you like to score 1 or 11")
            res = input()
            if res == "1":
                hand[x] = "Ace"

def aceCheckDealer(hand):
    #Using a for loop to loop through every card in the dealers hand to see if it is an ace eleven
    for x in range(len(usersHand)):
        if hand[x] == "Ace" or hand[x] == "Eleven":
            print("Dealer has Ace")
            if myFunction(hand) < 11:
                hand[x] = "Eleven"
                print("Dealer picks Aces values as 11")
            else:
                hand[x] = "Ace"
                print("Dealer picks Aces values as 1")
                
#Array of cards
cards = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
usersHand = []
dealersHand = []
dealersGoal = random.randint(15, 22)

#Deal two cards to the user
usersHand.append(cards[random.randint(0, 12)])
usersHand.append(cards[random.randint(0, 12)])

#Deals two cards to the dealer
dealersHand.append(cards[random.randint(0, 12)])
dealersHand.append(cards[random.randint(0, 12)])

#Play game
#Introduction
print("Lets play Blackjack!")
#Output users hand
print("Dealer gives you " + usersHand[0] + " and " + usersHand[1] + ".")
#Ace check
aceCheck(usersHand)
print("User has " + str(myFunction(usersHand)) + ".")
#User can stick or twist
newCard = True
while (newCard):
    #Would the user like to twist or stick
    print("Would you like to stick or twist?")
    response = input()
    response = response.lower()
    if response == "twist":
        #Add card
        usersHand.append(cards[random.randint(0, 12)])
        #Print out the users current hand and work out total
        print("User has ")
        for card in usersHand:
            print(card)
        #Ace check
        aceCheck(usersHand)
        #Print the users total
        print("User has " + str(myFunction(usersHand)) + ".")
        #Check if the user has above 21 
        if myFunction(usersHand) > 21:
            break
    elif response == "stick":
        #Stop taking cards
        newCard = False
        #Output users total
        print("User has " + str(myFunction(usersHand)) + ".")
    else:
        print("Invalid input, please try again and enter either twist or stick")

#Only continue playing the rest of the game if the users score is less that 22
if myFunction(usersHand) <= 21:
    #Output dealers hand
    print()
    print("Dealers cards are")
    print(dealersHand[0])
    print(dealersHand[1])
    aceCheckDealer(dealersHand)
    print("Dealers current total is " + str(myFunction(dealersHand)))
    print()

    #Give dealer a new card until the reach their goal
    while myFunction(dealersHand) < dealersGoal:
        #Give dealer another card
        dealersHand.append(cards[random.randint(0, 12)])
        #Print out the last value in the list
        print("Dealer gets a " + dealersHand[len(dealersHand)-1])
        aceCheckDealer(dealersHand)
        print("Dealers current total is " + str(myFunction(dealersHand)))
        #Check if the user has a total over 21 if so they have lost
        if myFunction(dealersHand) > 21:
            break

    if myFunction(dealersHand) <= 21:
        print("Dealer sticks")
        #Decide who has won, the dealer or user
        if myFunction(dealersHand) > myFunction(usersHand):
            #Game ends
            print("Dealer wins!!")
        elif myFunction(dealersHand) < myFunction(usersHand):
            #Game ends
            print("User wins!!")
        else:
            #Game ends
            print("Games ends in a tie!")  
    else:
        #Game ends
        print("Dealer busts, congratulations you win!!")
else:
    #Game ends
    print("GAME OVER, user busted on "+ str(myFunction(usersHand)) + ". Thanks for playing")

