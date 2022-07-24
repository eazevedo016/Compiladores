# Como executar?

- Faça um clone do repositório;
- Altere o arquivo "entrada.txt" de acordo com as entradas que deseja testar;
- Abra o arquivo "Main.py" e execute o arquivo na IDE de sua preferência.
- Caso queira testar unicamente o Analisador Léxico e/ou Sintático:
- Abra o arquivo "LexScanner.py" (analisador léxico) e/ou "Sintatico.py" (analisador sintático), descomente a chamada da função "main()" na última linha do arquivo e execute.


# Autômato

![image](https://user-images.githubusercontent.com/75282286/178392128-9c08496b-a17a-4c48-b37e-f5645368e08c.png)

# Eliminando Recursão à Esquerda

- E -> TE’
- E’ ->  +TE’ |  -TE’ | e
- T -> PT’
- T’ - > *PT’ | /PT’ | e
- P -> exp[F] | FP’
- P’ -> ^FP’ | e
- F -> (E) | id

# Alfabeto

- Terminais: + - * / exp ( ) [ ]
- Não terminais: E E' T T' P P' F

# First e Follow

## First

- First(E) = { } U First{T} = { exp, ( , id }
- First(E’) = { + , -, e }
- First(T) = { }  U First(P) = { exp, ( , id }
- First(T’) = { * , /  , e}
- First(P) = { exp } U First(F) = { exp, ( , id }
- First(P’) = { ^, e }
- First(F) = { ( , id }


-sintetizando:
- First(E)  = { exp, ( , id }          
- First(E’) = { + , - , e }                            
- First(T)  = { exp, ( , id }     
- First(T’) = { * , / , e }                           
- First(P)  = { exp, ( , id } 
- First(P’) = { ^ , e }                               
- First(F)  = { ( , id }


## Follow

- Follow(E) = { $, ) }
- Follow(E’) =  { } U Follow(E) = { $, ) }
- Follow(T) = 	{ } U First(E’)	= { + , - } U Follow(E) = {  + , - , $ , ) }
- Follow(T’) = { } U Follow(T) =  {  + , - , $ , ) }
- Follow(P) = { } U First(T’) =  { * , /  } U Follow(T) = {  * , / , + , - , $ , ) }
- Follow(P’) = { } Follow(P) = {  * , / , + , - , $ , ) }
- Follow(F) = { } U First(P’) = { ^} U Follow(P) =  {  ^, * , / , + , - , $ , ) }

-sintetizando:
- Follow(E)  = { ) , $ }
- Follow(E’) = { ) , $ }
- Follow(T)  = {  + , - , ) , $ }
- Follow(T’) = {  + , - , ) , $ }
- Follow(P)  = {  * , / , + , - , ) , $ }
- Follow(P’) = {  * , / , + , - , ) , $ }
- Follow(F)  = {  ^, * , / , + , - , ) , $ }


# Tabela M para análise sintática

![image](https://user-images.githubusercontent.com/75282286/179992492-3d92d4b1-8154-4f39-9995-44db848666e2.png)

# Semântico

Foi usado o conceito de "pilha posfixa" para o cálculo das expressões de entrada. Trata-se da realocação dos elementos da pilha original, empilhando o operador após os seus operandos. Dessa forma o cálculo é feito seguindo a ordem de precedência corretamente.
Portanto, implica-se que a regra semântica aplicada sobre o compilador é a execução correta da operação seguindo sua ordem de precedência de operadores.

![image](https://user-images.githubusercontent.com/75282286/180669599-2a85e15b-abc7-4d4b-bbb8-44b1d3a4915f.png)









