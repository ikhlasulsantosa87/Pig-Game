import random # Python built-in modules to make random numbers

def dice():
    
    """
        Definitions: A function that acts as a dice. Using a random module and random.randint() method from Python to simulate the roll of a dice. Returns a random number from 1 - 6.
    """

    min_number = 1
    max_number = 6

    dice = random.randint(min_number, max_number)

    return dice