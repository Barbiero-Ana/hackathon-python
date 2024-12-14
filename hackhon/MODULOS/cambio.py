
from rich.theme import Theme
from rich.console import Console
from rich.progress import track
import time
from rich.spinner import Spinner

# Tema para estilização
estilo = Theme({
    'certo': 'bold green',
    'error': 'bold red',
    'titulo': 'bold underline magenta',
    'entrada': 'bold yellow',
    'saida': 'bold cyan'
})

console = Console(theme=estilo)

cambio = {
    1: ('USD', 6.0),
    2: ('EUR', 6.33),
    3: ('PESO ARGENTINO', 166.46),
    4: ('USD CANADENSE', 4.26),
    5: ('LIBRA ESTERLINA', 7.70)
}

def mostrar_opcoes_cambio():
    console.print('\nOpções de câmbio disponíveis:\n', style='titulo')
    for chave, (nome, taxa) in cambio.items():
        console.print(f'{chave}. {nome} - Taxa: {taxa}', style='entrada')

def cambio_trade(cliente):
    console.print("\n=== Conversão de Moeda ===", style='titulo')
    mostrar_opcoes_cambio()
    try:
        opcao = int(input('\nEscolha a moeda: '))
        if opcao not in cambio:
            console.print("\n:x: Moeda inválida!", style='error')
            return

        nova_moeda, taxa = cambio[opcao]
        saldo_em_brl = cliente['saldo']
        cliente['saldo'] = saldo_em_brl / taxa
        cliente['moeda'] = nova_moeda
        with console.status("[bold green]Consultando saldo...[/bold green]", spinner="dots"):
            time.sleep(4)
        for step in track(range(10), description="Processando..."):
            time.sleep(0.5)

        console.print(f'\nMoeda convertida! Novo saldo: {cliente["saldo"]:.2f} {nova_moeda}', style='certo')
    except ValueError:
        console.print("\n:x: Entrada inválida!", style='error')