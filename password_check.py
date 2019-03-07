query = input("Please enter your password: ")
password = 'Ginger'
correct = False
counter = 0
while correct == False:
    if query == password:
        print("Password is correct.")
        correct = True
    else:
        print("Incorrect password. Please check and try again.")
        counter = counter+1
        print("You have entered an incorrect password",counter,"times.")
        query = input("Please enter your password: ")