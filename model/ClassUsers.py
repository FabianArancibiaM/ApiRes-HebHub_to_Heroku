class User:

    def __init__(self,name, password):
        self.__name =name
        self.__password = password

    def printUser(self):
        print('name: {} and password {}'.format(self.__name,self.__password))

    def validar(self):
        if self.__name == 'admin' and self.__password == 'admin':
            return True
        else:
            return False