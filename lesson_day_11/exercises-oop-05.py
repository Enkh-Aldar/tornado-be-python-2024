class User:
    
    login_attemps = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_users(self):
        print(f'Hello my name is {self.first_name} {self.last_name}')
    
    def greet_user(self):
        print(f'Hello i am {self.first_name} {self.last_name}')
    
    def increment_login_attemps(self):
        self.login_attemps += 1
        print(f'Hello, {self.first_name} {self.last_name} your login attemps are {self.login_attemps} ')
         
    def reset_login_attemps(self):
        self.login_attemps = 0
        print(f'Hello your login attemps is {self.login_attemps}')     
    
Enkhaldar = User('Enkh', 'Aldar')
Enkhaldar.increment_login_attemps()
Enkhaldar.increment_login_attemps()
Enkhaldar.increment_login_attemps()
Enkhaldar.increment_login_attemps()
Enkhaldar.increment_login_attemps()
Enkhaldar.reset_login_attemps()