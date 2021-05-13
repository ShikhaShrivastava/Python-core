import time
from abc import *


class Printer(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Hpprinter(Printer):
    def start(self, text):
        time.sleep(5)
        print('Hp printer started to print')
        time.sleep(5)
        print(text)

    def stop(self):
        print('Hp printer has stopped printing')


class Epsonprinter(Printer):
    def start(self, text):
        time.sleep(5)
        print('Epson printer started to print')
        time.sleep(5)
        print(text)
        time.sleep(5)

    def stop(self):
        print('Epson printer has stopped printing')


if __name__ == '__main___':
    print('Select the printer from below option\n Hpprinter \nEpsonprinter')
    myprinter = input('Enter the printername\n')
    classname = globals()[myprinter]
    ref = classname()
    ref.start('This printer is one of the best printer')
    ref.stop()
