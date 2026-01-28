from rich import print
from rich.table import Table

tabela = Table(title = "Tabela preços")

tabela.add_column("Nome", justify="rigth", style="red")
tabela.add_column("Preço",justify="rigth", style="blue")

tabela.add_row("Lapis", "R$1,50")
tabela.add_row("Borracha", "[green]R$2,50[/]")

print(tabela)