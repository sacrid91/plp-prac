#Simple Quiz Game 🎮
#Create a 1.multiple-choice quiz with 
# questions about Python, movies, or any fun topic! 
# Display scores at the end and allow the user to play again. 🏆

#NOT E buffering in the vs code terminal might cause the quiz to show one optiona at a time
import time
import os
import sys

print("Welcome to the Forex Basic Quiz...")

user = input("Provide 1st name to undertake the Quiz..")

print(f"Hello {user},\nThe grading will come afterwards\nAll the Best!")

#Lists of Questions using Dictionary Data type
fxQuest = [{"question":"1. What does FOREX stand for?","options":{"a":"Foreign Exchange",
                                                                  "b":"For External Trade",
                                                                  "c":"Foreign Expansion"},
                                                       "answer":"a"},
           {"question":"2. What is a 'pip' in FOREX trading?","options":{"a":"A type of currency",
                                                                         "b":"The smallest Price move",
                                                                         "c":"An economic policy"},
                                                        "answer":"b"},
           {"question":"3. What are the most traded currency pairs called?","options":{"a":"Minors",
                                                                                       "b":"Exotics",
                                                                                       "c":"Majors"},
                                                        "answer":"c"},
           {"question":"4. Which two currencies are in the EUR/USD pair?","options":{"a":"Euro and US dollar",
                                                                                     "b":"Pound and Yen",
                                                                                     "c":"Dollar and Franc"},
                                                        "answer":"a"},
           {"question":"5. What does leverage 'leverage' the trader to do?","options":{"a":"Buy only Physical Assets",
                                                                                       "b":"Trade larger amounts with less capital",
                                                                                       "c":"Avoid paying taxes"},
                                                        "answer":"b"
           }
          ]

score = 0

#Quiz loop
for q in fxQuest:
    
    #print(q["question"])
    print("\n" + q["question"])
    time.sleep(0.5) #For readability
    
    #Print all options first
    for key in sorted(q["options"]):
        print(f"{key} {q['options'][key]}")
        
        #Force all print output to appear b4 input prompt
        sys.stdout.flush()
        
            
         
    #Validate loop
    blank_count = 0
    while True:
        user_answ = input("For your answer, \nType either (a/b/c):").strip().lower()
        if user_answ == "":
            blank_count += 1
            if blank_count >= 3:
                print("Need Help?\nRemember your options are a,b or c when ready")
            #Just Enter -Let user scroll, do nothing
            continue
        elif user_answ in ['a','b','c']:
            break #Valid Answer,Proceed
        else:
            print("Invalid input.\nPlease enter 'a', 'b' or 'c'")
    
    
    if user_answ == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong!\nThe correct answer was {q['answer']}")
        
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
            
#Final score
print(f"{user}, The Quiz is complete...You scored {score} out of {len(fxQuest)}.")

if score == 5:
    print("Perfect You're ready to Learn about candlestcks\nExplore on it\nThen Demo")
elif score >=3:
    print("You did a good work...Look for PDFs on the same to sharpen the knowledge!")
else:
    print("It's all in the mindset,It was hard at first for me too!\nKeep Learning!")
                
        