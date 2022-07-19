def isE(token):
    global pilha 
    if(token=='id'):
        pilha = pilha.replace("E","TE'",1)
    elif(token=='exp'):
        pilha = pilha.replace("E","TE'",1)
    elif(token=='('):
        pilha = pilha.replace("E","TE'",1)
    else:
        raise Exception('Erro sintático.')

        
def isElinha(token):
    global pilha 
    if(token == '+'):
        pilha = pilha.replace("E'","+TE'",1)
    elif(token == '-'):
        pilha = pilha.replace("E'","-TE'",1)
    elif(token == ')'):
        pilha = pilha.replace("E'","",1)
    elif(token == '$'):
        pilha = pilha.replace("E'","",1)
    else:
        raise Exception('Erro sintático.')


def isT(token): 
    global pilha 
    if(token=='id'):
        pilha = pilha.replace("T","PT'",1)
    elif(token=='exp'):
        pilha = pilha.replace("T","PT'",1)
    elif(token=='('):
        pilha = pilha.replace("T","PT'",1)
    else:
        raise Exception('Erro sintático.') 


def isTlinha(token):
    global pilha 
    if(token=='+' or  token=='-' or  token==')' or  token=='$'):
        pilha = pilha.replace("T'","",1)
    elif(token=='/'):
        pilha = pilha.replace("T'","/PT'",1)
    elif(token=='*'):
        pilha = pilha.replace("T'","*PT'",1)
    else:
        raise Exception('Erro sintático.') 
    

def isP(token):
    global pilha 
    if(token=='id' or  token=='('):
        pilha = pilha.replace("P","FP'",1)
    elif(token=='exp'):
        pilha = pilha.replace("P'","exp[F]",1)
    else:
        raise Exception('Erro sintático.') 


def isPlinha(token):
    global pilha 
    if(token=='+' or  token=='-' or  token=='/' or  token=='*' or  token==')' or  token=='$'):
        pilha = pilha.replace("P'","",1)
    elif(token=='^'):
        pilha = pilha.replace("P'","^FP'",1)
    else:
        raise Exception('Erro sintático.') 


def isF(token):
    global pilha 
    if(token=='id'):
        pilha = pilha.replace("F", "id", 1)
    elif(token=='('):
        pilha = pilha.replace("F", "(E)", 1)
    else:
        raise Exception('Erro sintático.')


def Sintatico(tokenList):

    global pilha 
    global cadeia

    pilha = 'E$'
    cadeia = ''

    for token in tokenList:
        if ((pilha == '$') and (token == '$')):
            break
        tokenList.append("$")
        while not((pilha == '$') and (token == '$')):

            # PILHA COM INICIAL NÃO TERMINAL
            if (pilha.startswith("E") and pilha[1] != "'"):
                isE(token)
            elif (pilha.startswith("E'")):
                isElinha(token)
            elif (pilha.startswith("T") and pilha[1] != "'"):
                isT(token)
            elif (pilha.startswith("T'")):
                isTlinha(token)
            elif (pilha.startswith("P") and pilha[1] != "'"):
                isP(token)
            elif(pilha.startswith("P'")):
                isPlinha(token)
            elif(pilha.startswith("F")):
                isF(token)

            # PILHA COM INICIAL TERMINAL

            elif(pilha.startswith("id")):
                pilha = pilha.replace("id","", 1)
                cadeia = cadeia + 'id'
                break
            elif(pilha.startswith("+")):
                pilha = pilha.replace("+","", 1)
                cadeia = cadeia + '+'
                break
            elif(pilha.startswith("-")):
                pilha = pilha.replace("-","", 1)
                cadeia = cadeia + '-'
                break
            elif(pilha.startswith("/")):
                pilha = pilha.replace("/","", 1)
                cadeia = cadeia + '/'
                break
            elif(pilha.startswith("*")):
                pilha = pilha.replace("*","", 1)
                cadeia = cadeia + '*'
                break
            elif(pilha.startswith("^")):
                pilha = pilha.replace("^","", 1)
                cadeia = cadeia + '^'
                break
            elif(pilha.startswith("exp")):
                pilha = pilha.replace("exp","", 1)
                cadeia = cadeia + 'exp'
                break
            elif(pilha.startswith("(")):
                pilha = pilha.replace("(","", 1)
                cadeia = cadeia + '('
                break
            elif(pilha.startswith(")")):
                pilha = pilha.replace(")","", 1)
                cadeia = cadeia + ')'
                break
            elif(pilha.startswith("[")):
                pilha = pilha.replace("[","", 1)
                cadeia = cadeia + '['
                break
            elif(pilha.startswith("]")):
                pilha = pilha.replace("]","", 1)
                cadeia = cadeia + ']'
                break
            elif(pilha.startswith("$")):
                pilha = pilha.replace("$","", 1)
                cadeia = cadeia + '$'
                break   


    
   
def main():

    tokenList = ['id','id','*','id', '^', 'id']
    Sintatico(tokenList)
    print("Cadeia aceita")
    
main()


