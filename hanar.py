from string import digits,punctuation,ascii_uppercase
class Passwordf:
    def __init__(self,login,password):
        self.get_password=password #этим действием похоже что мы сделали self.get_password(password)
        self.login = login
    @property
    def get_password(self):
        return self.__password
    @staticmethod
    def upp(gan):
        for i in ascii_uppercase:
            if i in gan:
                return True
        return False
    @staticmethod
    def symbols(gan):
        for i in punctuation:
            if i in gan:
                return True
        return False
    @staticmethod
    def file_opp(vane):
        file = open('пароли.txt', encoding='UTF-8')
        for i in file:
            if i==vane+'\n':
                return False
        return True
    @staticmethod
    def diggey(gan):
        for i in digits:
            if i in gan:
                return True
        return False
    @get_password.setter
    def get_password(self,value):
        if not isinstance(value,str):
            raise ValueError('пароль должен быть ввиде строки')
        if len(value)<=4:
            raise ValueError('пароль должен быть больше четырёх символов')
        if len(value)>=18:
            raise ValueError('пароль должен быть меньше 18 символов')
        if Passwordf.diggey(value)==False:
            raise ValueError('должна быть хотя бы одна цыфра')
        if Passwordf.file_opp(value)==False:
            raise ValueError('пароль слишком слабый, придумайте другой')
        if Passwordf.symbols(value)==False:
            raise ValueError('должен быть хотя бы один символ в пароле')
        if Passwordf.upp(value)==False:
            raise ValueError('должен быть хотя бы один заглавный символ в пароле')
        self.__password=value
        print('пароль изменён')
    @property
    def change_name(self):
        if input('введите ваш пароль')!=self.__password:
            raise ValueError('доступ закрыт')
        self.login=input('введите ваш новый логин')
        return self.login
ka=Passwordf('hel','Hey98[b')
print(ka.change_name)
print(ka.__dict__)