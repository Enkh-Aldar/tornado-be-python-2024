class User:
    def __init__(self, first_name, last_name, email, expertise):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.expertise = expertise
        self.login_attempts = 0

    def describe_user(self):
        print("The current user's summary: " + self.first_name.title() +
              self.last_name.title() + ", " + self.email + "," + self.expertise)

    def greet_user(self):
        print("Hello " + self.first_name.title() + self.last_name.title())

    def increment_login_attempts(self, attempts):
        self.login_attempts = attempts

        if attempts >= self.increment_login_attempts:
            self.login_attempts = attempts

            if attempts <= 3:
                attempts += 1
                print (self.login_attempts)

            elif attempts > 3:
                print("You have tried too many times, device is locked.")

    def reset_login_attempts(self, attempts):
        self.login_attempts = 0
        print (self.login_attempts)

user1 = User("Aye", "Bee", "ab@gmail.com", "Computer Hardware")
user2 = User("Cee", "Dee", "cd@mozila.com", "Computer Networks")
user3 = User("Ee", "Eff", "ef@pillowz.com", "Operating Systems")

print("The Malware Analyst is " + user1.first_name.title() + ' ' + user1.last_name.title())
print("Her expertise is in " + user1.expertise)
print("Her email is " + user1.email) 
print("-------------------------------------")

print("The Security Engineer is " + user2.first_name.title() + ' ' + user2.last_name.title())
print("His expertise is in " + user2.expertise)
print("His email is " + user2.email)
print("-------------------------------------")

print("The Pen Tester is " + user3.first_name.title() + ' ' + user3.last_name.title()) 
print("His expertise is in " + user3.expertise)
print("His email is " + user3.email)

# What you are doing is incrementing the login attempts by using calling increment_login_attempts
user1.increment_login_attempts(33)
user1.reset_login_attempts(1)