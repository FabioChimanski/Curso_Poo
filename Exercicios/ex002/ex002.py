#Declaração de Classes
class Gafanhoto:
    def __init__(self, nome = "", idade = 0):#metodo construtor

        #Atributos de instancia
        self.nome = nome
        self.idade = idade


        #Metedos de instancia
    def aniversario(self):
        self.idade += 1

    
    def __str__(self): #Dunder Method
        return f"{self.nome} e um Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"

#Declaração de Objetos

g1 = Gafanhoto("Maria", 17)
g1.aniversario()
#print(g1)
print(g1.__dict__)# exibindo como dicionario usando attribute
print(g1.__getstate__()) #exibindo como dicionario usando methodo


g2 = Gafanhoto("Mauro", 54)
print(g2)
print(g2.__getstate__())