from LexScanner import Lexico
class Sintatico():
    pilha = ""
    pilha2 = []
    ListaCadeias = []
    listaTokens = []

    def isE(self,token):
        if(token=='id' or token=='exp' or token=='('):
            self.pilha = self.pilha.replace("E","TE'",1)
        else:
            raise Exception('Erro sintático.')

            
    def isElinha(self,token):
        if(token == '+'):
            self.pilha = self.pilha.replace("E'","+TE'",1)
        elif(token == '-'):
            self.pilha = self.pilha.replace("E'","-TE'",1)
        elif(token == ')'):
            self.pilha = self.pilha.replace("E'","",1)
        elif(token == '$'):
            self.pilha = self.pilha.replace("E'","",1)
        else:
            raise Exception('Erro sintático.')


    def isT(self,token):  
        if(token=='id' or token=='exp' or token=='('):
            self.pilha = self.pilha.replace("T","PT'",1)
        else:
            raise Exception('Erro sintático.') 


    def isTlinha(self,token): 
        if(token=='+' or  token=='-' or  token==')' or  token=='$'):
            self.pilha = self.pilha.replace("T'","",1)
        elif(token=='/'):
            self.pilha = self.pilha.replace("T'","/PT'",1)
        elif(token=='*'):
            self.pilha = self.pilha.replace("T'","*PT'",1)
        else:
            raise Exception('Erro sintático.') 
        

    def isP(self,token):
        if(token=='id' or  token=='('):
            self.pilha = self.pilha.replace("P","FP'",1)
        elif(token=='exp'):
            self.pilha = self.pilha.replace("P","exp[F]",1)
        else:
            raise Exception('Erro sintático.') 


    def isPlinha(self,token):
        if(token=='+' or  token=='-' or  token=='/' or  token=='*' or  token==')' or  token=='$'):
            self.pilha = self.pilha.replace("P'","",1)
        elif(token=='^'):
            self.pilha = self.pilha.replace("P'","^FP'",1)
        else:
            raise Exception('Erro sintático.') 


    def isF(self,token): 
        if(token=='id'):
            self.pilha = self.pilha.replace("F", "id", 1)
        elif(token=='('):
            self.pilha = self.pilha.replace("F", "(E)", 1)
        else:
            raise Exception('Erro sintático.')


    def AvaliarSintaxe(self,path):
        lexico = Lexico(path)

        lista = []
        while not(lexico.isEOF()):
            token = lexico.nextToken()
            print(token.valor)
            if token.valor == "\n" and len(lista)>0:
                self.listaTokens.append(lista)
                lista = []
            elif token.valor not in  [' ','\t']:
                lista.append(token.valor)

        self.listaTokens.append(lista)
        
        print("tamanho lista : " + str(len(self.listaTokens)))
        print("lista: ",  self.listaTokens)
        for lista2 in self.listaTokens:
            self.cadeia = ''
            self.pilha = 'E$'
            print("lista entrada: " + str(lista2))
            for token in lista2:
                print(token)
                if (str(token).isnumeric() or '.' in token):
                    token = 'id'
                if ((self.pilha == '$') and (token == '$')):
                    break
                lista2.append("$")
                while not((self.pilha == '$') and (token == '$')):
                    # self.pilha COM INICIAL NÃO TERMINAL
                    if (self.pilha.startswith("E") and self.pilha[1] != "'"):
                        self.isE(token)
                    elif (self.pilha.startswith("E'")):
                        self.isElinha(token)
                    elif (self.pilha.startswith("T") and self.pilha[1] != "'"):
                        self.isT(token)
                    elif (self.pilha.startswith("T'")):
                        self.isTlinha(token)
                    elif (self.pilha.startswith("P") and self.pilha[1] != "'"):
                        self.isP(token)
                    elif(self.pilha.startswith("P'")):
                        self.isPlinha(token)
                    elif(self.pilha.startswith("F")):
                        self.isF(token)

                    # self.pilha COM INICIAL TERMINAL

                    elif(self.pilha.startswith("id")):
                        self.pilha = self.pilha.replace("id","", 1)
                        self.cadeia = self.cadeia + 'id'
                        break
                    elif(self.pilha.startswith("+")):
                        self.pilha = self.pilha.replace("+","", 1)
                        self.cadeia = self.cadeia + '+'
                        break
                    elif(self.pilha.startswith("-")):
                        self.pilha = self.pilha.replace("-","", 1)
                        self.cadeia = self.cadeia + '-'
                        break
                    elif(self.pilha.startswith("/")):
                        self.pilha = self.pilha.replace("/","", 1)
                        self.cadeia = self.cadeia + '/'
                        break
                    elif(self.pilha.startswith("*")):
                        self.pilha = self.pilha.replace("*","", 1)
                        self.cadeia = self.cadeia + '*'
                        break
                    elif(self.pilha.startswith("^")):
                        self.pilha = self.pilha.replace("^","", 1)
                        self.cadeia = self.cadeia + '^'
                        break
                    elif(self.pilha.startswith("exp")):
                        self.pilha = self.pilha.replace("exp","", 1)
                        self.cadeia = self.cadeia + 'exp'
                        break
                    elif(self.pilha.startswith("(")):
                        self.pilha = self.pilha.replace("(","", 1)
                        self.cadeia = self.cadeia + '('
                        break
                    elif(self.pilha.startswith(")")):
                        self.pilha = self.pilha.replace(")","", 1)
                        self.cadeia = self.cadeia + ')'
                        break
                    elif(self.pilha.startswith("[")):
                        self.pilha = self.pilha.replace("[","", 1)
                        self.cadeia = self.cadeia + '['
                        break
                    elif(self.pilha.startswith("]")):
                        self.pilha = self.pilha.replace("]","", 1)
                        self.cadeia = self.cadeia + ']'
                        break
                    elif(self.pilha.startswith("$")):
                        self.pilha = self.pilha.replace("$","", 1)
                        self.cadeia = self.cadeia + '$'
                        break   
            self.ListaCadeias.append(self.cadeia)
        

    
   
def main():


    
    sintatico = Sintatico()
    sintatico.AvaliarSintaxe('inputLexico.txt')
    
    print("self.cadeia aceita")
    
    
main()


