questions = ['What is CPU stand for ? ',
             'What is GPU stand for ? ',
             'What is RAM stand for ? ',   ]

answers = ['central processing unit',
            "graphics processing unit",
            "random access memory"]


print("Welcome to the quiz!")
playing = input("Do you want to play ? y/n : ")
playing = playing.lower()
while playing!='y' or playing!='n':

    if playing== 'y':
        break
    elif playing == 'n':
        quit()
    else:
        print("Sorry I didn't get that...please type your answer again")
        playing = input("Do you want to play ? y/n : ")


print("Let's begin then...")

score = 0;

for i in range(len(questions)):
    print(questions[i])
    answer = input("Type your answer: ")
    if(answers[i]==answer.lower()):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("You got " + str((score /len(questions))*100)  + "% questions correct ! ")
print( "Thanks for playing ! Bye Bye ^^ ")





