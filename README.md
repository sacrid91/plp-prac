This repository contains three simple Python applications that demonstrate basic programming concepts such as user input, conditionals, loops, and randomization. These are part of the PowerLearnProject practical exercises. 
 
🧾 Project Overview 
1. greetingApp.py – Personalized Greeting App 

A program that: 

    Asks the user for their name and favorite color.
    Prints a personalized greeting using both f-strings and .format() formatting.
------------------------------------------------------------------------------------    
 2. quizGame.py – Simple Quiz Game 

A multiple-choice quiz about Forex basics with: 

    5 questions.
    Input validation for answers (a, b, or c).
    Score tracking.
    Option to play again (not included in this version).
     

Features: 

    Displays each question and options one by one.
    Provides feedback after each answer.
    Shows final score at the end.
------------------------------------------------------------------------------------
3. jokeGen.py – Joke Generator 

A simple script that: 

    Stores a list of jokes.
    Randomly selects and displays one joke from the list.
------------------------------------------------------------------------------------
4. largePower.py
A script that evaluates the exponent and returns value and if it's >= 5000 it returns True else False
    i.e Base 4 and Exponent 2 in 4² = 16 False
------------------------------------------------------------------------------------
5. fileHandler file contains a fileHandler.py + input.txt + output.txt
   The python file reads from input.txt then writes in output.txt 
------------------------------------------------------------------------------------
How to Run the Scripts 

Make sure you have Python 3 installed on your system. 

To run any script, open your terminal or command prompt and navigate to the folder containing the files, then run: 

     python greetingApp.py
     python quizGame.py
     python jokeGen.py
     python largePower.py
     python fileHandler.py
------------------------------------------------------------------------------------
NOTE: 

    The quizGame.py may show issues in some terminals due to buffering, especially in VS Code..
    but I have already handled it with stdout() in the code.
    Ensure you're using a compatible terminal or adjust the output flush logic if needed.
    All scripts are self-contained and require no external libraries.
------------------------------------------------------------------------------------
