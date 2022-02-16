from random import randint
r = randint(1,20)
prompt = input("Hello, what's your name? ")
print("Well, {}, I am thinking of a number between 1 and 20.".format(prompt))
print("You have 5 guesses.")
count = 0
guess = 0
for guess in range(r):
    guess = int(input("Take a guess: "))
    count += 1
    if r > guess:
        print("Your guess is too low.")
    if r < guess:
        print("Your guess is too high.")
    if guess == r:
        print("Good job, {} You guessed my number in {} guesses!".format(prompt, count))
    if count == 5:
         print("Nope. The number I was thinking of was {}".format(r))
         
    
