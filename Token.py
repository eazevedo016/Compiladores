from enum import Enum
from tokenize import String


class TipoToken(Enum):

    # numeros naturais = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numero = 0

    # numero real
    numeroReal = 1

    # operacoes = ['+','-','*','/','^','exp']
    operador = 2

    # precedencia = ['(',')','[',']']
    precedencia = 3

    # espacos = ['\n', '\t', '']
    espacos = 4


class Token():
    tipo: TipoToken
    valor: str

    def toString(self):
        if(self.valor=='\n'):
            return "Token[" + str(self.tipo) + ", " + "\\" + "n" + "]"
        elif(self.valor=='\t'):
            return "Token[" + str(self.tipo) + ", " + "\\" + "t" + "]"
        return "Token[" + str(self.tipo) + ", " + str(self.valor) + "]"




