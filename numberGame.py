class Math:
    def __init__(self, name):
        print('Welcome to number checker '+name+'!')
        self.playerName = name

    def square(self, i):
        print('Good choice ' + self.playerName)
        return 'The square of your number is ' + str(i*i)

    def isEven(self, i):
        if (type(i) == int and i%2 == 0):
            print('Well, ' + self.playerName + ', you choose well.')
            return 'Your number is even.'
        elif(type(i) == float):
            msg = str(i) + " is not an integer so it can't be even or odd"
            return msg
        else:
            return 'Your number is odd'

    def isFloat(self, i):
        if ('.' in i):
            period = i.index('.')
            cleaned = i[:period] + i[period+1:]
        else:
            cleaned = i

        if (cleaned.isnumeric() == True):
            print('A float eh, '+  self.playerName + '? Interesting choice.')
            return True
        else:
            return False

name = input('Please enter your name... ')
math = Math(name)

def userInput():
    def enterNumber():
        valid = False
        while (valid == False):
            number = input('Enter a number... ')

            if (number.isnumeric() == True):
                return int(number)
            else:
                valid = math.isFloat(number)

            if(valid == True):
                return float(number)
            else:
                print(math.playerName+ ', please enter a number')

    number = enterNumber()
    operator = input('Do you want to know if it is even or the square? ')

    valid = True

    if (operator == 'even'):
        msg = math.isEven(number)

    elif (operator == 'square'):
        msg = math.square(number)

    else:
        msg = 'Please enter a number and either "even" or "square"'
        valid = False

    print(msg)

    if (valid == False):
        userInput()

playing = True
playState = True
while (playing == True):
    if (playState == True):
        userInput()

    replay = input('Play again? ')

    if (replay == 'yes'):
        playState = True
        changePlayer = input('Switch players? ')
        if (changePlayer == 'yes'):
            newPlayer = input('Enter new player name... ')
            math = Math(newPlayer)

    elif(replay == 'no'):
        print('Thanks for playing!')
        playing = False
    else:
        playState = False
        print('Enter "yes" or "no"')

