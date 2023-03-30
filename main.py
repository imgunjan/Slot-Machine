# Importing the module in python
import random
from art import logo
# Global variable
MAX_LINE = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3


# Dictionary for the slot machinb
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_line.append(line+1)
    return winnings, winning_line

# Function for the slot machine spin


def get_slot_machine_spin(rows, cols, symbol):
    all_symbol = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    # colums = [[], [], []]
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


# Creating the deposit function where the user can deposit his or her amount


def deposit():
    """This function helps you to deposit the amount by the user and check weather the
    deposit amount is valids or invalid """
    while True:
        amount = input("What amount you want to deposit in the game:RS: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            # else:
            #     print("Please enter the valid amount it must be greater than 0")
        else:
            print("Please enter a number ")
    return amount

# Creating the function to check weather the lines that the user want to play is valid or not


def get_number_of_lines():
    """This function helps to check the number of line the user has input are valid to play 
    or not"""
    while True:
        lines = input(
            "Enter the number of lines you want to bet on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter the valid number of lines ")
        else:
            print("plesae enter the valid number of lines .")
    return lines

# Function to get the bet amount from the user


def get_bet():
    """This function helps user to get the bet amount and return it """
    while True:
        amount = input("Enter the amount you want to bet on each line. RS: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Enter the amount higher then Rs{MIN_BET}and not more then RS{MAX_BET}")
        else:
            print("Enter the the number ")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(
                f"You dont have enough amoun to bet, Your current balance is {balance} ")
        else:
            break
    print(
        f"You are betting RS{bet} on {lines} lines. Total bet will be rs{total_bet}  ")
    # print(balance, lines, bet)
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winngs_line = check_winning(slots, lines, bet, symbol_value)
    print(f"you won rs {winnings}.")
    print(f"you won on lines: ", *winngs_line)
    return winnings - total_bet


def main():
    print(logo)
    balance = deposit()
    while True:
        print(f"Your corrent balance is RS: {balance} ")
        play_game = input("Press enter to play (q to quit)")
        if play_game == "q":
            break
        balance += spin(balance)
    print(f"You left with RS:{balance}")


main()
