#! /usr/bin/python3
from main import *
from question import Question,run_test
from database import *

result = fetch()




class Superuser(Question):

    def __init__(self,name):
        self.name=name
        Question.__init__(self)
    

    def addQuestion(self,topic_name,difficulty_level):
        if identity == 2:
            Question._addQuestion(self,topic_name,difficulty_level)
            execute()

        else:
            print("You are not a super user")
    
def displayAllQuestions(result=result):
    if identity == 2:
        print("Total no of questions: ",len(result))
        print("!!!!!!!!Begining of Questions!!!!!!!!!!!")
        for i in range(len(result)):
            print("\t"+result[i][0]+"\t")
        print("!!!!!!!!!!!!End of Questions!!!!!!!!!!!!!")
    else:
        print("You are not a super user")
    
        
def quiz_test():
    run_test(result=result)
        
if identity == 1:
    print("Enter your name \n")
    name = input("Enter Here: ")
    print()
    print("Enter your location \n")
    location = input("Enter Here: ")
    print()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("To run the test, Enter 'Y' for Yes or 'N' for No \n")
    output = input("Enter here: ").lower()
    if output == "y":
        quiz_test()
        print()
        print("Thanks for visiting,",name,"from",location,"!!!\n")
        print("Correct answers for the question !!!!\n")
        for i in result:
            print("Question:",i[0],"Answer: option",i[2],"\n")
        print("End !!!!!!!!!!!!!!!!!")

    else:
        print("exiting the application\n")
        print("!!!!!!!!!!!!GOODBYE!!!!!!!!!!!!!")
        quit()
   


if identity == 2:
    superuser_name = input("Enter your name,Superuser: ")
    print()
    print("Don't tell your secret phase to anyone\n")
    obj = Superuser(superuser_name)


    while True:
        print("Do you want to add questions to database\n")
        print("Enter 'Y' for yes or 'N' for no\n")
        add_q = input("Enter here: ").lower()
        print()
        if add_q == "y":
            topic = input("enter the topic of your choice: ")
            print()
            level = input("enter difficulty of your choice : easy,medium or hard: ")

            obj.addQuestion(topic,level)
        elif add_q == 'n':
            dq = input("if you want to display all the question,Press Y for yes or N for no: ").lower()
            print()
            if dq == "y":
                displayAllQuestions()
            
        print("Finally,Do u want to add questions, Enter Y for yes and N for no\n")
        inf = input("Enter Here: ").lower()
        if inf == "y":
            topic = input("enter the topic of your choice: ")
            print()
            level = input("enter difficulty of your choice : easy,medium or hard: ")
            print()
            obj.addQuestion(topic,level)
        else:
            break
    

    


    print("Lastly,if u want to Display all your questions, Enter 'Y' for Yes or 'N' for No\n")
    display = input("Enter here: ").lower()
    print()
    while True:
        if display == "y":
            displayAllQuestions()
            break
        else:
            print("quitting the application\n")
            quit()
            