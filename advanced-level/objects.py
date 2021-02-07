class MyRouter(object):
    "This is a class that describes the characteristics of a router."

    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is:  ", self.routername)
        print("The router model is:  ", self.model)
        print("The serial number of:  ", self.serialno)
        print("The IOS version is:  ", self.ios)
        print("The model and date combined:  ", self.model + manuf_date)


router1 = MyRouter('R1', '2600', '123456', '12.4')

router1

router1.model

router1.ios

router1.serialno

router1.routername

router1.print_router("20181010")

router2 = MyRouter('R2', '7200', '101010', '12.20')

router2

router2.model

router2.ios

router2.serialno

router2.routername

router2.print_router("20190101")

router2.ios

router2.ios = "12.3"

router2.ios

setattr(router2, "ios", "12.1")

getattr(router2, "ios")

hasattr(router2, "ios")  # should return true

hasattr(router2, "ios2")  # should return false

getattr(router2, "ios")  # will return error

isinstance(router2, MyRouter)
