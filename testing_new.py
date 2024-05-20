
class MyRouter(object):
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
        
    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)
        
router1 = MyRouter('R1', '2600', '123456', '12.4') 
router1.serialno
router1.print_router("20150101")

getattr(router1, "ios") #getting the value of an attribute
setattr(router1, "ios", "12.1") #setting the value of an attribute
hasattr(router1, "ios") #checking if an object attribute exists
delattr(router1, "ios") #deleting an attribute
isinstance(router1, MyRouter) #verifying if an object is an instance of a particular class


