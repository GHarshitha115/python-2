class Bike:
    def __init__(self, model_name, acceleration):
        self.model_name = model_name
        self.acceleration = acceleration
        self.current_speed = 0
        self.color = "black"

    #def accelerate(self):
     #   self.current_speed += self.acceleration


def get_bike_object_color(bike_object):
    return bike_object.color
    # TODO: Fill code here
    #pass


def get_bike_object_current_speed(bike_object):
    return bike_object.current_speed
    # TODO: Fill code here
    pass


def change_bike_color(bike_object, new_color):
    bike_object.color=new_color
    
    # TODO: Fill code here
    pass


def increase_bike_speed(bike_object):
    bike_object.current_speed=bike_object.acceleration
    #return bike_object.current_speed
    # TODO: Fill code here
    pass


if __name__ == "__main__":
    model_name = input()
    acceleration = float(input())
    color = input()

    bike = Bike(model_name=model_name, acceleration=acceleration)
    print(get_bike_object_color(bike))

    print(get_bike_object_current_speed(bike))

    change_bike_color(bike, color)
    print(get_bike_object_color(bike))

    increase_bike_speed(bike)
    print(get_bike_object_current_speed(bike))
