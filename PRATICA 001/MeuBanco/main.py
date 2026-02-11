#Ponto de partida do software
import Banco_Dados.database as db

opcao = ""

while True:
    print('BANCO')
    print('================')
    print('1 - cadastro: ')
    print('2 - acessar conta: ')
    print('0 - sair sistema')
    print('================')
    opcao = input('opção: ')
    match opcao:

        case "1":
            print('Bem vindo!')
            nome_usuario = input('Informe seu nome: ')
            senha_usuario = input('Informe sua senha usando apenas 4 digitos')
            usuario = db.criar_conta(nome_usuario, senha_usuario)

            if usuario:
                print(f'Bem vindo {usuario}!')
            else:
                print('usuario não encontrado!')

        case "2":
            l = input("Usuario: ")
            s = input("Senha: ")
            usuario = db.acessar_conta(l, s)

        case "0":
            print('Até logo!')
            break
