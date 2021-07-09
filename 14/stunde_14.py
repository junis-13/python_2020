


fruits = ['apple', 'banana', 'kiwi', 'dragonfruit']
years = [2012,  2013,  2014,  2015]
computer_class = ['Alex', 78, 42, 'Ramin', 98]

print(fruits)
print(years)
print(computer_class)





fruits.append('orange')

fruits.remove('dragonfruit')

for fruit in fruits:
    print('I see  ' + fruit  +  '.')


colors = ['blue', 'yellow', 'green', 'purple', 'red']
for color in colors:
    print('I see  ' + color +  '.')

    players = ['player1', 'player2']
    player1 = ['name1', 'score1', 'backpack1']
    player2 = ['name2', 'score2', 'backpack2']
    backpack1 = ['sword', 'book', 'meat', 'magic stone']
    backpack2 = ['bow', 'helmet', 'shield', 'knife']

    for item in backpack1:
        print('I see  ' + item + '.')

    for item in backpack2:
        print('I see  ' + item + '.')

        player1name = input("wie soll spieler 1 heißen?")
        player2name = input("wie soll spieler 2 heißen?")
        backpack1 = input("was für items soll spieler eins in seinem rucksack haben?")
        backpack2 = input("was für items soll spieler zwei in seinem rucksack haben?")

        players = ['player1', 'player2']
        player1 = ['name1', 'score1', 'backpack1']
        player2 = ['name2', 'score2', 'backpack2']
        backpack1 = ['sword', 'book', 'meat', 'magic stone']
        backpack2 = ['bow', 'helmet', 'shield', 'knife']

        qu = input("welche werte werte willst du wissen?")
        if (qu == "keine"):
            quit
        elif (qu == "player1"):
            for wert in player1:
                print('I see  ' + wert + '.')


        elif (qu == "player2"):
            for wert in player2:
                print('I see  ' + wert + '.')

        elif (qu == "backpack1"):
            for wert in backpack1:
                print('I see  ' + wert + '.')

        elif (qu == "backpack2"):
            for wert in backpack2:
                print('I see  ' + wert + '.')