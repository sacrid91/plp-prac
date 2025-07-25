import random

#List of jokes
jokes = [
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do python programmers wear glasses? Because they can't C.",
    "What do you call 8 hobbits? A hobbyte.",
    "Why did the computer show up at work late? It had a hard drive.",
    "Why did the edeveloper go broke? Because he used up all his cache.",
    "Why did the functions stop calling each other? Because they had constant arguments.",
    "Why do java developers wear glasses? Because they don't see sharp."
]

#Pick a random joke
joke = random.choices(jokes)

#Print the joke
print("Here's your joke for the day:\n")
print(joke)