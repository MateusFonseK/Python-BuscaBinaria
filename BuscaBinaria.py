import random

def menu():
    print("=====MENU=====")
    print("Selecione a opção desejada:")
    print("1-> Alterar o tamanho da lista")
    print("2-> Realizar Busca Binaria")
    print("0-> Sair")

def busca_binaria(lista):
    tamanho_lista = len(lista)
    inf = 0
    sup = tamanho_lista - 1
    tentativas = 0

    print("Lista gerada: \n", lista)
    lista.sort()
    print("\n")
    print("Lista gerada ordenada: \n", lista)

    chave_busca = int(input("\nQual chave você deseja buscar na lista: "))
    busca_binariarecursao(lista, inf, sup, chave_busca, tentativas)

def busca_binariarecursao(lista, inf, sup, chave_busca, tentativas):
    tentativas += 1
    if inf <= sup:
        meio = (inf + sup) // 2  

        if lista[meio] == chave_busca:
            print("\nChave encontrada no índice:", meio) 
            print("Após ", tentativas, ' tentativas.')
        elif chave_busca < lista[meio]:
            busca_binariarecursao(lista, inf, meio - 1, chave_busca, tentativas)  
        else:
            busca_binariarecursao(lista, meio + 1, sup, chave_busca, tentativas)  
    else:
        print("\nChave não encontrada na lista.")


lista = []
tamanho_lista = 20

while True:
    menu()
    opcao = int(input("Opção: "))
    if opcao == 0:
        print("\nSaindo...\n")
        break
    elif opcao == 1:
        print("\n-Tamanho da lista-\n")
        try:
            print("Tamanho atual da lista: ", tamanho_lista)
            tamanho_lista = int(input("Insira o novo tamanho da lista: "))
        except ValueError:
            print("\nPor favor, insira um valor inteiro válido.\n")
    elif opcao == 2:
        print("\n-Busca Binária-\n")
        lista.clear()
        for i in range(tamanho_lista):
            inserelista = random.randint(1,10000)
            lista.append(inserelista)
        busca_binaria(lista)
    else:
        print("\nOpção Inválida\n")
