#Jumbled words game : guess the correct word 

#Selecting a word 
import random
def choose():
    words = [ "pronunciation","ajaykumar","phenomenon","computer","arrays","temperature","converter","migration","binary","jupyter","anaconda","transcription","transaction","microsoft","instagram","reverse","linear","autonomous","argument","algorithm","development","programming","software","interaction","mathematimatics","environment","hardware","application","technology","intelligence"]
    pick = random.choice(words)
    return pick
#Jumbling the selected word  
def jumble(word):
    jumbled =  "".join(random.sample(word , len(word)))
    return jumbled 



   
def thank( Player1, Player2, P1points, P2points):
    if P1points > P2points:
        print(Player1 , ", won the game.")
    elif P1points == P2points:
        print("Tie game")
    else:
        print(Player2, ", won the game.")
    print(Player1, ", your score is :", P1points)
    print(Player2, ", your score is :", P2points)
    print("Thanks for playing!")
    
def play():
    print("Welcom to Jumble Words Game")
    P1 = input("Player1, please enter your name: ")
    P2 = input("Player2, please enter your name: ")
    #pp1 = player1 points and pp2 = player2 points are intially zero.
    pp1 = 0
    pp2 = 0
    turn = 0
    while True:
        picked_word = choose()
        question = jumble(picked_word)
        if turn % 2 == 0:
            print(P1, "your turn now")
            print(question)
            ans = input("Guess the above : ")
            if ans == picked_word :
                pp1 += 1
                print("you  guessed the correct word", P1 ,"\n", P1," your score is :", pp1)
            else:
                print("You are wrong,", P1)
                print(P1,'score is ',pp2)
                print("Correct word is :", picked_word)
            print("Press '1' to continue \nPress '0' to exit")
            C = int(input("Please enter only 1 or 0, case sensitive: "))
            if C == 0:
                thank(P1,P2,pp1,pp2)
                break
            
        else:
            print(P2, "your turn now ")
            print(question)
            ans = input("Guess the above word: ")
            if ans == picked_word :
                pp2 += 1
                print("you  guessed the correct word", P2 ,"\n", P2,"score is :", pp2)
            else:
                print("You are wrong  ,", P2)
                print(P2,"score is :", pp2)
                print("Correct word is :", picked_word)
            print("Press '1' to continue \nPress '0' to exit")
            C = int(input("case sensitive: "))
            if C == 0:
                thank(P1,P2,pp1,pp2)
                break    
        turn += 1
            
play()
input("Please press enter to exit.")
                
                
                
                
                

        
        
 