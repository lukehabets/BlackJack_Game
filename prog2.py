import random

def main():    
    q = 0 #quit variable, 0 will continue, will quit when pulled high
    chips = 100 #chip count (begin with 100)
    bet = 0 #bet amount
    card1 = 0 #player card 1
    card2 = 0 #player card 2
    dealerCard = 0 #dealer start card
    hitStay = 0 #hit or stay flag (1 to hit, 2 to stay)
    handTotal = 0 #total value of cards in hand (must remain below 22 or lose)
    nextCard = 0
    blackJackWin = 0 #set to 1 if a blackjack is hit
    
    welcome() #calling welcome function
    begin() #calling function to begin game
    
    while(q == 0 and chips > 1):

        hitStay = 0 #resetting hit/stay variable after loop
        bet = 0 #resetting bet after loop
        
        print("\n","Chips: ",chips) #printing chip amount (initially 100)

        while(bet < 1 or bet > 10): #getting a bet amount between 1 and 10
            print("Please enter a bet between 1 & 10")
            bet = int(input())

        blackJackWin = 0 #resetting blackJack flag after loop
        card1 = random.randint(1,10) #randomizing cards between 1 and 10
        card2 = random.randint(1,10)
        dealerCard = random.randint(1,10)

        print("Card 1: ",card1)     #printing initial 2 cards
        print("Card 2: ",card2,"\n")

        if(card1 == 1 and card2 == 10) or (card1 == 10 and card2 == 10): #checking for blackjack
            print("BLACKJACK, YOU WIN")
            chips = chips + bet
            blackJackWin = 1 #setting blackJack flag high to signal blackjack
        
        if(blackJackWin == 0): #if they did not get a blackjack
        
            print("Dealer Card: ",dealerCard,"\n") #show dealer card

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
                    
            if(handTotal < 22): #if didn't bust
                while(dealerCard < 17): #dealer hitting until at least 17
                    dealerCard = dealerCard + random.randint(1,10)

                if(dealerCard > 21): #if dealer busts
                    print("Dealer busts! You Win!")
                    chips = chips + bet
                else:
                    if(dealerCard > handTotal): #if dealer wins
                        print("House Wins! Try Again")
                        print("Dealer: ",dealerCard,"\t","You: ",handTotal)
                        chips = chips - bet #subtract loss
                    elif(handTotal > dealerCard): #if player wins
                        print("You Win! Congrats!")
                        print("You: ",handTotal,"\t","Dealer: ",dealerCard)
                        chips = chips + bet #add winnings
                    else: #if tie
                        print("Its a  tie!")
                        print("You both had: ",handTotal)
             
        print("\n","Enter '0' to continue OR any other number to quit") #prompt to quit
        q = int(input()) 

def welcome(): #welcome function for greeting, in seperate function to clean up code
    print("Hello. Welcome to our BlackJack game.")
    print("You will start with 100 chips and can bet a maximum of 10 per bet.")
    print("A 1 and a 10 indicates a blackjack.")
    print("You can play until you run out of chips or decide you have had enough.")
    print("\n")
    print("Have Fun!")

def begin(): #beginning button press function
    start = 0
    while(start != 1): #start key with input validation
        print("\n\n\n","~Enter '1' to begin~")
        start = int(input())

main() #calling main function 
