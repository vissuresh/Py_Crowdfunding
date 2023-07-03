from models import *
import sqlite3

# conn = sqlite3.connect("funding.db")
# conn.execute("ALTER TABLE PROJECT RENAME COLUMN type TO category;")
# conn.close()


print("Crowdfunding Application")
user_status = int(input("1.Login\n2.Register\n : "))
email = input("Enter Email: ")
password = input("Enter Password: ")

if(user_status == 2):
    role = input("Enter role: ")
    if(role == "Admin"):
        user = Admin(email, password, role)

    elif role == "Donor":
        user = Donor(email, password, role)
    
    elif role == "Raiser":
        user = Raiser(email, password, role)

    user.save()

elif(user_status == 1): 
    user = User.get(email)

    if user.role == "Admin":
        admin = Admin(user.email, user.password)

        choice = int(input("1. View all projects\n2. Approve a project\n : "))

        if choice == 1:
            projects = Project.fetchall()
            for pr in projects:
                print(pr)


    elif user.role == "Donor":
        donor = Donor(user.email, user.password)

    elif user.role == "Raiser":
        raiser = Raiser(user.email, user.password)
        choice = int(input("1. Create Project\n : "))

        if choice == 1:
            deadline, target, emergency, category = input("Enter the following\nDeadline\tTarget\tEmergency\tCategory\n").split()
            raiser.createProject(deadline = deadline, target = target, category = category, emergency = emergency)
