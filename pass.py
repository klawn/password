query = input("Please enter your password: ")
password = 'Ginger'
correct = False
while correct == False:
    if query == password:
        print("Password is correct.")
        correct = True
    else:
        print("Incorrect password. Please check and try again.")
        query = input("Please enter your password: ")
