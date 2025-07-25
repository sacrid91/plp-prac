#Personalized Greeting App 👋
#Create a program that 1.asks for the user’s name and 
#                      2.favorite color, 
#                      3.then prints a personalized greeting like:
# “Hello, [Name]! Your favorite color, [Color], is awesome!”
username = input("Enter your name Please!")

favColor = input("What's your favourite color?")

#Prints with f string formatter
print(f"Hello {username} ,the {favColor} is my favourite color too!\nThat's awesome")

#Prints with .format
print("Hello {},Wow your favourite color is {} .. \nThat's Awesome.".format(username, favColor))
