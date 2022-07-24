class posFixa():
  pilha = []
  pilhaPosFixa = []

  def resetarPilhas(self):
    self.pilha = []
    self.pilhaPosFixa = []

  def inserirPosfixa(self,token):
    self.pilhaPosFixa.append(token)

  def inserirPilha(self,token):
    self.pilha.append(token)

  def ajustarPilhas(self,token):
    achou = False
    for elemento in self.pilha[::-1]:
      if self.validarPrecedencia(token,elemento):
        achou=True
        self.pilhaPosFixa.append(self.pilha.pop())
      else:
        break
    self.pilha.append(token)
    #if achou:
    #  self.pilhaPosFixa.append(token)
    #else:
    #  self.pilha.append(token)

  def desempilharParenteses(self):
    removido = ""
    while removido != "(":
      removido = self.pilha.pop()
      if removido != "(":
        self.pilhaPosFixa.append(removido)
  
  def desempilharTudo(self):
    for i in self.pilha[::-1]:
      self.pilhaPosFixa.append(self.pilha.pop())

  def validarPrecedencia(self, elemento1, elemento2):
    precedencia={"(":0,"+":1,"-":1,"*":2,"/":2,"^":3,"exp":4}
    return precedencia.get(elemento1) <= precedencia.get(elemento2)


  def gerarPosFixa(self,palavra):
    self.desempilharTudopilha = []
    self.pilhaPosFixa = []
    self.palavra = palavra
    for token in self.palavra:
      if token.isnumeric():
        self.pilhaPosFixa.append(token)
      if token == "(":
        self.pilha.append(token)
      if token in ["+","-","*","/","^","EXP"] :
        self.ajustarPilhas(token)
      if token == ")":
        self.desempilharParenteses()
    self.desempilharTudo()

      