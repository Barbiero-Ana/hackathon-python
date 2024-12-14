from rich.theme import Theme
from rich.console import Console
import math
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

# Opções de empréstimos disponíveis
emprestimos = {
    1: (500.00, 0.03),  # R$500,00, 3% de juros
    2: (1000.00, 0.07),  # R$1.000,00, 7% de juros
    3: (1500.00, 0.10),  # R$1.500,00, 10% de juros
    4: (2000.00, 0.05),  # R$2.000,00, 5% de juros
    5: (3000.00, 0.12),  # R$3.000,00, 12% de juros
    6: (4000.00, 0.08),  # R$4.000,00, 8% de juros
    7: (5000.00, 0.15),  # R$5.000,00, 15% de juros
    8: (10000.00, 0.20), # R$10.000,00, 20% de juros
    9: (1200.00, 0.04),  # R$1.200,00, 4% de juros
    10: (2500.00, 0.09)  # R$2.500,00, 9% de juros
}


def opcoes_emprestimo():
    console.print('\nOpções de empréstimos disponíveis:\n', style='titulo')
    for chave, (valor, taxa) in emprestimos.items():
        console.print(f'{chave}. Empréstimo de R${valor:.2f} - Taxa: {taxa * 100:.2f}%', style='entrada')

def taxas_emprestimo(valor, meses, taxa_juros):
    # Total do empréstimo com juros compostos
    return valor * (1 + taxa_juros) ** meses

def parcelamento(valor, meses, taxa_juros):
    # Valor da parcela mensal
    valor_final = taxas_emprestimo(valor, meses, taxa_juros)
    return valor_final / meses

def emprestimo(cliente):
    console.print("\n=== Central de Empréstimos do Banco Noob Bank ===", style='titulo')
    opcoes_emprestimo()

    try:
        opcao = int(console.input('\n[bold yellow]Escolha o tipo de empréstimo (digite o número correspondente): '))
        if opcao not in emprestimos:
            console.print("\n:x: Opção inválida... Tente novamente.", style='error')
            return

        meses = int(console.input('\n[bold yellow]Digite o número de parcelas (máximo 36 meses): '))
        if meses <= 0 or meses > 36:
            console.print('O número de parcelas deve ser entre 1 e 36.', style='error')
            return

        valor, taxa_juros = emprestimos[opcao]
        valor_final = taxas_emprestimo(valor, meses, taxa_juros)
        valor_parcela = parcelamento(valor, meses, taxa_juros)

        confirmacao = console.input('\n[bold yellow]Deseja confirmar o empréstimo? (s/n): ')
        if confirmacao.lower() != 's':
            console.print("\n:x: Empréstimo cancelado...", style='error')
            return

        cliente['saldo'] += valor
        
        for step in track(range(10), description="Processando..."):
            time.sleep(0.5)
        with console.status("[bold green]Consultando saldo...[/bold green]", spinner="dots"):
            time.sleep(4)


        console.print(f'\nEmpréstimo de R${valor:.2f} concedido com sucesso!', style='certo')
        console.print(f'O valor total com juros será de R${valor_final:.2f}.', style='saida')
        console.print(f'Parcelamento em {meses} meses: R${valor_parcela:.2f} por mês.', style='saida')
        console.print(f'Saldo atual: R${cliente["saldo"]:.2f}.', style='saida')

    except ValueError:
        console.print("\n:x: Entrada inválida! Digite apenas números por favor.", style='error')
