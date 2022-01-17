from datetime import datetime

class Car:
    def __init__(self,color,model_name,serial_number,duration_of_existence, present_year = datetime.today().year):
        self.color = color
        self.model_name = model_name
        self.serial_number = serial_number
        self.duration_of_existence = duration_of_existence
        self.present_year = present_year
    def calc_expiry_year(self):
        return self.present_year + self.duration_of_existence
        
    def show_case(self):   
        print('The color of my car is: ', self.color,  'and the model name is : ', self.model_name,'which has a serial number of : ',
         self.serial_number, 'and will last for about: ',
          self.duration_of_existence, 'which is from present year to  ',self.calc_expiry_year() )
    




x =Car('blue', 'camry', 123456, 4)
y =Car('red', 'Forerunner', 123457, 6,)
z = Car('green','madza', 123458, 8)
x.show_case()
x.calc_expiry_year()
y.show_case()
y.calc_expiry_year()
z.show_case()
z.calc_expiry_year()