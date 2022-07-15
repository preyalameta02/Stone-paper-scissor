
import random
def game(comp , you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        elif you =='sc':
            return False
    elif comp == 'p':
        if you == 's':
            return False
        elif you =='sc':
            return True
    elif comp == 'sc':
        if you == 'p':
            return False
        elif you =='s':
            return True
    
randNo = random.randint(1,3)
if randNo==1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo ==3:
    comp = 'sc'

you = input("Your turn : Stone(s) paper(p) Scissor(sc) ")
a = game(comp, you)
if a==True:
    print("You win!!")
elif a ==None:
    print("It's a tie!!")
elif a == False:
    print("You lose!!")