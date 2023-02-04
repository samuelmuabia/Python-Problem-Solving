# Write a program to accept an amount and find the number of notes. Assume that, Available
# notes are 1000,500,100,50,10,5,1 please keep in mind that to find the answer, you have to
# consider the highest value as the first priority.



def findNumberOfNotes(money):
    notes ={}
    moneyToNotes = money
    while moneyToNotes>0:
        if moneyToNotes >= 1000:
            notes[1000] = moneyToNotes//1000
            moneyToNotes = moneyToNotes%1000
        elif moneyToNotes >= 500:
            notes[500] = moneyToNotes//500
            moneyToNotes = moneyToNotes%500
        elif moneyToNotes >= 100:
            notes[100] = moneyToNotes//100
            moneyToNotes = moneyToNotes%100
        elif moneyToNotes >= 50:
            notes[50] = moneyToNotes//50
            moneyToNotes = moneyToNotes%50
        elif moneyToNotes >= 10:
            notes[10] = moneyToNotes//10
            moneyToNotes = moneyToNotes%10
        elif moneyToNotes >= 5:
            notes[5] = moneyToNotes//5
            moneyToNotes = moneyToNotes%5
        else:
            notes[1] = moneyToNotes
            moneyToNotes =0
    for note,item in notes.items():
        print(note,"->",item)



money = 868
findNumberOfNotes(money)



def findNumberOfNotes(money):
    notes = [1000, 500, 100, 50, 10, 5, 1]
    note_count = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(notes)):
        if money >= notes[i]:
            note_count[i] = money // notes[i]
            money = money % notes[i]

    for i in range(len(notes)):
        if note_count[i] > 0:
            print(f"{notes[i]} -> {note_count[i]}")

money = 868
findNumberOfNotes(money)
