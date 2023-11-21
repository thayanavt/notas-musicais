from rich import print
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.escalas import escala

app = Typer()


@app.command()
def escalas(tonica=Argument('c'), tonalidade=Argument('maior')):
    notas, graus = escala(tonica, tonalidade).values()
    table = Table()

    for grau in graus:
        table.add_column(grau)

    table.add_row(*notas)
    print(table)
