class Restaurant:
     
    number_served = 0
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'This restaurant name is {self.restaurant_name} cuisine type is {self.cuisine_type}')
    
    def set_number_served(self, number):
        self.number_served = number

        print(f'{self.restaurant_name} is customer is {self.number_served} ')


    def increment_number_served(self):
        self.number_served += 1
        print(f'{self.restaurant_name} is customer is {self.number_served} ')
        
Altangas = Restaurant('Altangadas', 'Mongolian Traditional')
Altangas.describe_restaurant()
Altangas.set_number_served(3)
Altangas.set_number_served(2)
Altangas.set_number_served(1)
Altangas.increment_number_served()

