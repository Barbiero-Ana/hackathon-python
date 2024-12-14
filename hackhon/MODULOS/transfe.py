from rich.theme import Theme
from rich.console import Console
from rich.progress import track
import time
from rich.spinner import Spinner


# Tema para estilização
# Entradas - [bold yellow]
estilo = Theme({
    'certo': 'bold green',
    'error': 'bold red',
    'titulo': 'bold underline magenta',
    'entrada': 'bold yellow',
    'saida': 'bold cyan'
})

console = Console(theme=estilo)

def transferencia(origem, destino, valor):
    try:
        if valor <= 0:
            console.print('O valor deve ser maior que zero!', style='error')
            return

        if valor > origem['saldo']:
            console.print('Saldo insuficiente para realizar a transferência!', style='error')
            return

        origem['saldo'] -= valor
        destino['saldo'] += valor
        
        for step in track(range(10), description="Processando..."):
            time.sleep(0.6)
            
        console.print(f'\n:white_check_mark: Transação realizada com sucesso no valor de R${valor:.2f}.',style='certo')
        with console.status("[bold green]Consultando saldo...[/bold green]", spinner="dots"):
            time.sleep(4)
            
        console.print(f"\nSaldo atual de {origem['nome']}: R${origem['saldo']:.2f}", style='saida')
        console.print(f"Saldo atual de {destino['nome']}: R${destino['saldo']:.2f}", style='saida')
    except ValueError:
        console.print("\n:x: Entrada inválida!", style='error')