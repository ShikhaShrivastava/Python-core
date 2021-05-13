class Unifiedcourse:
    def __init__(self):
        self.__maxprice=35000

    def set_maxprice(self,max):
        if max==35000:
            self.__maxprice = max
        else:
            print('Price is being changed,Prevent')

    def get_maxprice(self):
        return self.__maxprice

if __name__=='__main__':
    uc=Unifiedcourse()
    print(uc.get_maxprice())
    uc.set_maxprice(3500)
    print(uc.get_maxprice())
    uc._Unifiedcourse__maxprice =350000 #data mangling
    print(uc.get_maxprice())


