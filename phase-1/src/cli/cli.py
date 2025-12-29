"""Command-line interface for the todo application."""

from typing import Optional
from services.task_service import TaskService


def display_menu() -> None:
    """Display the main menu with available options."""
    print("\n" + "=" * 50)
    print("TODO APPLICATION - MAIN MENU")
    print("=" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print("=" * 50)


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
    """Handle the Add Task operation.

    Prompts user for title and description, validates inputs,
    and creates a new task.

    Args:
        task_service: The TaskService instance for task operations
    """
    print("\n--- Add New Task ---")

    try:
        # Prompt for title
        title_input = input("Enter task title: ")
        title = validate_non_empty(title_input, "Title")

        # Prompt for description
        desc_input = input("Enter task description: ")
        description = validate_non_empty(desc_input, "Description")

        # Create task
        task = task_service.create_task(title, description)
        print(f"\n✓ Task {task.id} created successfully")

    except ValueError as e:
        print(f"\n✗ Error: {e}")
        print("Please try again.")


def handle_view_tasks(task_service: TaskService) -> None:
    """Handle the View Tasks operation.

    Retrieves and displays all tasks with their status indicators.

    Args:
        task_service: The TaskService instance for task operations
    """
    print("\n--- All Tasks ---")

    tasks = task_service.get_all_tasks()

    if not tasks:
        print("No tasks found")
        return

    print()
    for task in tasks:
        print(task)
        print()


def handle_mark_complete(task_service: TaskService) -> None:
    """Handle the Mark Complete/Incomplete operation.

    Prompts user for task ID and toggles its completion status.

    Args:
        task_service: The TaskService instance for task operations
    """
    print("\n--- Mark Task Complete/Incomplete ---")

    task_id_input = input("Enter task ID: ")
    task_id = validate_task_id(task_id_input)

    if task_id is None:
        print("\n✗ Error: Invalid ID format. Please enter a number.")
        return

    success = task_service.toggle_complete(task_id)

    if success:
        task = task_service.get_task_by_id(task_id)
        status = "complete" if task.completed else "incomplete"
        print(f"\n✓ Task {task_id} marked as {status}")
    else:
        print(f"\n✗ Error: Task with ID {task_id} not found")


def handle_update_task(task_service: TaskService) -> None:
    """Handle the Update Task operation.

    Prompts user for task ID, new title, and new description,
    then updates the task if it exists.

    Args:
        task_service: The TaskService instance for task operations
    """
    print("\n--- Update Task ---")

    task_id_input = input("Enter task ID: ")
    task_id = validate_task_id(task_id_input)

    if task_id is None:
        print("\n✗ Error: Invalid ID format. Please enter a number.")
        return

    # Verify task exists
    task = task_service.get_task_by_id(task_id)
    if task is None:
        print(f"\n✗ Error: Task with ID {task_id} not found")
        return

    # Display current details
    print(f"\nCurrent title: {task.title}")
    print(f"Current description: {task.description}")

    try:
        # Prompt for new details
        new_title_input = input("\nEnter new title: ")
        new_title = validate_non_empty(new_title_input, "Title")

        new_desc_input = input("Enter new description: ")
        new_description = validate_non_empty(new_desc_input, "Description")

        # Update task
        task_service.update_task(task_id, new_title, new_description)
        print(f"\n✓ Task {task_id} updated successfully")

    except ValueError as e:
        print(f"\n✗ Error: {e}")
        print("Please try again.")


def handle_delete_task(task_service: TaskService) -> None:
    """Handle the Delete Task operation.

    Prompts user for task ID and deletes the task if it exists.

    Args:
        task_service: The TaskService instance for task operations
    """
    print("\n--- Delete Task ---")

    task_id_input = input("Enter task ID: ")
    task_id = validate_task_id(task_id_input)

    if task_id is None:
        print("\n✗ Error: Invalid ID format. Please enter a number.")
        return

    success = task_service.delete_task(task_id)

    if success:
        print(f"\n✓ Task {task_id} deleted successfully")
    else:
        print(f"\n✗ Error: Task with ID {task_id} not found")


def run_cli(task_service: TaskService) -> None:
    """Run the main CLI loop.

    Displays menu, captures user choice, and routes to appropriate handlers.
    Continues until user selects Exit option.

    Args:
        task_service: The TaskService instance for task operations
    """
    print("\n" + "=" * 50)
    print("Welcome to the Todo Application!")
    print("=" * 50)

    while True:
        display_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

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
            print("\nThank you for using the Todo Application!")
            print("Goodbye!\n")
            break
        else:
            print("\n✗ Error: Invalid option. Please select a valid menu item.")
