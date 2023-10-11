class Questions():
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer

q1=Questions('fastest language',['c#','python','java','c'],'c')
q2=Questions('common language',['c#','python','java','c'],'python')
q3=Questions('banking language',['c#','python','java','c'],'java')
listA=[q1,q2,q3]

#print(q1.checkAnswer('c'))

class Quiz():
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question=self.getQuestion()
        print(f'soru {self.questionIndex +1}-) {question.text}')

        for q in question.choices:
            print(q)       
        
        answer=input('answer:')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
             self.displayQuestion()

    def showScore(self):
        print('score', self.score)

quiz=Quiz(listA)
quiz.displayQuestion()

