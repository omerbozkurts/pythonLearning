# Try to find a randomly generated number between 1 and 100 with more or less expressions
    #Score out of 100, 20 points for each question
    #in the next stage, take the lifes information from the user and calculate the score accordingly

import random

number=(random.randrange(0,100))
score=100
lifes=score/int(input('enter your lifes number:'))
usrPrediction=int(input('your guess:'))
predictNum=0

while number!=usrPrediction:
    print('your guess is not true')
    predictNum+=1
    score-=lifes
    if(number<usrPrediction):
        print('down')
        usrPrediction=int(input('your guess:'))
    else:
        print('up')
        usrPrediction=int(input('your guess:'))

print(f'congratulations your guess is correct number is {number} and your predict num is {predictNum} and your score is {score}')

