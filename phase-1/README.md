# In-Memory Python Console Todo Application

A command-line todo application demonstrating spec-driven development with clean code principles. This project showcases a minimal viable product for task management via console interface, suitable for hackathon projects and learning spec-driven development methodologies.

## Features

- **Add Tasks**: Create tasks with title and description
- **View Tasks**: List all tasks with status indicators ([ ] incomplete, [x] complete)
- **Update Tasks**: Modify task details by ID
- **Delete Tasks**: Remove tasks by ID
- **Mark Complete/Incomplete**: Toggle task completion status

## Requirements

- **Python 3.13+**
- No external dependencies (uses Python standard library only)

## Setup Instructions

1. **Clone the repository** (or ensure you have the project files)

2. **Verify Python version**:
   ```bash
   python --version
   ```
   Ensure you have Python 3.13 or higher installed.

3. **Navigate to the project directory**:
   ```bash
   cd phase-1
   ```

## Running the Application

**From the project root directory** (`phase-1/`):

```bash
cd src
python main.py
```

Or run directly from the `src/` directory:

```bash
# If you're already in src/
python main.py
```

**Alternative** (if using UV from project root):

```bash
uv run python src/main.py
```

## Usage Guide

Once the application starts, you'll see a menu with 6 options:

```
==================================================
TODO APPLICATION - MAIN MENU
==================================================
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit
==================================================
```

### Menu Navigation

- Enter a number (1-6) to select an operation
- Follow the prompts for each operation
- The application will display confirmation messages or errors
- Press Ctrl+C at any time to exit

### Operation Examples

**1. Adding a Task**:
- Select option `1`
- Enter task title (e.g., "Implement login")
- Enter task description (e.g., "Create user authentication system")
- Task is created with a unique ID

**2. Viewing Tasks**:
- Select option `2`
- All tasks are displayed with:
  - Status indicator: `[ ]` for incomplete, `[x]` for complete
  - Task ID
  - Title
  - Description

**3. Updating a Task**:
- Select option `3`
- Enter the task ID
- Current details are displayed
- Enter new title and description
- Task is updated with new details

**4. Deleting a Task**:
- Select option `4`
- Enter the task ID
- Task is removed from the list

**5. Marking Complete/Incomplete**:
- Select option `5`
- Enter the task ID
- Task status toggles between complete and incomplete

**6. Exiting**:
- Select option `6`
- Application terminates (all data is lost as it's in-memory only)

## Demonstration Scenarios

### Scenario 1: Basic Task Management

1. **Start the application**:
   ```bash
   cd src
   python main.py
   ```

2. **Add three tasks**:
   - Task 1: "Implement login" / "Create user authentication system"
   - Task 2: "Write tests" / "Add unit tests for auth module"
   - Task 3: "Update documentation" / "Document API endpoints"

3. **List all tasks**:
   - Select option `2`
   - Verify all 3 tasks display with `[ ]` status

4. **Update a task**:
   - Select option `3`
   - Enter ID `2`
   - Update to: "Write comprehensive tests" / "Add unit and integration tests"

5. **Mark a task complete**:
   - Select option `5`
   - Enter ID `1`
   - Verify task 1 now shows `[x]` status

6. **Delete a task**:
   - Select option `4`
   - Enter ID `3`
   - Verify task 3 is removed

7. **List remaining tasks**:
   - Select option `2`
   - Verify only tasks 1 and 2 remain (ID gaps are normal)

### Scenario 2: Error Handling

**Test empty inputs**:
- Select option `1` (Add Task)
- Press Enter without typing a title
- Observe error: "Title cannot be empty"

**Test invalid task ID**:
- Select option `5` (Mark Complete)
- Enter `999` (non-existent ID)
- Observe error: "Task with ID 999 not found"

**Test invalid ID format**:
- Select option `4` (Delete Task)
- Enter `abc` (non-numeric)
- Observe error: "Invalid ID format. Please enter a number."

**Test invalid menu option**:
- Enter `9` at main menu
- Observe error: "Invalid option. Please select a valid menu item."

## Project Structure

```
phase-1/
├── .specify/
│   ├── memory/
│   │   └── constitution.md          # Project governance principles
│   └── templates/                    # Spec-Kit Plus templates
├── specs/
│   └── 001-todo-console-app/
│       ├── spec.md                   # Feature specification
│       ├── plan.md                   # Implementation plan
│       ├── tasks.md                  # Task breakdown
│       └── checklists/
│           └── requirements.md       # Spec quality checklist
├── history/
│   └── prompts/                      # Prompt History Records
│       ├── constitution/
│       └── 001-todo-console-app/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py                   # Task dataclass
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py           # Business logic (CRUD)
│   ├── cli/
│   │   ├── __init__.py
│   │   └── cli.py                    # Command-line interface
│   ├── __init__.py
│   └── main.py                       # Application entry point
├── README.md                         # This file
└── CLAUDE.md                         # Claude Code instructions
```

## Architecture

The application follows a clean, modular architecture:

- **Models** (`src/models/`): Data structures (Task dataclass)
- **Services** (`src/services/`): Business logic and CRUD operations
- **CLI** (`src/cli/`): User interface and input handling
- **Main** (`src/main.py`): Entry point with error handling

## Data Storage

- **In-Memory Only**: All tasks are stored in memory during the session
- **Session-Scoped**: Data is lost when the application exits (intentional behavior)
- **ID Management**: Task IDs are sequential integers starting from 1
- **ID Gaps**: Deleting tasks creates gaps in ID sequence (this is normal and acceptable)

## Code Quality

This project adheres to:
- **PEP 8**: Python code style guide
- **Clean Code**: Modular design, single-responsibility principle
- **Documentation**: Google-style docstrings for all public functions and classes
- **Error Handling**: Specific exceptions with clear error messages
- **No External Dependencies**: Uses Python standard library only

## Development Methodology

This project demonstrates:
- **Spec-Driven Development (SDD)**: Specifications written before implementation
- **Spec-Kit Plus Integration**: Structured governance and traceability
- **Constitution-Based Development**: Following defined project principles
- **Incremental Delivery**: User stories implemented independently and tested

## Limitations

- **No Persistence**: Tasks are not saved to disk or database
- **Single Session**: All data is lost when application exits
- **No Concurrent Users**: Designed for single-user, single-session use
- **Console Only**: No GUI or web interface
- **Manual Testing**: No automated test framework (per project constitution)

## Testing

Manual testing has been performed against all acceptance criteria:
- ✅ Add tasks with title and description
- ✅ View task list with status indicators
- ✅ Update task details by ID
- ✅ Delete tasks by ID
- ✅ Mark tasks as complete/incomplete (toggle functionality)
- ✅ Empty input validation
- ✅ Invalid ID error handling
- ✅ Invalid menu option handling
- ✅ Clean exit behavior

## License

This is a hackathon project for educational purposes.

## Author

Created as part of "The Evolution of Todo - Phase I" hackathon project demonstrating spec-driven development with Python 3.13+.
