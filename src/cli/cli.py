"""Command-line interface for the todo application."""

from typing import Optional

from services.task_service import TaskService


def display_menu() -> None:
    """Display the main menu with numbered options."""
    print("\n=== Todo Application Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print("=============================")


def validate_non_empty(user_input: str, field_name: str) -> str:
    """Validate that user input is not empty.

    Args:
        user_input: The input string to validate.
        field_name: Name of the field (for error message).

    Returns:
        The trimmed input string if valid.

    Raises:
        ValueError: If input is empty or contains only whitespace.
    """
    if not user_input or not user_input.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return user_input.strip()


def validate_task_id(user_input: str) -> Optional[int]:
    """Validate and convert task ID input to integer.

    Args:
        user_input: The input string to convert.

    Returns:
        The integer task ID if valid, None if conversion fails.
    """
    try:
        return int(user_input.strip())
    except ValueError:
        return None


def handle_add_task(task_service: TaskService) -> None:
    """Handle adding a new task.

    Args:
        task_service: The task service instance for creating tasks.

    Raises:
        ValueError: If title or description is empty.
    """
    print("\n--- Add New Task ---")
    while True:
        title = input("Enter task title: ")
        try:
            title = validate_non_empty(title, "Title")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        description = input("Enter task description: ")
        try:
            description = validate_non_empty(description, "Description")
            break
        except ValueError as e:
            print(f"Error: {e}")

    task = task_service.create_task(title, description)
    print(f"Task {task.id} created successfully!")


def handle_view_tasks(task_service: TaskService) -> None:
    """Handle viewing all tasks.

    Args:
        task_service: The task service instance for retrieving tasks.
    """
    print("\n--- Task List ---")
    tasks = task_service.get_all_tasks()

    if not tasks:
        print("No tasks found")
    else:
        for task in tasks:
            print(f"\n{task}")


def handle_mark_complete(task_service: TaskService) -> None:
    """Handle marking a task as complete or incomplete.

    Args:
        task_service: The task service instance for toggling task completion.
    """
    print("\n--- Mark Task Complete/Incomplete ---")
    while True:
        task_id_input = input("Enter task ID: ")
        task_id = validate_task_id(task_id_input)
        if task_id is not None:
            break
        print("Invalid ID format. Please enter a number.")

    if task_service.toggle_complete(task_id):
        task = task_service.get_task_by_id(task_id)
        status = "complete" if task.completed else "incomplete"
        print(f"Task {task_id} marked as {status}")
    else:
        print(f"Task with ID {task_id} not found")


def handle_update_task(task_service: TaskService) -> None:
    """Handle updating an existing task.

    Args:
        task_service: The task service instance for updating tasks.
    """
    print("\n--- Update Task ---")
    while True:
        task_id_input = input("Enter task ID: ")
        task_id = validate_task_id(task_id_input)
        if task_id is not None:
            break
        print("Invalid ID format. Please enter a number.")

    task = task_service.get_task_by_id(task_id)
    if task is None:
        print(f"Task with ID {task_id} not found")
        return

    print(f"\nCurrent Title: {task.title}")
    while True:
        new_title = input("Enter new title: ")
        try:
            new_title = validate_non_empty(new_title, "Title")
            break
        except ValueError as e:
            print(f"Error: {e}")

    print(f"\nCurrent Description: {task.description}")
    while True:
        new_desc = input("Enter new description: ")
        try:
            new_desc = validate_non_empty(new_desc, "Description")
            break
        except ValueError as e:
            print(f"Error: {e}")

    task_service.update_task(task_id, new_title, new_desc)
    print(f"Task {task_id} updated successfully!")


def handle_delete_task(task_service: TaskService) -> None:
    """Handle deleting a task.

    Args:
        task_service: The task service instance for deleting tasks.
    """
    print("\n--- Delete Task ---")
    while True:
        task_id_input = input("Enter task ID: ")
        task_id = validate_task_id(task_id_input)
        if task_id is not None:
            break
        print("Invalid ID format. Please enter a number.")

    if task_service.delete_task(task_id):
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Task with ID {task_id} not found")


def run_cli(task_service: TaskService) -> None:
    """Run the main CLI loop.

    Args:
        task_service: The task service instance for all operations.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

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
            print("\nExiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid menu item.")
