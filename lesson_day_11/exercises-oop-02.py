class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, open_time):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_time = open_time
        
    def describe_restaurant(self):
        print(f'This restaurant name is {self.restaurant_name} cuisine type is {self.cuisine_type}. This restaurant open at {self.open_time}.')
    
    # def open_restaurant(self):
    #     print(f'{self.restaurant_name} is open at 10am')



Altangadas = Restaurant('Altan Gadas', 'Mongoliin undesnii hool', '09am')
# Altangadas.open_restaurant()
Altangadas.describe_restaurant()

Yuna = Restaurant('Yuna', 'Korean Traditional', '09am')
# Yuna.open_restaurant()
Yuna.describe_restaurant()