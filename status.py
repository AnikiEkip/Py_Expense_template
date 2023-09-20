from PyInquirer import prompt
import csv



def show_status():
    all_users = []
    f = open("users.csv", "r")
    for line in f:
        user = line.strip('\n')
        all_users.append([user, 0])

    with open('expense.csv', mode="r") as file:
        reader = csv.reader(file)

        next(reader, None)

        for row in reader:
            price = float(row[0])
            cash = row[2]
            remb = row[3]

            number = 0
            if (cash in remb):
                number = remb.len(-1)
            else:
                number = remb.len()
            unit_price = price / number
            for user in all_users:
                for name in remb:
                    if (cash != name):
                        if (name == user[0]):
                            user[1]+=unit_price
            for user in all_users:
                if (user[0] == cash):
                    print("%s owes nothing", user[0])
                else:
                    print("%s owes %d to %s", user[0], user[1], cash)                    
