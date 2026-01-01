"""Command-line interface for todo application."""

from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.theme import Theme

from services.task_service import TaskService

# Create a rich console with custom theme
console = Console(theme=Theme({"info": "cyan", "success": "green", "error": "red"}))


def display_menu() -> None:
    """Display main menu with rich formatting."""
    menu_content = r"""
[bold cyan]1.[/] [white]Add Task
[bold cyan]2.[/] [white]View Tasks
[bold cyan]3.[/] [white]Update Task
[bold cyan]4.[/] [white]Delete Task
[bold cyan]5.[/] [white]Mark Complete/Incomplete
[bold cyan]6.[/] [white]Exit
"""

    panel = Panel(
        menu_content,
        title="[bold green]TODO APPLICATION - MAIN MENU",
        border_style="green",
        padding=(1, 2)
    )
    console.print(panel)


def validate_non_empty(user_input: str, field_name: str) -> str:
    """Validate that user input is not empty.

    Args:
        user_input: The input string to validate
        field_name: Name of the field for error messages

    Returns:
        str: The stripped input string

    Raises:
        ValueError: If input is empty or only whitespace
    """
    if not user_input or not user_input.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return user_input.strip()


def validate_task_id(user_input: str) -> Optional[int]:
    """Validate and convert user input to a task ID.

    Args:
        user_input: The input string to validate and convert

    Returns:
        Optional[int]: The task ID if valid, None if invalid format
    """
    try:
        return int(user_input.strip())
    except ValueError:
        return None


def handle_add_task(task_service: TaskService) -> None:
    """Handle Add Task operation.

    Prompts user for title and description, validates inputs,
    and creates a new task with rich output.

    Args:
        task_service: The TaskService instance for task operations
    """
    console.print(Panel.fit(
        "[bold cyan]Add New Task",
        border_style="cyan"
    ))

    try:
        # Prompt for title
        title_input = input("Enter task title: ")
        title = validate_non_empty(title_input, "Title")

        # Prompt for description
        desc_input = input("Enter task description: ")
        description = validate_non_empty(desc_input, "Description")

        # Create task
        task = task_service.create_task(title, description)

        # Display success with rich
        success_panel = Panel(
            f"[bold green]✓[/bold green] Task [cyan]{task.id}[/cyan] created successfully",
            border_style="green",
            padding=(0, 1)
        )
        console.print(success_panel)

    except ValueError as e:
        error_panel = Panel(
            f"[bold red]✗ Error:[/bold red] {e}",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)
        console.print("[yellow]Please try again.[/yellow]")


def handle_view_tasks(task_service: TaskService) -> None:
    """Handle View Tasks operation with rich table formatting.

    Retrieves and displays all tasks with their status indicators
    in a beautifully formatted table.

    Args:
        task_service: The TaskService instance for task operations
    """
    console.print(Panel.fit(
        "[bold cyan]All Tasks",
        border_style="cyan"
    ))

    tasks = task_service.get_all_tasks()

    if not tasks:
        empty_panel = Panel(
            "[italic yellow]No tasks found[/italic yellow]",
            border_style="yellow",
            padding=(1, 2)
        )
        console.print(empty_panel)
        return

    # Create rich table
    table = Table(
        title="[bold]Task List[/bold]",
        show_header=True,
        header_style="bold magenta",
        border_style="cyan"
    )

    # Add columns
    table.add_column("Status", width=8)
    table.add_column("ID", width=5, justify="center")
    table.add_column("Title", width=30)
    table.add_column("Description", width=50)

    # Add rows
    for task in tasks:
        status_icon = "[green]✓[/green]" if task.completed else "[red]○[/red]"
        status_text = "[bold green]Complete[/bold green]" if task.completed else "[bold red]Incomplete[/bold red]"

        table.add_row(
            status_icon,
            f"[cyan]{task.id}[/cyan]",
            f"[white]{task.title}[/white]",
            f"[dim]{task.description}[/dim]"
        )

    console.print(table)


def handle_mark_complete(task_service: TaskService) -> None:
    """Handle Mark Complete/Incomplete operation.

    Prompts user for task ID and toggles its completion status
    with rich colored output.

    Args:
        task_service: The TaskService instance for task operations
    """
    console.print(Panel.fit(
        "[bold cyan]Mark Task Complete/Incomplete",
        border_style="cyan"
    ))

    task_id_input = input("Enter task ID: ")
    task_id = validate_task_id(task_id_input)

    if task_id is None:
        error_panel = Panel(
            "[bold red]✗ Error:[/bold red] Invalid ID format. Please enter a number.",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)
        return

    success = task_service.toggle_complete(task_id)

    if success:
        task = task_service.get_task_by_id(task_id)
        status = "complete" if task.completed else "incomplete"
        status_color = "green" if task.completed else "yellow"

        success_panel = Panel(
            f"[bold green]✓[/bold green] Task [cyan]{task_id}[/cyan] marked as [{status_color}]{status}[/{status_color}]",
            border_style="green",
            padding=(0, 1)
        )
        console.print(success_panel)
    else:
        error_panel = Panel(
            f"[bold red]✗ Error:[/bold red] Task with ID [cyan]{task_id}[/cyan] not found",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)


