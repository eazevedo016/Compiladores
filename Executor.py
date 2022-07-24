from math import exp

class Executor():
    pilha = []


    def executarOperacao(self, pilhaCodigo):
        for caracter in pilhaCodigo:
            if (str(caracter).isnumeric() or '.' in caracter):
                self.pilha.append(float(caracter))
            elif(caracter == '+'):
                a = self.pilha.pop(-2)
                b = self.pilha.pop(-1)
                self.pilha.append(a+b)
            elif(caracter == '-'):
                a = self.pilha.pop(-2)
                b = self.pilha.pop(-1)
                self.pilha.append(a-b)
            elif(caracter == '*'):
                a = self.pilha.pop(-2)
                b = self.pilha.pop(-1)
                self.pilha.append(a*b)
            elif(caracter == '/'):
                a = self.pilha.pop(-2)
                b = self.pilha.pop(-1)
                self.pilha.append(a/b)
            elif(caracter == '^'):
                a = self.pilha.pop(-2)
                b = self.pilha.pop(-1)
                self.pilha.append(a**b)
            elif(caracter == 'exp'):
                b = self.pilha.pop(-1)
                self.pilha.append(exp(b))
        result = self.pilha[0]
        self.pilha = []
        return result

             
             
#executor = Executor()
#executor.executarOperacao(['1.45', '5', '4.5', '*', '+'])



#[23.95,]