# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing
# in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
#
# Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets
# strictly in the order people queue?
#
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
# Otherwise return NO.


def tickets(people_list):
    vasya_money = 0
    ticket_price = 25
    sold_tickets = 0
    bill_25 = 0
    bill_50 = 0
    bill_100 = 0
    all_people_handled = True

    for each_item in tickets_list:
        if each_item == 25:
            bill_25 += 1
            vasya_money += ticket_price
            sold_tickets += 1
        elif each_item == 50:
            if bill_25 >= 1:
                bill_25 -= 1
                bill_50 += 1
                vasya_money += ticket_price
                sold_tickets += 1
            else:
                all_people_handled = False
                return "NO"
        elif each_item == 100:
            if bill_25 >= 1 and bill_50 >= 1:
                bill_25 -= 1
                bill_50 -= 1
                bill_100 += 1
                vasya_money += ticket_price
                sold_tickets += 1
            elif bill_25 >= 3:
                bill_25 -= 3
                bill_100 += 1
                vasya_money += ticket_price
                sold_tickets += 1
            else:
                all_people_handled = False
                return "NO"

    if all_people_handled:
        return "YES"


tickets_list = [int(x) for x in input().split(" ")]
print(tickets(tickets_list))

