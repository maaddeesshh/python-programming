count = 0

while count < 5:
    print("Count is:", count)
    print("Count is: " + str(count))
    count += 1
print("Done with the exciting loop, Hurray!!!")    



secret_word = "Manchester"
guess= ""

while guess != secret_word:
    guess= input("Enter guess: ")
    
print("You win!!!!")    


secret_word = "Manchester"
guess= ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess= input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True     
if out_of_guesses:
    print("You loose sucker!!!!")
else:
    print("You win!!!!") 
    
    
    
secret_word = "Manchester"
guess= ""
guess_count = 0
guess_limit = 5
# out_of_guesses = False

while guess != secret_word :
    if guess_count < guess_limit:
        guess= input("Enter guess: ")
        guess_count += 1
    else:
        print("you dont have another guess") 
        break   
    
if guess == secret_word:
    print("You win!!!!")        
