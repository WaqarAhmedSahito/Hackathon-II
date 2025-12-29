"""Main entry point for the In-Memory Python Console Todo Application."""

import sys
from services.task_service import TaskService
from cli.cli import run_cli


def main():
    """Initialize the application and start the CLI."""
    try:
        # Initialize TaskService
        task_service = TaskService()

        # Start CLI
        run_cli(task_service)

    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        print("Goodbye!\n")
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {e}", file=sys.stderr)
        print("Please restart the application.\n", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
