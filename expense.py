from PyInquirer import prompt
import csv





def new_expense(*args):
    all_users = []
    checkbox_choices = []

    f = open("users.csv", "r")
    for line in f:
            user = line.strip('\n')
            all_users.append(user)
            checkbox_choices.append({"name": user, "checked":True})



    expense_questions = [
        {
            "type":"input",
            "name":"amount",
            "message":"New Expense - Amount: ",
        },
        {
            "type":"input",
            "name":"label",
            "message":"New Expense - Label: ",
        },
        {
            "type":"list",
            "name":"spender",
            "message":"New Expense - Spender: ",
            "choices": all_users,
        },
        {
            "type":"checkbox",
            "name":"payback",
            "message":"New Expense - Involved peoples: ",
            "choices": checkbox_choices,
        },
    ]

    infos = prompt(expense_questions)
    with open('expense.csv', mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=infos.keys())
        writer.writerow(infos)
    return True


