import random
from IPython.display import clear_output




ranks=['two','Three','Four','Five','Six','Seven','Eight','Nine','King','Queen','Jack','Ace']
values={'two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'King':10,'Queen':10,'Jack':10,'Ace':11}
suits=['hearts','diamonds','spades','clubs']
playing=True


class card():
    
    
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    
    
    def __str__(self):
        return self.rank+' of '+self.suit
        

class Deck():
    
    
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(rank,suit))
    
    
    def __str__(self):
        deck=''
        for card in self.deck:
            deck+='\n'+card.__str__()
        return 'deck has:'+deck
    
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    
    def deal(self):
        single_card=self.deck.pop()
        return single_card


class Hand():
    
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    
    def adjust_for_ace(self):
        if  self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

class Chips():
    def __init__(self,chips):
        self.total=chips
        self.bet=0
    
    def win_bet(self):
        self.total+=self.bet
        
    def loose_bet(self):
        self.total-=self.bet
        
def take_bet(chips):
    while True:
        try:
            print(f'you have {chips.total} chips!')
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total and chips.total!=0 :
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break 


def hit(Deck,Hand):
    Hand.add_card(Deck.deal())
    Hand.adjust_for_ace()
    

def hit_or_stand(Deck,Hand):
    global playing
    
    while True:
        x=input('hit or stand:')
        
        if x[0].lower()=='h':
            hit(Deck,Hand)
        elif x[0].lower()=='s':
            playing = False
        else:
            print('enter valid input')
            continue
        break
    

def show_some(player,dealer):
    clear_output()
    print('\n Dealers hand:')
    print('<card hidden>')
    print('',dealer.cards[1])
    print('\n players hand:')
    print( *player.cards,sep='\n')
    print("Player's stands at:",player.value)
    
        
def show_all(player,dealer):
    clear_output()
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.loose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.loose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


    
chips=int(input('how many chips do you have?'))
while True:
    print(' Welcome to BlackJack!')

    

    deck=Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
        
    player_chips=Chips(chips)
    

    take_bet(player_chips)
    
   
    show_some(player,dealer)
    
    while playing:  
        
        
        hit_or_stand(deck,player)
        
        show_some(player,dealer)
        
        
        if player.value>21:
            player_busts(player,dealer,player_chips)
            break


    if player.value<=21:
        while dealer.value<17:
            hit(deck,dealer)
            
    
        
        show_all(player,dealer)
    
        if dealer.value > 21:
            dealer_busts(player,dealer,player_chips)

        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chips)

        elif dealer.value < player.value:
            player_wins(player,dealer,player_chips)

        else:
            push(player,dealer)
     
    print("\nPlayer's winnings stand at",player_chips.total)
    
  
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        chips=player_chips.total
        if chips>0:
            
            clear_output()
            playing=True
            continue
        else:
            clear_output()
            print("Sorry,looks like you have lost all your chips!")
            ask=input('do you want to start playing again?')
            if ask.lower()=='yes':
                playing=True
                chips=int(input('how many chips do you have?'))
            elif ask.lower()=='no':
                    clear_output()
                    print("Thanks for playing!")
                    break
    else:
        
        clear_output()
        print("Thanks for playing!")
        break
