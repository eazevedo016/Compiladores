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


# Tabela M

![image](https://user-images.githubusercontent.com/75282286/179992492-3d92d4b1-8154-4f39-9995-44db848666e2.png)








