#! /usr/bin/python3



class Question:
    
    prompt=[]
    options=[]
    answers=[]
    topic_name=[]
    difficulty_level=[]

    def __init__(self,prompt=[],options=[],answer=[],topic_name=[],difficulty_level=[]):
        self.prompt=prompt
        self.options=options
        self.answer=answer
        self.topic_name=topic_name
        self.difficulty_level=difficulty_level
        
    
    def _addQuestion(self,topic_name,difficulty_level):

        statement=input("Enter question statement: ")
        self.prompt = statement
        Question.prompt = self.prompt
        self.topic_name = topic_name
        Question.topic_name = self.topic_name
        self.difficulty_level = difficulty_level
        Question.difficulty_level = self.difficulty_level

        l1=[]
        for i in range(4):
            l1.append(input("Enter option no. "+str((i+1))+": "))
        self.options = l1
        Question.options = self.options

        ans=input("Which is the correct option (1/2/3/4) ? ")
        self.answer = ans
        Question.answers = self.answer
        
            

def run_test(result):
    score = 0
    for i in range(len(result)):
        print("Topic: "+result[i][3],"\n")
        print(result[i][0],"\n") 
        opt = eval(result[i][1])
        for num in range(4):
            print(str(num+1)+")"+str(opt[num]))

        print("Question level: ",result[i][4],"\n")
                
        answer=int(input("Enter option number as answer: "))
        print("\n")

        if answer == int(result[i][2]):
            score += 1
    print("\n")
    print("You got",str(score),"/",str(len(result)),"correct.\n")