
#Mathematical thinking (Decompression, Pattern Recog, Abstraction, Algo design)

#🔹Challenge: 
#1.Create a program that reads a text file, done..
#2.processes its content, and done...
#3.writes the results to a new file.

#📌 Task Requirements:
#Create a file called input.txt and write at least five lines of text into it.
#Write a Python script to:
#Read the contents of input.txt.
#Count the number of words in the file.
#Convert all text to uppercase.
#Write the processed text and the word count to a new file called output.txt.
#Print a success message once the new file is created.

#Open and read input.txt file
with open("input.txt","r") as file:
    data = file.read()
    
#Processing the data
upperCasedData = data.upper()

#Wordlength
wordLength = len(upperCasedData.split())
   
#Write to output.txt file
with open("output.txt","w") as file:
    file.write(upperCasedData)
    file.write(f"\n\nWord count is {wordLength}")
    
print("Processing complete.Result saved in output.txt")    