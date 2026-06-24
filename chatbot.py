import random
from datetime import datetime

print("✨ SMART STUDY BOT ✨")
print("Type 'help' to see all commands.")
print("Type 'bye' to exit.\n")

name = input("What's your name? ")

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
    "There are 10 types of people: those who understand binary and those who don't. 😂",
    "Why did Python go to school? To improve its class! 😂"
]

facts = [
    "Honey never spoils.",
    "The human brain contains about 86 billion neurons.",
    "Python was named after Monty Python."
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Believe you can and you're halfway there.",
    "Dream big. Start small. Act now."
]

study_tips = [
    "Study for 25 minutes and take a 5 minute break.",
    "Keep your phone away while studying.",
    "Write short notes while learning.",
    "Teach someone else what you learned."
]

subjects = {
    "python": "Practice small projects daily.",
    "math": "Solve problems step by step.",
    "english": "Read and speak regularly.",
    "computer": "Focus on concepts, not memorizing.",
    "physics": "Understand formulas before memorizing.",
    "chemistry": "Practice reactions and equations.",
    "biology": "Use diagrams and flowcharts.",
    "history": "Create timelines for events.",
    "islamiyat": "Revise verses and meanings regularly."
}

quiz_questions = [
    {
        "question": "What is 5 + 5?",
        "answer": "10"
    },
    {
        "question": "What is the capital of Pakistan?",
        "answer": "islamabad"
    },
    {
        "question": "What keyword prints output in Python?",
        "answer": "print"
    }
]

help_text = """
Available Commands:

BASIC CHAT
hello
hi
hey
how are you
good morning
good night
thanks

STUDY
study
motivate me
focus
revision
exam tips
memory tips

SUBJECTS
python
math
english
computer
physics
chemistry
biology
history
islamiyat

FUN
joke
fact
quote
riddle
compliment me

UTILITIES
time
date
day
year
coin flip
dice
random number
calculator

PERSONAL
i am sad
i am happy
i am tired
encourage me

EXTRAS
quiz
goal
success
career
ai
github

OTHER
help
bye
"""

while True:

    user = input(f"\n{name}: ").lower()

    if user == "bye":
        print("Bot: Goodbye! Keep studying and chasing your dreams! 🚀")
        break

    elif user == "help":
        print(help_text)

    elif user in ["hello", "hi", "hey"]:
        print("Bot: Hello! 😊")

    elif user == "how are you":
        print("Bot: I'm doing great! 😎")

    elif user == "good morning":
        print("Bot: Good morning! Have a productive day! 🌞")

    elif user == "good night":
        print("Bot: Good night! Sleep well. 🌙")

    elif user == "thanks":
        print("Bot: You're welcome! 😊")

    elif user == "study":
        print("Bot:", random.choice(study_tips))

    elif user == "motivate me":
        print("Bot: Your future self will thank you for studying today! 🔥")

    elif user == "focus":
        print("Bot: Focus on one task at a time. 🎯")

    elif user == "revision":
        print("Bot: Revise important topics before starting new ones. 📚")

    elif user == "exam tips":
        print("Bot: Practice past papers and manage your time well. 📝")

    elif user == "memory tips":
        print("Bot: Use flashcards and active recall. 🧠")

    elif user in subjects:
        print("Bot:", subjects[user])

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "fact":
        print("Bot:", random.choice(facts))

    elif user == "quote":
        print("Bot:", random.choice(quotes))

    elif user == "riddle":
        print("Bot: What has keys but can't open locks? A piano! 🎹")

    elif user == "compliment me":
        print("Bot: You're capable of achieving amazing things! 🌟")

    elif user == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d/%m/%Y"))

    elif user == "day":
        print("Bot:", datetime.now().strftime("%A"))

    elif user == "year":
        print("Bot:", datetime.now().strftime("%Y"))

    elif user == "coin flip":
        print("Bot:", random.choice(["Heads", "Tails"]))

    elif user == "dice":
        print("Bot: 🎲", random.randint(1, 6))

    elif user == "random number":
        print("Bot:", random.randint(1, 100))

    elif user == "calculator":
        try:
            num1 = float(input("First number: "))
            op = input("Operator (+ - * /): ")
            num2 = float(input("Second number: "))

            if op == "+":
                print("Result:", num1 + num2)
            elif op == "-":
                print("Result:", num1 - num2)
            elif op == "*":
                print("Result:", num1 * num2)
            elif op == "/":
                print("Result:", num1 / num2)
            else:
                print("Invalid operator.")
        except:
            print("Invalid input.")

    elif user == "i am sad":
        print("Bot: Better days are coming. ❤️")

    elif user == "i am happy":
        print("Bot: That's wonderful! 😄")

    elif user == "i am tired":
        print("Bot: Take a short break and recharge. ☕")

    elif user == "encourage me":
        print("Bot: Keep going. Progress is progress, no matter how small. 💪")

    elif user == "goal":
        print("Bot: Set a goal, make a plan, and stay consistent. 🎯")

    elif user == "success":
        print("Bot: Success comes from consistency, not perfection. 🚀")

    elif user == "career":
        print("Bot: Keep learning valuable skills and building projects. 💻")

    elif user == "ai":
        print("Bot: AI is the simulation of human intelligence by machines. 🤖")

    elif user == "github":
        print("Bot: GitHub helps developers store and share code. 🌐")

    elif user == "quiz":
        q = random.choice(quiz_questions)
        answer = input(q["question"] + " ").lower()

        if answer == q["answer"]:
            print("Bot: Correct! 🎉")
        else:
            print("Bot: Wrong! The answer was:", q["answer"])

    else:
        print("Bot: I don't understand that command. Type 'help'.")