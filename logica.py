class Logica:
    def __init__(self, lista=None):
        self.__lista = lista
    
    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self, value):
        self.__lista = value

    def par_impar(self, numero):
        fuera = numero % 2
        if fuera == 0:
            print('{} es par.'.format(numero))
        else:
            print('{} es impar.'.format(numero))
    
    def perfect(self, num):
        acu = 0
        for accountant in range(1, num):
            outc = num % accountant
            if outc == 0:
                acu += accountant
        if acu == num:
            print('{} es perfecto.'.format(num))
        else:
            print('{} no es perfecto.'.format(num))


class Ejercicio(Logica):
    def __init__(self, lista, num):
        super().__init__(lista)
        self.data = num
    
    def agregar(self, n1, n2):
        return n1 + n2
    
    def par_impar(self, numero):
        super().pair_odd(numero)
        return numero % 2


if __name__ == '__main__':
    ejer = Ejercicio([1, 3, 5], 20)
    if ejer.par_impar(6) == 0:
        print('Par')
    else:
        print('Impar')
    print(ejer.lista)
    print(ejer.agregar(4, 8))