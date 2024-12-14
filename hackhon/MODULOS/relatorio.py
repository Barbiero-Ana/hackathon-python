from rich.theme import Theme
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time
from rich.spinner import Spinner


# Tema para estilização
# Entradas - [bold yellow]
estilo = Theme({
    'titulo': 'bold underline magenta',
    'error': 'bold red'
})

console = Console(theme=estilo)

def registrar_despesas():
    despesas = []
    while True:
        console.print("\n==== Bem vindo(a) ao sistema de gestão do Noob Bank ====", style= 'titulo')
        descricao = console.input('\n[bold yellow]Digite a descrição da despesa (ou "sair" para encerrar): ')
        if descricao.lower() == 'sair':
            break
        try:
            valor = float(console.input('[bold yellow]Digite o valor da despesa: '))
            despesas.append({'descricao': descricao, 'valor': valor})
            with console.status("[bold green]Consultando saldo...[/bold green]", spinner="dots"):
                time.sleep(4)
        except ValueError:
            console.print("\n:x: valor inválido!", style='error')
    return despesas


def gerar_relatorio(despesas):
    for step in track(range(10), description="Processando..."):
            time.sleep(0.10)
    console.print("\n=== Relatório de Despesas ===", style='titulo')
    tabela = Table(show_header=True, header_style="bold magenta")
    tabela.add_column("Descrição")
    tabela.add_column("Valor", justify="right", style="bold red")

    for despesa in despesas:
        tabela.add_row(despesa['descricao'], f"R${despesa['valor']:.2f}")

    console.print(tabela)