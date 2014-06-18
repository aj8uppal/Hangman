import time, sys, os, animals, termcolor, typewrite, colors, figures
def clear():
        os.system('clear')
def is_over(all):
        if '_' in all:
                return False
        else:
                return True

clear()
easy = list('rstlne')
medium = list('aeiou')
hard = list('')
figure = figures.figures
guessed = [' ', ' ', ' ', ' ', ' ']
all_guessed = []
guesses_left = 5
answer = animals.rand_animal().lower()
all = list('_'*len(answer))
cur = 0
typewrite.typewrite('Welcome to PythonHangman! Please choose a level: easy, medium, or hard: ', length = 0.055)
level = raw_input('\n')
obj = colors.obj(color='green', attrs=['bold'])
if level.lower().startswith('e'):
        vowels = easy
        typewrite.typewrite('You have chosen easy!')
        for vowel in vowels:
                if vowel in answer:
                        for i in range(len(answer)):
                                if answer[i] == vowel:
                                        all[i] = vowel
elif level.lower().startswith('m'):
        vowels = medium
        typewrite.typewrite('You have chosen medium!')
        for vowel in vowels:
                if vowel in answer:
                        for i in range(len(answer)):
                                if answer[i] == vowel:
                                        all[i] = vowel
else:
        vowels = hard
        typewrite.typewrite('You have chosen hard!')
        for vowel in vowels:
                if vowel in answer:
                        for i in range(len(answer)):
                                if answer[i] == vowel:
                                        all[i] = vowel


while guesses_left > 0 and is_over(all) == False:
        clear()
        print figure[cur] %(tuple(guessed)+(' '.join(all),))
        guess = raw_input('Enter your guess: ')
        if guess in all_guessed:
                print 'Already guessed!'
                time.sleep(1)
        elif guess in vowels and level.lower().startswith('e'):
                print 'All the letters %s, %s, %s, %s, %s, and %s have been guessed for you!' %(obj['r'], obj['s'], obj['t'], obj['l'], obj['n'], obj['e'])
                time.sleep(1)
        elif guess in vowels and level.lower().startswith('m'):
                print 'All the vowels have been guessed for you!'
                time.sleep(1)
        elif guess in answer:
                all_guessed.append(guess)
                for i in range(len(answer)):
                        if answer[i] == guess:
                                all[i] = guess
        else:
                guessed[cur] = termcolor.colored(guess, 'red', attrs=['bold'])
                all_guessed.append(guess)
                cur+=1
                guesses_left-=1

if is_over(all) == True:
        clear()
        print figure[cur] %(tuple(guessed)+(' '.join(all),))
        print 'You Won!'
        sys.exit()

clear()
print figure[cur] %(tuple(guessed)+(' '.join(all),))

last = ['The', 'answer', 'was', answer]

for i in last:
        sys.stdout.write(i+' ')
        sys.stdout.flush()
        time.sleep(0.5)

clear()

all = list(answer)
print figure[cur] %(tuple(guessed)+(' '.join(all),))

sys.stdout.write(' '.join(last)+'\n\n')
