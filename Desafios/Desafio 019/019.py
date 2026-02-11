from rich import print
import time


class Livro():

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f'[blue]Você acabou de abarir o livro [red]{self.titulo}[/] que tem [green]{self.paginas}[/] páginas no total.\nVocê está na [yellow]pagina {self.pagina_atual}[/][/]')

    

    def avancar_paginas(self, quant):
        time.sleep(1)
        cont = 0
        destino = self.pagina_atual + quant

        if self.pagina_atual > self.paginas:
            print(f'[red]Você já termiou o livro {self.titulo}[/]')
            return

        for i in range(self.pagina_atual, destino):
            if i <= self.paginas:
                print(f'Pag{i} > ', end="")
                time.sleep(0.3)
                cont += 1

            if i == self.paginas:
                print(f'[red]Você chegou ao final do livro')
                break

        self.pagina_atual = min(self.pagina_atual + cont, self.paginas)

        print(f'[blue]Você avanço {cont} páginas e agora está na [yellow]pagina {self.pagina_atual}[/][/]')

        


    
l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(10)