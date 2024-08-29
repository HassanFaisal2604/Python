class Vehicle:
    def start_engine(self):
        print("This is an engine")

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        print("This is a truck")

# Create an instance of Truck
truck_instance = Truck()

# Call the start_engine method on the truck instance
truck_instance.start_engine()