class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f'This restaurant name is {self.restaurant_name} cuisine type is {self.cuisine_type}')
    
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open at 10am')



Altangadas = Restaurant('Altan Gadas', 'Mongoliin undesnii hool')
Altangadas.open_restaurant()
Altangadas.describe_restaurant()

Yuna = Restaurant('Yuna', 'Korean')
Yuna.open_restaurant()
Yuna.describe_restaurant()