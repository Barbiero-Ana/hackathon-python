from rich.console import Console
from rich.prompt import Prompt

from rich.prompt import Confirm

console = Console()


confirmar = Confirm.ask("[bold yellow]Deseja realmente sair?[/bold yellow]")
if confirmar:
    console.print("[red]Saindo...[/red]")
