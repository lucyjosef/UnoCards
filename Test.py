class Test:

    def __init__(self, ex):
        self.__exemple = ex

    def display(self):
        print(self.exemple)

    def __getExemple(self):
        print("Je passe par getExemple")
        return self.__exemple

    def __setExemple(self, val):
        print("Je passe par setExemple")
        self.__exemple = val

    exemple = property(__getExemple, __setExemple)
