import random
n = random.randrange(1,10)

guess = int(input("Enter any number"))

while n!=guess:
    if guess < n:
        print('Too Low')
        guess = int(input("Enter number Again!"))
    elif guess > n:
        print("Too High")
        guess = int(input("Enter number Again!"))
    else:
        break
print("You guessed it right!!")
        
                    
