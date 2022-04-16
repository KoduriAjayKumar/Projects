import string 
import random

def exit():
    n = int(input("Press 1 to continue \nPress 0 to exit: "))
    print()
    if n == 0:
        print("Thanks for playing")
        input("Please press enter for exit")
    else:
        Dobble_game()
        
        
def Dobble_game():
    print("Welcome to Dobble game(#finding the same symbol).")
    print()
    card1 = [0]*7
    card2 = [0]*7
    symbols = list(string.ascii_letters)
    same_symbol = random.choice(symbols)
    symbols.remove(same_symbol)
    post1 = random.randint(0,6)
    post2 = random.randint(0,6)
    card2[post2] = same_symbol
    card1[post1] = same_symbol
    i = 0
    while(i<7):
        if i != post1 :
            alphabet1 = random.choice(symbols)
            symbols.remove(alphabet1)
            card1[i] = alphabet1
        if i != post2 :
            alphabet2 = random.choice(symbols)
            symbols.remove(alphabet2)
            card2[i] = alphabet2
        i += 1
    print(card1)
    print(card2)
    print()
    ans = input("spot the same symbol in above two lists: ")
    if ans == same_symbol :
        print("You are correct")
        print()
    else:
        print("You are wrong")
        print("Correct answer is :", same_symbol)
        print().
    exit()   


             
Dobble_game()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
