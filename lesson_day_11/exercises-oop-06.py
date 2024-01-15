class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f'This restaurant name is {self.restaurant_name} cuisine type is {self.cuisine_type}')
    

class IceCreamStand(Restaurant):
    flavors = []
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print('We have available flavors')
        for flavor in self.flavors:
            print(flavor)

IceCream = IceCreamStand('TESO', 'Mongolian', ['Vanilla', 'Chocolate', 'Milk'])
IceCream.describe_restaurant()
IceCream.show_flavors()