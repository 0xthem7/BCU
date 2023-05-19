class Vechicles:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        self.__state = 'stopped'

    def move(self):
        print("I am moving")
        self.__state = 'moving'

    def stop(self):
        print("I am stopped")
        self.__state = 'stopped'
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_state(self):
        return self.__state
    
    def __str__(self):
        return f"{self.get_make()} {self.get_model()} {self.get_state()}."


class Bus(Vechicles):
    '''
    Provide :
    make, model, decks, route, state, current_stop, 
    '''
    def __init__(self, make, model,decks, current_stop, route="New Street - Bullring - Moor Street - BCU"):
        Vechicles.__init__(self, make, model)
        self.__route = route
        self.__decks_no = decks
        self.__state = "Not in use"
        self.__current_stop = current_stop

    def set_decks_no(self,deck):
        self.__decks_no = deck
    
    def get_decks_no(self):
        return self.__decks_no

    def get_route(self):
        return self.__route
    
    def move(self,next_stop):
        if "BCU" in self.__current_stop:
            print("I am finished for today")
        else:
            print(f"The bus was at {self.__current_stop} and is moving to {next_stop}")
            self.__current_stop = next_stop

    def stop(self):
        print("I am non-stop Bus")


class Car(Vehicle):
    def __init__(self, make, model, doors):
        Vehicle.__init__(self, make, model)
        self.__doors_no = doors

    def set_doors_no(self, number):
        self.__doors_no = number

    def get_doors_no(self):
        return self.__doors_no

    def __str__(self):
        return f"{self.get_make()} {self.get_model()} with {self.get_doors_no()} doors is {self.get_state()}."


theM7 = Bus("bus","alpha",2,'New street', "New Street - Bullring - Moor Street - BCU")

theM7.set_decks_no(deck=4)
print(theM7.get_decks_no())
print(theM7.get_route())
theM7.move(next_stop="BCU")
theM7.move("Paradise")
theM7.stop()

