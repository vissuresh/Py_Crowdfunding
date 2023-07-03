import sqlite3

class User():
    email, password, role = None, None, None

    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role
        
    def save(self):
        conn = sqlite3.connect("funding.db")
        conn.execute("INSERT INTO USER VALUES ('{}', '{}', '{}')".format(self.email, self.password, self.role))

        conn.commit()
        conn.close()

    def view_projects():
        conn = sqlite3.connect("funding.db")

        result = conn.execute('''SELECT * FROM PROJECTS where is_active = 1;''').fetchall()

        conn.close()
        return result
        
    
    def get(email):
        conn = sqlite3.connect("funding.db")

        result = conn.execute('''SELECT * FROM USER where email = ?;''',(email,)).fetchone()

        user = User(result[0], result[1], result[2])

        conn.close()
        return user
        

class Admin(User):
    def __init__(self, email, password):
        super().__init__(email, password, "Admin")

    def view_account():
        pass

    def review(project):
        return True

class Donor(User):
    def __init__(self, email, password):
        super().__init__(email, password, "Donor")
        
    def make_donation(self, proj_id, amount):
        pass

class Raiser(User):
    def __init__(self, email, password):
        super().__init__(email, password, "Raiser")

    def createProject(self, deadline, target, category, emergency):
        project = Project(self.email, deadline, target, category, emergency)
        project.save()


class Project():
    #Class variable
    conn = sqlite3.connect("funding.db")
    id = conn.execute("SELECT MAX(id) FROM Project;").fetchone()[0] + 1
    conn.close()

    def __init__(self, user_id, deadline, target, category, emergency):
        self.id = Project.id
        Project.id +=1

        self.user_id = user_id
        self.deadline = deadline
        self.target = target
        self.collected = 0
        self.category = category
        self.emergency = emergency

    def save(self):
        conn = sqlite3.connect("funding.db")
        conn.execute("INSERT INTO PROJECT(id, user_id, deadline, target, collected, is_emergency, is_active, category ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(self.id, self.user_id, self.deadline, self.target, 0, self.emergency, 0, self.category))

        conn.commit()
        conn.close()

    def fetchall():
        conn = sqlite3.connect("funding.db")
        result = conn.execute("SELECT * FROM PROJECT;").fetchall()
        conn.close()

        return result