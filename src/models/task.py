"""Task data model for the todo application."""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo item.

    Attributes:
        id: Unique numeric identifier for the task.
        title: Short name or summary of the task (max 200 characters).
        description: Detailed information about the task (max 1000 characters).
        completed: Completion state (False for incomplete, True for complete).
    """

    id: int
    title: str
    description: str
    completed: bool = False

    def format_status(self) -> str:
        """Return formatted status indicator.

        Returns:
            "[x]" if task is complete, "[ ]" if incomplete.
        """
        return "[x]" if self.completed else "[ ]"

    def __str__(self) -> str:
        """Return formatted string representation for display.

        Returns:
            Formatted string with status, ID, title, and description.
        """
        return (
            f"{self.format_status()} ID: {self.id} | Title: {self.title}\n"
            f"    Description: {self.description}"
        )
