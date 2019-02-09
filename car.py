
# example class (car) static data

class car:          # class name
    def __init__(self):     #  here defining a constructor
        self.name="Maruti Suzuki"
        self.model="00M3"       # this are the static variables
        self.engine="UI9089"
        self.speed="80km/hr"
    def car(self):      # creating a method of car class
        print(self.name)    # printing the values
        print(self.model)
        print(self.engine)
        print(self.speed)
c=car()
c.car()


