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

# Dicionário de opções de investimento
menu_invest = {
    1: ('Poupança', 0.5),
    2: ('CDB', 0.8),
    3: ('Fundos Imobiliários', 1.2),
    4: ('Tesouro Selic', 0.7),
    5: ('Peer-to-Peer Lending', 1.4),
    6: ('Debêntures', 1.0),
    7: ('Fundo Multimercado', 1.1)
}

def rendimento(valor, taxa, meses):
    return valor * (1 + (taxa / 100)) ** meses

def opcoes_investimento():
    console.print('\nOpções de investimento disponíveis:\n', style='titulo')
    for chave, (nome, taxa) in menu_invest.items():  # Corrigido para 'menu_invest'
        console.print(f'{chave}. {nome} - Rendimento de {taxa}% ao mês', style='entrada')

def investimento(cliente):
    console.print("\n=== Central de investimentos do Noob Bank ===", style='titulo')
    opcoes_investimento()

    try:
        opcao = int(console.input('\n[bold yellow]Escolha onde deseja investir seus fundos (digite o número correspondente): '))
        if opcao not in menu_invest:  
            console.print("\n:x: Opção inválida.", style='error')
            return

        valor = float(input('\nDigite o valor que deseja investir: '))
        with console.status("[bold green]Consultando saldo...[/bold green]", spinner="dots"):
            time.sleep(4)
        if valor <= 0 or valor > cliente['saldo']:
            console.print("\n:x: Valor inválido ou saldo insuficiente.", style='error')
            return

        meses = int(console.input('\n[bold yellow]Digite por quantos meses deseja investir: '))
        if meses <= 0:
            console.print('O tempo deve ser maior que zero...', style='error')
            return

        nome_invest, taxa = menu_invest[opcao]  
        valor_final = rendimento(valor, taxa, meses)
        cliente['saldo'] -= valor
        for step in track(range(10), description="Processando..."):
            time.sleep(0.5)

        console.print(f'\nInvestido em {nome_invest}. R${valor:.2f} renderá R${valor_final:.2f} em {meses} meses.', style='certo')
        console.print(f'Saldo atual: R${cliente["saldo"]:.2f}', style='saida')
    except ValueError:
        console.print("\n:x: Entrada inválida!", style='error')