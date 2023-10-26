def addNote():
    name=input('name:')
    surname=input('surname:')
    midTerm=input('midTerm note:')
    final=input('final note:')
    with open('notes.txt','a+',encoding='utf-8') as file:
        file.write(f'{name} {surname} : {midTerm},{final}\n')
def calculateAverage(index):
    index=index[:-1]
    listA=index.split(':')
    name=listA[0]
    notes=listA[1]
    notes=notes.split(',')
    midterm=int(notes[0])
    final=int(notes[1])
    average=(midterm*0.4)+(final*0.6)
    if average>=90 and average<=100:
        letterGrade='AA'
    elif average>=80:
        letterGrade='BA'
    elif average>=70:
        letterGrade='BB'
    elif average>=60:
        letterGrade='CB'
    elif average>=50:
        letterGrade='CC'
    elif average>=40:
        letterGrade='DC'
    elif average>=30:
        letterGrade='DD'
    else:
        letterGrade='FF'
    return name+': '+ letterGrade
def showAverages():
    with open('notes.txt','r',encoding='utf-8') as file:
        for i in file:
            print(calculateAverage(i))
def saveNotes():
    listA=[]
    with open('notes.txt','r',encoding='utf-8') as file:
        for a in file:
            listA.append(calculateAverage(a))
        with open('letterGrade.txt','w',encoding='utf-8') as file2:
            for notes in listA:
                file2.write(notes+'\n')
choose=1
while choose!=4:
    print('1.Add Note\n2.Show Averages\n3.Save Notes\n4.Exit')
    choose=int(input('choose your process:'))
    if choose==1:
        addNote()
    elif choose==2:
        showAverages()
    elif choose==3:
        saveNotes()
    elif choose==4:
        print('exiting...')
    else:
        print('incorrect value enterred')