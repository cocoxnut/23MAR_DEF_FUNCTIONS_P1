def user_file():
    user = input("Enter name of your file: ")
    with open(user, 'w') as db:
        db.write(user)
user_file()