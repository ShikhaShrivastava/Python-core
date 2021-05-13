class Demo:
    count=0
    def __init__(self):
        Demo.count=Demo.count+1

    @classmethod
    def no_of_object(cls):
        print('No of object created', cls.count)

d1=Demo()
d2=Demo()
Demo.no_of_object()
d3=Demo()
d4=Demo()
d5=Demo()
Demo.no_of_object()
