"""Main entry point for the todo application."""

import sys

from cli.cli import run_cli
from services.task_service import TaskService


def main() -> None:
    """Run the todo application."""
    task_service = TaskService()
    try:
        run_cli(task_service)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
