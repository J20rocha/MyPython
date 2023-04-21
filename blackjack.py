import random
import sys

CardsList =['A', 'K', 'Q', 'J', 10, 9, 8, 7,6,5,4, 3,2]
PipsList= ['C','H','D','S']

PlayerHand=[]
PlayerPip=[]
DealerHand=[]
DealerPip=[]

#Create the initial 2 cards for the dealer and the player
def CreatePlayerHand():
    for i in range(1,3):
        PlayerCards= CardsList[random.randrange(0, 13)]
        PlayerHand.append(PlayerCards)
        PlayerPip.append(PipsList[random.randrange(0, 4)])
        
    for j in range(len(PlayerHand)):
        print(f"Player's Card number {j+1} is {PlayerHand[j]} of {PlayerPip[j]}")

def CreateDealerHand():
    for i in range(1, 3):
        DealerCards = CardsList[random.randrange(0, 13)]
        DealerHand.append(DealerCards)
        DealerPip.append(PipsList[random.randrange(0, 4)])

    # Adapt this part so that only the first card of the dealer is shown, and then only later is shown
    print(f"Dealer's Card number 1 is {DealerHand[0]} of {DealerPip[0]}")
    print("Dealer's Card number 2 is *hidden*")


#Possible Plays
def Play():
    print("Select your move:\n C. Ask Card\n S. Stay\n E. Exit")
    play = input()
    if play.lower() == 'c':
        AddPlayerCard()
    elif play.lower() == 'e':
        sys.exit()
    return play


#Stay option compares the deale's and the player's points. Dealer stands at 16 and stops at 17
def DealerPlay(DealerPoints, PlayerPoints):
    if DealerPoints >= 16:
        results(DealerPoints, PlayerPoints)
        return DealerPoints
    elif DealerPoints < 16:
        AddDealerCard()
        DealerPoints = PointsCalculator(DealerHand, PlayerHand)
        return DealerPlay(DealerPoints, PlayerPoints)
        


#Adding a card to the player and the dealer
def AddPlayerCard():
    NewCard = CardsList[random.randrange(0, 13)]
    NewPip = PipsList[random.randrange(0, 4)]
    PlayerHand.append(NewCard)
    PlayerPip.append(NewPip)
    print(f"New Card: {NewCard} of {NewPip}")

def AddDealerCard():
    NewCard=CardsList[random.randrange(0, 13)]
    NewPip=PipsList[random.randrange(0, 4)]
    DealerHand.append(NewCard)
    DealerPip.append(NewPip)
    print(f"New Card: {NewCard} of {NewPip}")

def results(DealerPoints, PlayerPoints):
    if DealerPoints > PlayerPoints or PlayerPoints > 21:
        return "You Lose"
    else: return "You Win!"
    

#calculate the points
def PointsCalculator(PlayerHand, DealerHand):
    PlayerPoints = 0
    DealerPoints = 0
    
    for card in PlayerHand:
        if card == 'A':
            # Handle Ace separately
            if PlayerPoints + 11 <= 21:
                PlayerPoints += 11
            else:
                PlayerPoints += 1
        elif card in ['K', 'Q', 'J', '10']:
            PlayerPoints += 10
        else:
            PlayerPoints += int(card)

    for card in DealerHand:
        if card == 'A':
            if DealerPoints + 11<= 21:
                DealerPoints += 11
            else:
                PlayerPoints +=1
        elif card in ['A', 'K', 'Q', 'J']:
            DealerPoints +=10
        else:
            DealerPoints += int(card)
    print(PlayerPoints)
    print(DealerPoints)    



if __name__=="__main__":
    CreatePlayerHand()
    CreateDealerHand()
    
    PlayerPoints = PointsCalculator(PlayerHand, DealerHand)
    
    # Player's turn
    play = Play()
    while play != 's':
        play = Play()
        PlayerPoints = PointsCalculator(PlayerHand, DealerHand)
        if PlayerPoints > 21:
            print("Busted!")
            sys.exit()
    
    # Dealer's turn
    DealerPoints = PointsCalculator(DealerHand, PlayerHand)
    DealerPlay(DealerPoints, PlayerPoints)
    
    print(f"Player's final hand: {PlayerHand} (total: {PlayerPoints})")
    print(f"Dealer's final hand: {DealerHand} (total: {DealerPoints})")
    print(results(DealerPoints, PlayerPoints))


  
