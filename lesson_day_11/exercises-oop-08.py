class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_users(self):
        print(f'Hello my name is {self.first_name} {self.last_name}')
    
    def greet_user(self):
        print(f'Hello i am {self.first_name} {self.last_name}')
        



class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
    
class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        print('Privileges:')
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)
        else:
            print('This user has no privileges.')
    
Enkhaldar = Admin('Enkh', 'Aldar')
Enkhaldar.describe_users()

# Enkhaldar.privileges.show_privileges()

Enkhaldar_privileges = ['can add post', 'can delete post', 'can ban user']

Enkhaldar.privileges.privileges = Enkhaldar_privileges

Enkhaldar.privileges.show_privileges()

