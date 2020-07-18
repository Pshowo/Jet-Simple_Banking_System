import math
import random
import sqlite3
import os

credit_cards = {}


def create_table(cur):
    cur.execute(""""
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0
        );""")
    cur.commit()


# print menu
def menu():
    print("")
    print("1. Create an account")
    print("2. Log into account")
    print("0. exit")
    choose = input()
    return choose


def menu_account():
    print("")
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
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

    # Add card to database
    add_card_to_db(credit_card_num, pin_card)


def add_card_to_db(card_num, PIN):
    global id_card
    # Add to database
    conn = sqlite3.connect("card.s3db")
    cur = conn.cursor()
    sql_add_card = """
    INSERT INTO card (id, number, pin, balance) VALUES ({}, {}, {}, {})
    """.format(id_card, card_num, PIN, 0)
    cur.execute(sql_add_card)
    conn.commit()
    id_card += 1


def log_into(conn):
    global credit_cards
    print("Enter your card number:")
    card_num = str(input())

    cur = conn.cursor()
    cur.execute("SELECT number,PIN FROM card WHERE number='{}'".format(card_num))
    card_in_base = cur.fetchall()

    if len(card_in_base) == 1:
        print("Enter your PIN::")
        PIN = input()
        if PIN == card_in_base[0][1]:
            print("You have successfully logged in!")

            # In account
            while True:
                choose = menu_account()
                if choose == "1":  # balance
                    cur.execute("SELECT Balance FROM card WHERE number='{}'".format(card_num))
                    balance = cur.fetchall()
                    print("Balance: {}".format(balance[0][0]))

                    continue

                elif choose == "2":  # add income
                    print("Enter income:")
                    income = input()
                    cur.execute("UPDATE card SET balance=balance+{} WHERE number={}".format(income, card_num))
                    conn.commit()
                    print("Income was added!")
                    continue

                elif choose == '3':  # do transfer
                    print("Enter card number:")
                    other_card = input()
                    if other_card == card_num:
                        print("You can't transfer money to the same account!")
                    else:


                        if str(luhn(other_card[:-1])) == str(other_card[-1:]):
                            cur.execute("SELECT number FROM card WHERE number='{}'".format(other_card))
                            other_card = cur.fetchall()
                            cur.execute("SELECT balance FROM card WHERE number='{}'".format(card_num))
                            my_balance = cur.fetchall()[0][0]

                            if len(other_card) == 0:
                                print("Such a card does not exist.")
                            else:
                                print("Enter how much money you want to transfer:")
                                money = input()


                                if int(money) > int(my_balance):
                                    print('Not enough money!')
                                    continue
                                else:
                                    print(money, other_card[0][0])
                                    cur.execute(
                                        "UPDATE card SET balance=balance-{} WHERE number={}".format(money, card_num))
                                    cur.execute("UPDATE card SET balance=balance+{} WHERE number={}".format(money,
                                                                                                            other_card[0][
                                                                                                                0]))
                                    conn.commit()
                                    print("Success!")
                                    continue
                        else:
                            print("Probably you made mistake in the card number. Please try again!")
                elif choose == '4': # delete account
                    cur.execute("DELETE FROM card WHERE number={}".format(card_num))
                    conn.commit()
                    break

                elif choose == '5':
                    break

                elif choose == "0":
                    print("Bye!")
                    exit()
        else:
            print("Wrong card number or PIN!")
    else:
        print("Wrong card number or PIN!")


# ============


id_card = 0
conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
sql_create_table = """
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER
        );"""
cur.execute(sql_create_table)
conn.commit()

while True:
    choose = menu()
    if choose == "1":
        create_account()
    elif choose == "2":
        log_into(conn)
    elif choose == "0":
        print("Bye!")
        break
conn.commit()
conn.close()
