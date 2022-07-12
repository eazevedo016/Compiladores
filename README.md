# Autômato

![image](https://user-images.githubusercontent.com/75282286/178392128-9c08496b-a17a-4c48-b37e-f5645368e08c.png)

# Eliminando a Recursão à Esquerda

- E -> TE’
- E’ ->  +TE’ |  -TE’
- T -> PT’
- T’ - > *PT’ | /PT’
- P -> exp[F] P’ | FP’
- P’ -> ^FP’
- F -> (E) | id

# First e Follow



