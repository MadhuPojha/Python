import random

print("Welcome t onumber guessing game! Let's see if you can guess my 3 digit number that has no repeating digits")

def getRandom_No():
    digits = list(range(10)) 
    random.shuffle(digits) 
    return digits[:3] 


def play_games():
    global clueReport
    clueReport = False
    computer_guess = getRandom_No()
    print("computer_guess: ", computer_guess)
    while clueReport is False:
    
        user_guessInput = list(input("What is your guess? "))
        user_guessedNo = [eval(i) for i in user_guessInput]
        clues = []
        print("user_guessedNo: ", user_guessedNo)
        if computer_guess == user_guessedNo:
            clueReport = True
            print("Match: You've guessed a correct number in the correct position")

        else:
            for num in range(len(user_guessedNo)):
                
                if user_guessedNo[num] in computer_guess:
                    if user_guessedNo[num] == computer_guess[num]:
                        clues.append("Close: You've guessed a correct number {} in the correct position".format(user_guessedNo[num]))
                    else:
                        clues.append("Close: You've guessed a correct number {} but in the wrong position".format(user_guessedNo[num]))
                
            if clues == []:
                print("Nope: You haven't guess any of the numbers correctly")
            else:
                print(clues)
                 

play_games()
    
    
