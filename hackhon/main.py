from rich.theme import Theme
from rich.console import Console
from MODULOS.invest import investimento
from MODULOS.cambio import cambio_trade
from MODULOS.relatorio import registrar_despesas, gerar_relatorio
from MODULOS.transfe import transferencia
from MODULOS.linguas import textos
from MODULOS.emprestimo_mod import emprestimo
from rich.spinner import Spinner
import time
from rich.prompt import Prompt
from rich.prompt import Confirm


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

# valores de teste
cliente1 = {
    'nome': 'João Silva',
    'saldo': 1000.0,
    'moeda': 'BRL',
    'taxa_moeda': 1.0
}

cliente2 = {
    'nome': 'Maria Oliveira',
    'saldo': 500.0,
    'moeda': 'BRL',
    'taxa_moeda': 1.0
}

textos = {
    "pt": {
        "menu_opcoes": "\n=== Menu de Opções ===",
        "investir": "[1] Investir",
        "cambio": "[2] Câmbio",
        "conversao_moeda": "=== Conversão de Moeda ===",
        "registrar_despesas": "[3] Registrar Despesas",
        "relatorio":"[4] Relatório de gastos",
        "transferir": "[5] Transferir entre Usuários",
        "emprestimo": "[6] Empréstimos",
        "sair": "[7] Sair",
        "escolha": "\nEscolha uma opção: ",
        "saldo_insuficiente": "Saldo insuficiente! Tente novamente com um valor menor.",
        "valor_invalido": "Valor inválido!",
        "saindo": "\nSaindo do sistema. Até logo!",
        "opcao_invalida": "\nOpção inválida. Tente novamente."
    },
    "en": {
        "menu_opcoes": "\n=== Options Menu ===",
        "investir": "[1] Invest",
        "cambio": "[2] Currency Exchange",
        "conversao_moeda": "=== Currency Conversion ===",
        "registrar_despesas": "[3] Register Expenses",
        "relatorio": "[4] Report" ,
        "transferir": "[5] Transfer Between Users",
        "emprestimo": "[6] Loan",
        "sair": "[7] Exit",
        "escolha": "\nChoose an option: ",
        "saldo_insuficiente": "Insufficient balance! Please try again with a smaller amount.",
        "valor_invalido": "Invalid amount!",
        "saindo": "\nExiting the system. Goodbye!",
        "opcao_invalida": "\nInvalid option. Please try again."
    },
    "es": {
        "menu_opcoes": "\n=== Menú de Opciones ===",
        "investir": "[1] Invertir",
        "cambio": "[2] Cambio",
        "conversao_moeda": "=== Conversión de Moneda ===",
        "registrar_despesas": "[3] Registrar Gastos",
        "relatorio": "[4] Informe",
        "transferir": "[5] Transferir entre Usuarios",
        "emprestimo": "[6] Préstamo",
        "sair": "[7] Salir",
        "escolha": "\nElija una opción: ",
        "saldo_insuficiente": "¡Saldo insuficiente! Intente de nuevo con una cantidad menor.",
        "valor_invalido": "¡Valor inválido!",
        "saindo": "\nSaliendo del sistema. ¡Hasta luego!",
        "opcao_invalida": "\nOpción inválida. Intente de nuevo."
    },
    "fr": {
        "menu_opcoes": "\n=== Menu des Options ===",
        "investir": "[1] Investir",
        "cambio": "[2] Échange de Devises",
        "conversao_moeda": "=== Conversion de Monnaie ===",
        "registrar_despesas": "[3] Enregistrer des Dépenses",
        "relatorio": "[4] Informe",
        "transferir": "[5] Transférer entre Utilisateurs",
        "emprestimo": "[6] prêt",
        "sair": "[7] Quitter",
        "escolha": "\nChoisissez une option : ",
        "saldo_insuficiente": "Solde insuffisant ! Veuillez réessayer avec un montant plus petit.",
        "valor_invalido": "Montant invalide !",
        "saindo": "\nFermeture du système. À bientôt !",
        "opcao_invalida": "\nOption invalide. Veuillez réessayer."
    },
    "de": {
        "menu_opcoes": "\n=== Optionsmenü ===",
        "investir": "[1] Investieren",
        "cambio": "[2] Währungsumtausch",
        "conversao_moeda": "=== Währungsumrechnung ===",
        "registrar_despesas": "[3] Ausgaben erfassen",
        "relatorio": "[4] Bericht",
        "transferir": "[5] Zwischen Benutzern überweisen",
        "emprestimo": "[6] Darlehen",
        "sair": "[7] Beenden",
        "escolha": "\nWählen Sie eine Option: ",
        "saldo_insuficiente": "Unzureichendes Guthaben! Bitte versuchen Sie es mit einem kleineren Betrag.",
        "valor_invalido": "Ungültiger Betrag!",
        "saindo": "\nSystem wird beendet. Auf Wiedersehen!",
        "opcao_invalida": "\nUngültige Option. Bitte versuchen Sie es erneut."
    },
    "ru": {
        "menu_opcoes": "\n=== Меню опций ===",
        "investir": "[1] Инвестировать",
        "cambio": "[2] Обмен валюты",
        "conversao_moeda": "=== Конвертация валюты ===",
        "registrar_despesas": "[3] Зарегистрировать расходы",
        "relatorio": "[4] Отчет",
        "transferir":"[5] Перевод между пользователями",
        "emprestimo":"[6] кредит",
        "sair": "[7] Выйти",
        "escolha": "\nВыберите опцию: ",
        "saldo_insuficiente": "Недостаточно средств! Попробуйте еще раз с меньшей суммой.",
        "valor_invalido": "Неверное значение!",
        "saindo": "\nВыход из системы. До свидания!",
        "opcao_invalida": "\nНеверная опция. Попробуйте еще раз."
    },
    "jp": {
        "menu_opcoes": "\n=== オプションメニュー ===",
        "investir": "[1] 投資",
        "cambio": "[2] 両替",
        "conversao_moeda": "=== 通貨の変換 ===",
        "registrar_despesas": "[3] 支出を記録する",
        "relatorio": "[4] レポート" ,
        "transferir": "[5] ユーザー間で送金する",
        "emprestimo": "[6]  ローン",
        "sair": "[7] 終了する",
        "escolha": "\nオプションを選択してください: ",
        "saldo_insuficiente": "残高不足です！少ない金額で再試行してください。",
        "valor_invalido": "無効な金額です！",
        "saindo": "\nシステムを終了します。さようなら！",
        "opcao_invalida": "\n無効なオプションです。再試行してください。"
    },
    "ko": {
        "menu_opcoes": "\n=== 옵션 메뉴 ===",
        "investir": "[1] 투자",
        "cambio": "[2] 환전",
        "conversao_moeda": "=== 통화 변환 ===",
        "registrar_despesas": "[3] 지출 등록",
        "relatorio": "[4] 보고서",
        "transferir": "[5] 사용자 간 이체",
        "emprestimo": "[6] 대출",
        "sair": "[7] 종료",
        "escolha": "\n옵션을 선택하세요: ",
        "saldo_insuficiente": "잔액이 부족합니다! 더 적은 금액으로 다시 시도하세요.",
        "valor_invalido": "잘못된 금액입니다!",
        "saindo": "\n시스템을 종료합니다. 안녕히 가세요!",
        "opcao_invalida": "\n잘못된 옵션입니다. 다시 시도하세요."
    }
}

