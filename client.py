import requests
import os

def pesquisa_por_autor():
    autor = input("Digite o nome do autor que desejas. ")
    r_autor_prop = requests.get(f"http://127.0.0.1:8000/autor/{autor}")

    return r_autor_prop.json()

def pesquisa_por_tipo():
    tipo = input("Digite o nome do tipo de processo que desejas. ")
    r_tipo_prop = requests.get(f"http://127.0.0.1:8000/tipo/{tipo}")

    return r_tipo_prop.json()

def main():

    while(True):
        print("Qual o tipo de consulta desejas fazer?\n")
        print("<Digite 1 para listar todos as proposições>")
        print("<Digite 2 para listar proposições por autor>")
        print("<Digite 3 para listar proposições por tipo>")
        print("<Digite 4 para encerrar o programa>")
        print("")
        
        escolha = int(input("1, 2, 3 ou 4 ... "))

        if(escolha == 1):
            os.system("clear")
            r_todas_prop = requests.get(f"http://127.0.0.1:8000/proposicoes")
            print(r_todas_prop.json())
            print("")
            input("Press Enter to continue... ")
            os.system("clear")

        elif(escolha == 2):
            os.system("clear")
            print(pesquisa_por_autor())
            print("")
            input("Press Enter to continue... ")
            os.system("clear")
            
        elif(escolha == 3):
            os.system("clear")
            print(pesquisa_por_tipo())
            print("")
            input("Press Enter to continue... ")
            os.system("clear")

        elif(escolha == 4):
            print("Encerrando programa... ")
            break
        else:
            print("Entrada inválida! Tente uma válida da proxima vez... ")

        
if __name__ ==  '__main__':
    main()