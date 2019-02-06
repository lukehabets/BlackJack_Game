import random

def main():    

    q = 0 #quit variable, 0 will continue, will quit when pulled high
    chips = 100 #chip count (begin with 100)
    bet = 0 #bet amount
    card1 = 0 #player card 1
    card2 = 0 #player card 2
    dealerCard = 0 #dealer start card
    hitStay = 0 #hit or stay flag
    handTotal = 0 #total value of cards in hand (must remain below 22 or lose)
    nextCard = 0
    
    welcome() #calling welcome function
    begin() #calling function to begin game
    
    while(q != 1 or chips < 1):

        print("Chips: ",chips) #printing chip amount (initially 100)

        while(bet < 1 or bet > 10): #getting a bet amount between 1 and 10
            print("Please enter a bet between 1 & 10")
            bet = int(input())
        
        card1 = random.randint(1,10) #randomizing cards between 1 and 10
        card2 = random.randint(1,10)
        dealerCard = random.randint(1,10)

        print("Card 1: ",card1)     #printing initial 2 cards
        print("Card 2: ",card2,"\n")

        if(card1 == 1 and card2 == 10) or (card1 == 10 and card2 == 10): #checking for blackjack
            print("BLACKJACK, YOU WIN")
            chips = chips + bet
        
        print("Dealer Card: ",dealerCard,"\n")

        handTotal = card1 + card2 #totalling player hand
        print("Your hand total is: ",handTotal,". Don't go over 21!")

        while(hitStay < 1 or hitStay > 2): #checking for 1 or 2
            print("Enter '1' to Hit or '2' to stay")
            hitStay = int(input())
            
        while(hitStay == 1): #loop if player chooses '1' to hit
                nextCard = random.randint(1,10) #generating next card
                handTotal = handTotal + nextCard
                print("Next card: ",nextCard)
                print("Hand total: ",handTotal)

                if(handTotal > 21): #checking for player bust
                    print("You lost by busting!")
                    handTotal = 0 #resetting handTotal to 0
                    hitStay = 2 #exiting hit loop by setting to 2
                    chips = chips - bet #subtracting bet from chips
                else:
                    print("Enter '1' to hit again, or '2' to stay")
                    hitStay = int(input())
                    
        #need dealer to player compare now if stay and dealer hit routine
        
        
        
        
        print("Enter '1' to quit OR any other number to continue")
        q = int(input())

def welcome():
    print("Hello. Welcome to our BlackJack game.")
    print("You will start with 100 chips and can bet a maximum of 10 per bet.")
    print("A 1 and a 10 indicates a blackjack.")
    print("You can play until you run out of chips or decide you have had enough.")
    print("\n")
    print("Have Fun!")

def begin():
    start = 0
    while(start != 1): #start key with input validation
            print("\n\n\n","~Enter '1' to begin~")
            
            start = int(input())



main() #calling main function 
