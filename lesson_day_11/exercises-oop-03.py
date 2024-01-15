class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_users(self):
        print(f'Hello my name is {self.first_name} {self.last_name}')
    
    def greet_user(self):
        print(f'Hello i am {self.first_name} {self.last_name}')
        
Enkhaldar = User('Enkh', 'Aldar')
Enkhaldar.describe_users()
Enkhaldar.greet_user()