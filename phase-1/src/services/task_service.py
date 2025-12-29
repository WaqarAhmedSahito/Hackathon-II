"""TaskService for managing todo tasks in memory."""

from typing import List, Optional
from models.task import Task


class TaskService:
    """Service class for managing todo tasks with CRUD operations.

    Provides in-memory storage and business logic for task management.
    Tasks are stored in a list with auto-incrementing numeric IDs.
    """

    def __init__(self):
        """Initialize TaskService with empty task list and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def create_task(self, title: str, description: str) -> Task:
        """Create a new task with the given title and description.

        Args:
            title: Task title (required, max 200 characters)
            description: Task description (required, max 1000 characters)

        Returns:
            Task: The newly created task with auto-generated ID

        Raises:
            ValueError: If title or description is empty or exceeds length limits
        """
        # Validate required fields
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        # Validate length limits
        if len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters")
        if len(description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")

        # Create task with auto-generated ID
        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description.strip(),
            completed=False
        )

        self.tasks.append(task)
        self.next_id += 1

        return task

    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks in the current session.

        Returns:
            List[Task]: A copy of the task list (empty list if no tasks exist)
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Find and return a task by its ID.

        Args:
            task_id: The unique ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(
        self, task_id: int, title: str, description: str
    ) -> bool:
        """Update the title and description of an existing task.

        Args:
            task_id: The ID of the task to update
            title: New task title (required, max 200 characters)
            description: New task description (required, max 1000 characters)

        Returns:
            bool: True if task was found and updated, False if task not found

        Raises:
            ValueError: If title or description is empty or exceeds length limits
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Validate required fields
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        # Validate length limits
        if len(title) > 200:
            raise ValueError("Title cannot exceed 200 characters")
        if len(description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")

        # Update task
        task.title = title.strip()
        task.description = description.strip()

        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if task was found and deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def toggle_complete(self, task_id: int) -> bool:
        """Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            bool: True if task was found and toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = not task.completed
        return True
