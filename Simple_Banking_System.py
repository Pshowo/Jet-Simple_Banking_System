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


def create_account():
    print("Your card has been created")
    # Credit number
    print("Your card number:")
    user_num = random.randint(000000000, 999999999)
    check_sum = 3
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
                    exit
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

