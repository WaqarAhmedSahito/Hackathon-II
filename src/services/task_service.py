"""Business logic for managing tasks."""

from typing import List, Optional

from models.task import Task


class TaskService:
    """Service class for managing tasks in memory.

    Provides CRUD operations and task completion tracking.
    All data is stored in memory and lost on application exit.
    """

    def __init__(self) -> None:
        """Initialize task service with empty task list."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def create_task(self, title: str, description: str) -> Task:
        """Create a new task with auto-generated ID.

        Args:
            title: Task title (required, max 200 characters).
            description: Task description (required, max 1000 characters).

        Returns:
            The created Task object with assigned ID.

        Raises:
            ValueError: If title or description is empty or exceeds length limits.
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        if len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters")

        if len(description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")

        task = Task(id=self.next_id, title=title.strip(), description=description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Return a copy of all tasks.

        Returns:
            List of all Task objects (empty list if no tasks exist).
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Find a task by its ID.

        Args:
            task_id: The numeric ID of the task to find.

        Returns:
            The Task object if found, None otherwise.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str, description: str) -> bool:
        """Update an existing task's title and description.

        Args:
            task_id: The numeric ID of the task to update.
            title: New title for the task (required, max 200 characters).
            description: New description for the task (required, max 1000 characters).

        Returns:
            True if task was found and updated, False if task not found.

        Raises:
            ValueError: If title or description is empty or exceeds length limits.
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        if len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters")

        if len(description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")

        task.title = title.strip()
        task.description = description.strip()
        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: The numeric ID of the task to delete.

        Returns:
            True if task was found and deleted, False if task not found.
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def toggle_complete(self, task_id: int) -> bool:
        """Toggle the completion status of a task.

        Args:
            task_id: The numeric ID of the task to toggle.

        Returns:
            True if task was found and toggled, False if task not found.
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = not task.completed
        return True
