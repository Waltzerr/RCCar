from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_left(self, value):
       print("debug")


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()