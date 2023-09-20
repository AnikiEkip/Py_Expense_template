from PyInquirer import prompt
user_questions = [

]

def add_user():
    name = input('What is your user name?\n')
    f = open("users.csv", "a")
    f.write(name)
    f.close()