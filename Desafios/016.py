class Funcionario:
    def __init__(self, nome, setor, cargo, empresa = "Curso em video"):
        
        #atributos:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa
        

    def apresentacao(self):
        return(f'Olá, sou a {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}')

c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())