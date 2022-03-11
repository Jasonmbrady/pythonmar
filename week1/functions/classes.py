class Vehicle:
    def __init__(self, db_data):
        self.make = db_data['make']
        self.model = db_data['model']
        self.color = db_data['color']
        # self.max_speed = data['max_speed']
        # self.accel_rate = data['accel_rate']
    # Attribute: What describes your object
    # color:
    # max_speed:
    # accel_rate:
    # Method: What your object can do
    # accelerate:
    # decelrate:
    # turn_on_off:
    #"Chevy", "Equinox", "Black", 120, 10
my_car = {
    'make': "Chevy",
    'model': "Equinox",
    'color': "Black"
}
jason_car = Vehicle(my_car)
print(jason_car.make + " " + jason_car.model)