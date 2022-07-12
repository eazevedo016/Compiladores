# Autômato

![image](https://user-images.githubusercontent.com/75282286/178392128-9c08496b-a17a-4c48-b37e-f5645368e08c.png)

# Eliminando a Recursão à Esquerda

- E -> TE’
- E’ ->  +TE’ |  -TE’ | e
- T -> PT’
- T’ - > *PT’ | /PT’ | e
- P -> exp[F] P’ | FP’
- P’ -> ^FP’ | e
- F -> (E) | id

# First e Follow

## First

- First(E) = { } U First{T} = { exp, ( , id }
- First(E’) = { + , - }
- First(T) = { }  U First(P) = { exp, ( , id }
- First(T’) = { * , / }
- First(P) = { exp } U First(F) = { exp, ( , id }
- First(P’) = { ^ }
- First(F) = { ( , id }



## Follow

- Follow(E) = { $ , ) } 
- Follow(E’) = { } U Follow(E) = { $ , ) }
- Follow(T) = { } U First(E’) = 	 { + , - }			
- Follow(T’) = { } U Follow(T) = { + , - }
- Follow(P) = { } U First(T’) = { * , / }
- Follow(P’) = { } U Follow(P) = { * , / }
- Follow(F) = { } First(P’) = { ^ }





