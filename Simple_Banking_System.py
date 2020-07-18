import math
import random

credit_cards = {}


# print menu
def menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. exit")
    choose = input()
    return choose


def menu_account():
    print("1. Balance")
    print("2. Log out")
    print("0. Exit")
    choose = input()
    return choose

def luhn(num):
    # multiply odd digits by 2
    i = 0
    number = []
    sum_number = 0
    for char in num:
        char = int(char)
        if i % 2 == 0:
            char = char * 2
        number.append(char)
        i += 1
    i = 0
    for char in number:
        if char > 9:
            char = char - 9
        number[i] = char
        i += 1
    for char in number:
        sum_number += char
    check_sum = int(round((math.ceil(sum_number / 10) - sum_number / 10), 1) * 10)
    return check_sum

def create_account():
    print("Your card has been created")
    # Credit number
    print("Your card number:")
    user_num = random.randint(99999999, 999999999)
    credit_card_num = "400000" + str(user_num)
    check_sum = luhn(credit_card_num)
    credit_card_num = "400000" + str(user_num) + str(check_sum)
    print(credit_card_num)

    # PIN card
    print("Your card PIN:")
    pin_card = random.randint(999, 9999)
    print(pin_card)

    # Add card to dict
    credit_cards[credit_card_num] = {}
    credit_cards[credit_card_num]["PIN"] = pin_card
    credit_cards[credit_card_num]["Balance"] = 0


def log_into():
    global credit_cards
    print("Enter your card number:")
    card_num = str(input())

    print("Enter your PIN::")
    PIN = int(input())

    if card_num in credit_cards:
        if credit_cards[card_num]["PIN"] == PIN:
            print("You have successfully logged in!")
            while True:
                choose = menu_account()
                if choose == "1":
                    print("Balance: {}".format(credit_cards[card_num]["Balance"]))
                elif choose == "2":
                    print("You have successfully logged out!")
                    break
                elif choose == "0":
                    print("Bye!")
                    exit()
        else:
            print("Wrong card number or PIN!")
    else:
        print("Wrong card number or PIN!")


while True:
    choose = menu()
    if choose == "1":
        create_account()
    elif choose == "2":
        log_into()
    elif choose == "0":
        print("Bye!")
        break

