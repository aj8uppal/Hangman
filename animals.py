def rand_animal():
        import random
        animals = open('animals.txt').read().split()
        return random.choice(animals)
