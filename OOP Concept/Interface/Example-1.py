from abc import *


class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class Oracle(DatabaseInterface):
    @abstractmethod
    def connect(self):
        print('connecting to Oracle Database')

    @abstractmethod
    def disconnect(self):
        print('disconnecting to Oracle Database')


class MySQL(DatabaseInterface):
    @abstractmethod
    def connect(self):
        print('connecting to Mysql Database')

    @abstractmethod
    def disconnect(self):
        print('Diconnecting to Mysql Database')


if __name__ == '__main__':
    print(issubclass(Oracle, DatabaseInterface))
    print(issubclass(MySQL, DatabaseInterface))
    print('select the database name given below \n Oracle \n MySQL')
    database = input('Enter the database name:-')
    print(globals())
    # ref=database()--->TYPE ERROR
    classname = globals()[database]
    print(classname)
    ref = classname()
    ref.connect()
    ref.disconnect()