def selecionar_idioma():
    console.print("\nSelecione o idioma / Choose the language:", style='titulo')
    console.print("[1] Português (pt)", style='entrada')
    console.print("[2] English (en)", style='entrada')
    console.print("[3] Español (es)", style='entrada')
    console.print("[4] Français (fr)", style='entrada')
    console.print("[5] Deutsch (de)", style='entrada')
    console.print("[6] Русский (ru)", style='entrada')
    console.print("[7] 日本語 (jp)", style='entrada')
    console.print("[8] 한국어 (ko)", style='entrada')
    
    while True:
        opcao = console.input("\n[bold yellow]Digite o número da opção / Enter the option number: ")
        linguas = {'1': 'pt', '2': 'en', '3': 'es', '4': 'fr', '5': 'de', '6': 'ru', '7': 'jp', '8': 'ko'}
        
        if opcao in linguas:
            with console.status("[bold green] Traduzindo..[/bold green]", spinner="dots"):
                time.sleep(4)
            return linguas[opcao]
        
        
        else:
            console.print("\n:x: opção inválida / invalid option!", style='error')

def menu(idioma):
    t = textos[idioma]
    
    while True:
    # console.print("\n=== Menu de Opções ===",style='titulo')
        
        while True:
            console.print(t["menu_opcoes"], style='titulo')
            
            console.print(t["investir"], style='entrada')
            console.print(t["cambio"], style='entrada')
            console.print(t["registrar_despesas"], style='entrada')
            console.print(t["relatorio"], style='entrada')
            console.print(t["transferir"], style='entrada')
            console.print(t["emprestimo"], style='entrada')
            console.print(t["sair"], style='entrada')
            console.print("[0] Voltar para escolher idioma", style='entrada')

            opcao = input(t["escolha"])

            
        #   opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                investimento(cliente1) 
            elif opcao == '2':
                cambio_trade(cliente1)
            elif opcao == '3':
                despesas = registrar_despesas()
                
            elif opcao == '4':
                gerar_relatorio(despesas)

            elif opcao == '5':
                console.print("\n=== Transferência entre Usuários ===", style='titulo')
                try:
                    while True:
                        valor = float(console.input(f"\n[bold yellow]Digite o valor para transferir de {cliente1['nome']} para {cliente2['nome']}:  "))
                        if valor > cliente1['saldo']:
                            console.print(":warning: Saldo insuficiente.", style='error')
                            
                        else:
                            transferencia(cliente1, cliente2, valor)
                            break
                except ValueError:
                    console.print("\n:x: opção inválida / invalid option!", style='error')
            
            elif opcao == '6':
                emprestimo(cliente1)
                
            
            elif opcao == '7':
                confirmar = Confirm.ask("[bold yellow]Deseja realmente sair?[/bold yellow]")
                if confirmar:
                    console.print("[red]Saindo...[/red]")
                    console.print("Retornando ao menu inicial...", style='certo')
                break

            elif opcao == '0':  # Se o usuário escolher "Voltar", será solicitado que ele escolha o idioma novamente
                return True 
            
            else:
                console.print("\n:x: Erro ao processar a operação.", style='error')

if __name__ == "__main__":
    while True:
        idioma_selecionado = selecionar_idioma()
        voltar = menu(idioma_selecionado)
        if not voltar:
            break  