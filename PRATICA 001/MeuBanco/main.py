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
            db.criar_conta(nome_usuario, senha_usuario)
        case "2":
            usuario = input('Usuario: ')
            senha = input('Senha: ')
            dados = db.acessar_conta(usuario, senha)
            

            if dados:
                print(f'Bem vindo {dados[1]}!')
                while True:
                    print('================')
                    print('1 - Extrato: ')
                    print('2 - Saldo: ')
                    print('3 - Saque ')
                    print('4 - Transferir: ')
                    print('0 - Sair: ')
                    print('================')
                    opcao_usuario = input('')

                    match opcao_usuario:
                         
                        case "1":
                            print('EXTRATO')
                        case "2":
                            print('SALDO')
                        case "3":
                            print('SAQUE')
                        case "4":
                            print('TRANSFERIR')
                        case "0":
                            break



        case "0":
            print('Até logo!')
            break
