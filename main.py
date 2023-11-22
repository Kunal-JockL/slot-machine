import random

from mysqlx import Column

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROW = 3
COL = 3

reelSymbols = {
    "$" : 2,
    "#" : 3,
    "&" : 5,
    "#" : 8
}

def spin( rows, cols, sym):
    allSym = []
    for symbol, symbolcnt in sym.items():
        for _ in range(symbolcnt):
            allSym.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        

def deposit():
    while True:
        amount = input("What would u like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount has to be greater than zero")
        else:
            print("Please enter a number")
    return amount

def getLines():
    while True:
        lines = input("Enter number of lines to bet on ( 1 - " + str (MAX_LINES) + ") ?")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines > 0:
                break
            else:
                print("Lines has to be greater than zero")
        else:
            print("Please enter a number")
    return lines

def getBet():
    while True:
        amount = input("What would u like to BET on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("BET has to be greater than zero and less than " + str(MAX_BET))
        else:
            print("Please enter a number")
    return amount

def main():
    balance = deposit()
    lines = getLines()

    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet >= balance:
            print("Low balance\n")
        else:
            break


    print(f"Your balance is ${balance} \nYou have chosen to bet on ${lines} lines \nYou have bet $ ${bet} on each line, Which is a total of ${totalBet}")


main()