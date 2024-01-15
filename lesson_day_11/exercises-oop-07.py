class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_users(self):
        print(f'Hello my name is {self.first_name} {self.last_name}')
    
    def greet_user(self):
        print(f'Hello i am {self.first_name} {self.last_name}')
        



class Admin(User):
    privileges = []
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges
    
    def show_privileges(self):
        print('Priveleges:')
        for privelege in self.privileges:
            print(privelege)
    
Enkhaldar = Admin('Enkh', 'Aldar', ['can add post', 'can delete post', 'can ban user'])
Enkhaldar.describe_users()
Enkhaldar.show_privileges()