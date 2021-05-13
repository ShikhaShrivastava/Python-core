'''Garbadge collector'''

#program to check the status
import gc
print("status of garbadge collector:",gc.isenabled())
gc.disable()
print("status of garbadge collector:",gc.isenabled())
gc.enable()
print("status of garbadge collector:",gc.isenabled())
print()

'''Destructor'''
import time
class Cricketer:
    def __init__(self):
        print('Constructor get executed')
        print('initializing the object')
    def __del__(self):
        print('Destructor got executed')
        print('Fulling last wish')
        print('cleaning the activities of the object')
print('Main Function')
sachin= Cricketer()
dravid=sachin
dhoni=dravid
del sachin
print('sachin ref got deleted')
time.sleep(5)
dravid=None
print('dravid ref got deleted')
time.sleep(5)
print('dhoni ref got deleted')
print('No ref pointing to object')
dhoni=None
time.sleep(5)
print('Termination of program')
print()


'''Example-2'''
#In List object we are creating 3 Cricketer object

class Cricketer:
    def __init__(self):
        print('Constructor get executed')
        print('initializing the object')
    def __del__(self):
        print('Destructor got executed')
        print('Fulling last wish')
        print('cleaning the activities of the object')
print('Main Function')
lst=[Cricketer(),Cricketer(),Cricketer()]
del lst
time.sleep(5)
print('Termination of program')
