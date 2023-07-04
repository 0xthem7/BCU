class BMI:
    def __init__(self):
        '''Weight and Height'''
        self.__weight = 0
        self.__height = 0
        self.__BMI = 0.0

    def set_weight(self,w):
        self.__weight = w

    def set_height(self, h):
        self.__height = h

    def __cal_BMI(self):
        self.__BMI = self.__weight / (self.__height)**2
        return BMI

    def display_BMI(self):
        self.__cal_BMI()
        print("BMI : {:.2f}".format(self.__BMI))


x = BMI()
x.set_height(h=3)
x.set_weight(w=10)
x.display_BMI()
