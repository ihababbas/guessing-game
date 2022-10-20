from mimetypes import guess_all_extensions
from  random import randint

class GuessingGame :

    '''
    a fun game let user to interact with computer, guessing the number that the game has generated from 1 - 20 
    in five rounds 
    
    
    '''

    result={}
    def __init__(self,player):
        self.player=player
        self.number=randint(1,20)
        self.score = 0
        self.guessed_number=''
        
    def guess_number(self):

            '''
            Check the player input and return the result , with calculating the remaining rounds  
            
            '''
            count=5
            scores=[0,2,4,6,8,10]
            while count > 0 :
                

                try:

                    if __name__=='__main__':
                    
                        self.guessed_number=int(input(f'Dear {self.player} enter your guess between (1-20)  '))
                    if self.guessed_number == self.number:
                        self.score=scores[count]
                        print(f'congrats ! , You win the number is {self.number} and your score is : {scores[count]} ')
                    
                        count = 0
                    if self.guessed_number > self.number:
                        count-=1
                        if count == 0:
                            print ('you lose ')
                            
                        else:
                            print(f'your guess too high ,{count} rounds left')
                    if self.guessed_number < self.number:
                        count-=1
                        if count == 0:
                            print ('you lose ')
                            
                        else:
                            print(f'your guess too low ,{count} rounds left')
                except ValueError:
                         print('The provided value is not an integer')
                         continue

         


    def display_score(self):
        '''
        
         display all the players score as list at the end of the game and appended on score file
        
        '''
        with open ('./score.txt','a') as file:
            file.write(f'\n Name : {self.player} | Score : {self.score}')

        with open ('./score.txt','r') as f:

            print(f.read())
       

class RunGame:

    def run():

        '''
        Run the game class with welcome message and give the player a choice to play again or quit the game  
        '''

        if __name__=='__main__':
                x=True
                while x :
                
                    print('''#####  Hi! welcome to Guessing Game   ##### ''')

                    player_1=input("Please Enter Your Name ==> ")
                    player=GuessingGame(player_1)
                    player.guess_number()
                    player.display_score()

                    ask=input('Do you want to play again? y/n ')
                    if ask == 'n' or ask == 'N': 
                            print("Bye , we hope you come soon ")
                            
                            x=False
                    elif ask == 'y' or ask == 'Y':
                            x=True
                    else:
                            print("Incorrect Input")
                            x=True
        else:
            pass  

        
                 
RunGame.run()

    















