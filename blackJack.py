class black_jack():
    
  
    def __init__(self):
        
        self.person=[]
        self.dealer=[]
        #self.ace=int(input('ace=choose 1 or 11='))
    
    def ace(self):
        ace=int(input('ace choose 1 or 11='))
    
    
    
    def deck_of_cards(self):
        
        king=10
        jack=10
        queen=10
        one=2
        two=3
        three=4
        four=5
        five=6
        six=7
        seven=8
        eight=9
        nine=10
        
        import random
        return random.choice([king,queen,jack,one,two,three,four,five,six,seven,eight,nine,self.ace])


    
    def starting_game(self):
        import math
        placeBet=input("how much money do you want to place for bet")

        self.person.append(self.deck_of_cards())
        self.person.append(self.deck_of_cards())
        self.dealer.append(self.deck_of_cards())
        self.dealer.append(self.deck_of_cards())
        
        print('person ={}'.format(math.fsum(self.person)),'dealer={}'.format(math.fsum(self.dealer)))
        
        
    def hit(self):    
        import math
        while True:
            value=21-math.fsum(self.person)
            print('alert player you are {} close to get brust,choose hit or stand wisely'.format(value))
                    
            u=input('hit or stand=')
            
            
            
            if u=='hit':
                print('now person have')
                self.person.append(self.deck_of_cards())
                #using print not return because i want it as a infinite loop ,return simple jump out 
                #of this loop
                print(math.fsum(self.person))
                if math.fsum(self.person)>21:
                    print('you loses dealer wins')
                    break
                
                
                
            
            elif u=='stand':
                print('its dealer')
                
                while True:
                    if math.fsum(self.dealer) <17:
                        self.dealer.append(self.deck_of_cards())
                        #using print here because want to run this like a infinite loop
                        print(math.fsum(self.dealer))
                    elif math.fsum(self.dealer)>21:
                        
                        return'dealer got brust you wins collect your money'
                        #break
                    elif math.fsum(self.person) >math.fsum(self.dealer):
                        return 'you are  a winner ,collect your money man'
                        #break
                    elif math.fsum(self.dealer) >math.fsum(self.person):
                        return 'dealer wins you lose your bet '
                        #break
                
                    
                    
                    
                    else:
                        #its else so i dont want to create infinite loop ,so using retun to jump out 
                        #of loop
                        return 'dealer has sum of {}'.format(math.fsum(self.dealer))
           
           
 #here using return and print very carefully ,listen very carfully
#return ends the function so dont use it when you want to create a infinite loop 
#but like in the last place when i want to finish function after else i use return because i want it
#to stop