def handle_update_task(task_service: TaskService) -> None:
    """Handle Update Task operation.

    Prompts user for task ID, new title, and new description,
    then updates the task with rich colored output.

    Args:
        task_service: The TaskService instance for task operations
    """
    console.print(Panel.fit(
        "[bold cyan]Update Task",
        border_style="cyan"
    ))

    task_id_input = input("Enter task ID: ")
    task_id = validate_task_id(task_id_input)

    if task_id is None:
        error_panel = Panel(
            "[bold red]✗ Error:[/bold red] Invalid ID format. Please enter a number.",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)
        return

    # Verify task exists
    task = task_service.get_task_by_id(task_id)
    if task is None:
        error_panel = Panel(
            f"[bold red]✗ Error:[/bold red] Task with ID [cyan]{task_id}[/cyan] not found",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)
        return

    # Display current details in a panel
    current_info = f"""
[bold]Current Details:[/bold]
  [dim]ID:[/dim] [cyan]{task.id}[/cyan]
  [dim]Title:[/dim] [white]{task.title}[/white]
  [dim]Description:[/dim] [white]{task.description}[/white]
"""
    info_panel = Panel(
        current_info,
        title="[bold yellow]Current Task Information[/bold yellow]",
        border_style="yellow",
        padding=(0, 1)
    )
    console.print(info_panel)

    try:
        # Prompt for new details
        new_title_input = input("\nEnter new title: ")
        new_title = validate_non_empty(new_title_input, "Title")

        new_desc_input = input("Enter new description: ")
        new_description = validate_non_empty(new_desc_input, "Description")

        # Update task
        task_service.update_task(task_id, new_title, new_description)

        success_panel = Panel(
            f"[bold green]✓[/bold green] Task [cyan]{task_id}[/cyan] updated successfully",
            border_style="green",
            padding=(0, 1)
        )
        console.print(success_panel)

    except ValueError as e:
        error_panel = Panel(
            f"[bold red]✗ Error:[/bold red] {e}",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)
        console.print("[yellow]Please try again.[/yellow]")


def handle_delete_task(task_service: TaskService) -> None:
    """Handle Delete Task operation.

    Prompts user for task ID and deletes the task
    with rich colored output.

    Args:
        task_service: The TaskService instance for task operations
    """
    console.print(Panel.fit(
        "[bold cyan]Delete Task",
        border_style="cyan"
    ))

    task_id_input = input("Enter task ID: ")
    task_id = validate_task_id(task_id_input)

    if task_id is None:
        error_panel = Panel(
            "[bold red]✗ Error:[/bold red] Invalid ID format. Please enter a number.",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)
        return

    success = task_service.delete_task(task_id)

    if success:
        success_panel = Panel(
            f"[bold green]✓[/bold green] Task [cyan]{task_id}[/cyan] deleted successfully",
            border_style="green",
            padding=(0, 1)
        )
        console.print(success_panel)
    else:
        error_panel = Panel(
            f"[bold red]✗ Error:[/bold red] Task with ID [cyan]{task_id}[/cyan] not found",
            border_style="red",
            padding=(0, 1)
        )
        console.print(error_panel)


def run_cli(task_service: TaskService) -> None:
    """Run the main CLI loop with rich formatting.

    Displays a styled welcome message, shows the menu,
    captures user choice, and routes to appropriate handlers.
    Continues until the user selects the Exit option.

    Args:
        task_service: The TaskService instance for task operations
    """
    # Welcome panel
    welcome_panel = Panel(
        """[bold green]Welcome to the[/bold green] [bold cyan]Todo Application![/bold cyan]

[dim]A beautiful command-line task manager[/dim]
[dim]powered by Rich library for enhanced UI[/dim]""",
        border_style="green",
        padding=(1, 2)
    )
    console.print(welcome_panel)

    while True:
        display_menu()

        choice = input("\n[bold cyan]Enter your choice (1-6):[/bold cyan] ").strip()

        if choice == "1":
            handle_add_task(task_service)
        elif choice == "2":
            handle_view_tasks(task_service)
        elif choice == "3":
            handle_update_task(task_service)
        elif choice == "4":
            handle_delete_task(task_service)
        elif choice == "5":
            handle_mark_complete(task_service)
        elif choice == "6":
            # Goodbye panel
            goodbye_panel = Panel(
                """[bold green]Thank you for using the[/bold green] [bold cyan]Todo Application![/bold cyan]

[dim]All your in-memory tasks have been cleared.[/dim]
[dim]Have a productive day![/dim]""",
                border_style="green",
                padding=(1, 2)
            )
            console.print(goodbye_panel)
            break
        else:
            error_panel = Panel(
                "[bold red]✗ Error:[/bold red] Invalid option. Please select a valid menu item (1-6).",
                border_style="red",
                padding=(0, 1)
            )
            console.print(error_panel)
