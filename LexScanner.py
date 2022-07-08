from xml.etree.ElementTree import tostring
from Token import Token,TipoToken

class Lexico():

    def __init__(self, caminhoArquivo):
        with open(caminhoArquivo,'r') as arquivo:
            self.conteudo = arquivo.read()
            self.pos = 0
    linha = 1
    

    def nextToken(self):
        
        valor = ''
        token = None
        estado = 0
        if(not self.pos == 0):
            self.backChar()
        
        while(True):

            c = self.nextChar()
           
            if(self.isEOF()):
                return None
           
            # ESTADO 0 
            if (estado == 0):
                if(self.isNumero(c)):
                    estado = 1
                    valor = valor + c
                elif (self.isOperador(c)):
                    estado = 5
                    valor += c
                elif (self.isPreced(c)):
                    estado = 6
                    valor += c
                elif (self.isEspaco(c)):
                    estado = 10
                    # continue
                    valor += c
                elif (self.isEletter(c)):
                    estado = 7
                    valor += c
                else:
                    raise Exception(f"Token não reconhecido. Linha: {self.linha} Posição: {self.pos - 1} Token: {valor}")
                continue


            # ESTADO 1
            if(estado == 1):
                if(self.isNumero(c)):
                    estado = 1
                    valor += c
                    continue
                elif(self.isPonto(c)):
                    estado = 2
                    valor += c
                else:
                    estado = 4
            
            # ESTADO 2
            if(estado == 2):
                if(self.isNumero(c)):
                    estado = 2
                    valor += c
                else:
                    estado = 3
                    valor += c
            
            # ESTADO 3
            if(estado == 3):
                token = Token()

                # atribui o valor e tipo de token
                token.tipo = TipoToken.numeroReal
                token.valor = valor

                return token.toString()

            # ESTADO 4
            if(estado == 4):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.numero
                token.valor = valor
               
                return token.toString()

            # ESTADO 5
            if(estado == 5):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.operador
                token.valor = valor

                return token.toString()

            # ESTADO 6
            if(estado == 6):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.precedencia
                token.valor = str(valor)

                return token.toString()

            # ESTADO 7
            if(estado == 7):
                if(self.isXletter(c)):
                    estado = 8
                    valor += c
                    continue
                else:
                    raise Exception(f"Token não reconhecido. Linha: {self.linha} Posição: {self.pos - 1} Token: {valor}")
                    

            # ESTADO 8
            if(estado == 8):
                if(self.isPletter(c)):
                    estado = 9
                    valor += c
                    continue
                else:
                    raise Exception(f"Token não reconhecido. Linha: {self.linha} Posição: {self.pos - 1} Token: {valor}")

            # ESTADO 9
            if(estado == 9):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.operador
                token.valor = valor

                return token.toString()

            # ESTADO 10
            if(estado == 10):
                token = Token()
                
                # atribui o valor e tipo de token
                token.tipo = TipoToken.espacos
                token.valor = valor

                return token.toString()


    # POSSIBILIDADES QUE LEVAM A UM ESTADO X
    def isNumero(self,c):
        return (c>= '0' and c <='9')

    def isOperador(self, c):
        return (c == '+' or c == '-' or c == '*' or c == '/' or c == '^')

    def isPreced(self,c):
        return (c == '(' or c == ')' or c == '[' or c == ']')

    def isEletter(self,c):
        return (c == 'e')

    def isXletter(self,c):
        return (c =='x')

    def isPletter(self,c):
        return (c =='p')

    def isPonto(self, c):
        return (c == '.')
    
    def isEspaco(self,c):
        if (c == '\n'):
            self.linha+=1
        return (c == '\n' or c == '\t' or c == ' ')



    
    # verificar se chegou ao fim da fita
    def isEOF(self):
        return self.pos == len(self.conteudo)

    # anda na fita
    def nextChar(self):
        if(self.isEOF()):
            return 0
        aux = self.pos
        self.pos += 1
        return self.conteudo[aux]
    
    # volta na fita
    def backChar(self):
        if(not self.isEOF()):
            self.pos -= 1

    
def main():
    token = Lexico('inputLexico.txt')
    while not(token.isEOF()):
        print(token.nextToken())

main()
    



