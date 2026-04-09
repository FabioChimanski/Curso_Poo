from rich import print
from rich.panel import Panel
from rich.console import Console

class ControleRemoto:
            canal_min = 1
            canal_max = 7
            volume_min = 1
            volume_max = 5

            def __init__(self, canal = 1, volume = 5):
                 self.canal_atual:int = canal
                 self.volume_atual:int = volume
                 self.ligado:bool = False

            def liga_desliga(self):
                  self.ligado = not self.ligado

            def mostrar_tv(self):
                conteudo = ""
                if not self.ligado:
                    conteudo = ('[red]A tv está desligada')
                else:
                    conteudo = "CANAL = "
                    for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max +1):
                        if canal == self.canal_atual:
                            conteudo += f'[yellow on yellow] {canal} [/]'
                        else:
                            conteudo += f'  {canal}'
                    
                    conteudo += "\nVOLUME = "
                    for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max+1):
                        if volume <= self.volume_atual:
                            conteudo += "[black on cyan]    [/]"
                        else:
                            conteudo += "[white on white]    [/]"
                conteudo += "\nCANAL < >  VOL + - "
                

                
                tv = Panel(conteudo, title="[ TV ]", width=40)
                print(tv)


'''            match comando:
                case "@":
                    self.ligar()
                case "0":
                    break
                case ">":
                    print(">")
                case "<":
                    print("<")
                case "+":
                    print("+")
                case "-":
                    print("-")

    def canal(self):
        pass
'''

c = ControleRemoto(7,1)
c.liga_desliga()
c.mostrar_tv()