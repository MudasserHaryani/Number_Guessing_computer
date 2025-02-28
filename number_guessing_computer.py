import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            comp_guess = random.randint(low, high)
        else:
            comp_guess = low
        feedback = input(f"Is {comp_guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = comp_guess - 1
        elif feedback == 'l':
            low = comp_guess + 1
    print(f"Yay! The computer guessed your number, {comp_guess}, correctly!")

# Call the computer_guess function
computer_guess(3)