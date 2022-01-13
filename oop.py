import datetime
class Car:
    def __init__(self,color,model_name,serial_number,duration_of_existence ):
        self.color = color
        self.model_name = model_name
        self.serial_number = serial_number
        self.duration_of_existence = duration_of_existence
    def show_case(self):
        print('The color of my car is: ', self.color,  'and the model name is : ', self.model_name,'which has a serial number of : ',
         self.serial_number, 'and will last for about: ',  self.duration_of_existence, 'which from ',
          present_date, 'to ',  future_date )


present_date =datetime.datetime.today()
print('present_date',str(present_date))

future_date =present_date + datetime.timedelta(days =1460)
print('future_date_4years:', str(future_date))
print(future_date-present_date) 


x =Car('blue', 'camry', 123456, '4 years ')
x.show_case()

class Car2:
        def __init__(self,color,model_name,serial_number,duration_of_existence ):
             self.color = color
             self.model_name = model_name
             self.serial_number = serial_number
             self.duration_of_existence = duration_of_existence

        def show_out(self):
            print('The color of my car is: ', self.color,  'and the model name is : ', self.model_name,'which has a serial number of : ',
            self.serial_number, 'and will last for about: ',  self.duration_of_existence, 'which from ',
          present_date, 'to ',  future_date )


present_date =datetime.datetime.today()
print('present_date',str(present_date))

future_date =present_date + datetime.timedelta(days =2190)
print('future_date_6years:', str(future_date))
print(future_date-present_date) 


x =Car2('red', 'forerunner', 123457, '6 years ')
x.show_out()

class Car3:
    def __init__(self,color,model_name,serial_number,duration_of_existence ):
        self.color = color
        self.model_name = model_name
        self.serial_number = serial_number
        self.duration_of_existence = duration_of_existence
    

    def show_forth(self):
            print('The color of my car is: ', self.color,  'and the model name is : ', self.model_name,'which has a serial number of : ',
            self.serial_number, 'and will last for about: ',  self.duration_of_existence, 'which from ',
          present_date, 'to ',  future_date )


present_date =datetime.datetime.today()
print('present_date',str(present_date))

future_date =present_date + datetime.timedelta(days =1095)
print('future_date_3years:', str(future_date))
print(future_date-present_date) 


x =Car3('green', 'mazda', 123458, '3 years ')
x.show_forth()

              