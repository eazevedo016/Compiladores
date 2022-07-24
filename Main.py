from os.path import exists
from Sintatico import Sintatico
print("\n***************************************************************************************")
print('Será lido o arquivo "entrada.txt" e em seguida gerado um arquivo de saída "saida.txt".')

if exists("entrada.txt"):
    sintatico = Sintatico()
    arquivoSaida = open("saida.txt","w")
    try:
        sintatico.AvaliarSintaxe("entrada.txt")
        print("\nCódigo compilado com sucesso!")
        for i in range(len(sintatico.listaCadeias)):
            arquivoSaida.write(f'{sintatico.listaCadeias[i]} \t\t\t\t \\\\{sintatico.listaDeResultados[i]}\n' )
            print(f'\n{sintatico.listaCadeias[i]} \t\t\t\t \\\\{sintatico.listaDeResultados[i]}')
        arquivoSaida.close()
    except Exception as e:
        print(f'\nErro no Arquivo "entrada.txt"\n\nErro: {e}')
else:
    print('\nArquivo "entrada.txt" não foi encontrado na pasta.')
print("\n***************************************************************************************")

    