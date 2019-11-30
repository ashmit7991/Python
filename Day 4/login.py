Users = {
    "Sachin": "1234",
    "Dravid": "4567",
    "Virat": "9876",
    "Dhoni": "0000",
}

userName = input("Enter Username:")
password = input("Enter Password:")


class userNotFound(Exception):
    def __init__(self, message="Username or Password is incorrect"):
        Exception.__init__(self, message)


try:
    for user in Users:
        if user == userName and Users[user] == password:
            print("LoggedIn successfully")
            exit()
    raise userNotFound

except userNotFound as e:
    print(e)
except Exception as e:
    print("This is generic exception :", e)