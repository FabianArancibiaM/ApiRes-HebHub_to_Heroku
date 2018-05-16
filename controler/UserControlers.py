
import model.ClassUsers

class UserControler:

    def __init__(self,name, password):
        self.__user = model.ClassUsers.User(name,password)
    def validarUser(self):
        return self.__user.validar()