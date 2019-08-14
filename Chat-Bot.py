import time
import random

funFacts = ["Most toilets flush in E flat.",
"A raisin dropped in a glass of fresh champagne will bounce up and down continuously from the bottom of the glass to the top.",
". Cap’n Crunch’s full name is Horatio Magellan Crunch.",
"The Vatican City is the country that drinks the most wine per capita at 74 liters per citizen per year.",
"Approximately 40,000 Americans are injured by toilets each year.",
"If a female ferret does not have sex for a year, she will die.",
"Ketchup was sold in the 1830s as medicine.",
"“Almost” is the longest word in English with all the letters in alphabetical order.",
"Sean Connery wore a toupee in all his James Bond movies.",
"Nicholas Cage bought a pet octopus once because he sincerely thought it might help with his acting.",
"Nicholas Cage also once did magic mushrooms with his cat.",
"It actually takes 142.18 licks to reach the center of a Tootsie pop.",
"1% of all women can achieve full orgasm just by stimulating their breasts.",
"You’ll eat more than 35,000 cookies in your lifetime (probably).",
"Steve Jobs relieved stress by soaking his feet in Apple’s company toilets.",
"Fredric Baur was the man who invented the iconic “Pringles” can. When he died, his ashes were buried in one.",
"There is enough sperm in one single man to impregnate every woman on earth.",
"It is impossible to sneeze with your eyes open.",
"Human birth control pills work on gorillas.",
"France was still executing people by guillotine when the first Star Wars movie came outAll swans in England belong to the queen.",
"No piece of square paper can be folded more than 7 times in half.",
"The US Treasury once considered producing doughnut-shaped coins!"]

print("Hello")


name = input("Whats your name?")
if "why should i tell you" in name:
    print("Its ok you don't have to tell me your name.")

elif "no" in name:
    print("ha got you toby")
else:
    print("Hello " + name)

while True:
    feeling = input("How are you today?")
    if "good" in feeling:
        print("I'm feeling good too!")
        break

    elif "whos asking" in feeling:
        print("I'm asking" + name)


    else:
        print("Ohhh I'm sorry to hear that")
        break


time.sleep(2)
favcolour = input("What's your favorite colour?")

colours =["red", "Green", "Blue","Yellow"]

time.sleep(1.5)
print("My favorite colour at the moment is " + random.choice(colours))
time.sleep(2)

chanceGame = input("Do you want to play a game of chance?")

if"yes" in chanceGame:
    input("Heads or Tails")
    cointoss = random.randint(1, 2)

    if cointoss == 1:
        print("It was heads")


    else:
        print("It's tails")

else:
    print("Ok then.")

funFact = input("Do you want to hear a fun fact")
if "yes" in funFact:
    print(random.choice(funFacts))

else:
    print("Ok Then")


time.sleep(2)
bye = input("I have to go now, I am very busy today.")
if "bye" in bye:
    print("Bye")

elif "see you later aligator" in bye:
    print("After awhile crocadile.")

else:
    print("Peace Out")



