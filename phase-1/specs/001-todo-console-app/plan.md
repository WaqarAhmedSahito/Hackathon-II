# Implementation Plan: In-Memory Python Console Todo Application

**Branch**: `001-todo-console-app` | **Date**: 2025-12-28 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-console-app/spec.md`

## Summary

Build a command-line todo application with in-memory storage supporting five core operations: create tasks with title/description, view task list with status indicators, update task details, delete tasks by ID, and toggle completion status. Implementation uses Python 3.13+ with standard library only, following spec-driven development methodology and clean code principles from the project constitution.

**Technical Approach**: Dataclass-based Task model for type safety and readability, incremental integer ID generation for simplicity, menu-driven CLI interface for user-friendliness, and modular architecture separating models (data), services (business logic), and CLI (user interaction).

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (dataclasses, typing)
**Storage**: In-memory (list-based task storage, session-scoped)
**Testing**: Manual console testing against acceptance criteria (no automated test framework per constitution)
**Target Platform**: Cross-platform console (Windows, macOS, Linux)
**Project Type**: Single project (console application)
**Performance Goals**: Sub-500ms response time for operations on lists up to 100 tasks
**Constraints**: No external dependencies, no persistence, PEP 8 compliance mandatory, max 50 lines per function
**Scale/Scope**: Single-user, single-session, typical usage 10-50 tasks, max validated 100 tasks

## Constitution Check

*GATE: Must pass before implementation. Re-check after design.*

✅ **I. Spec-Driven Development**: Spec.md completed and validated before this plan; implementation will follow spec strictly
✅ **II. Spec-Kit Plus Integration**: Using specs/001-todo-console-app/ structure; history/prompts/ for PHRs; ADR planned for architectural decisions
✅ **III. Clean Code Standards**: PEP 8 enforcement, modular design (models/services/cli separation), docstrings for all public functions, specific exception handling
✅ **IV. Minimal Viable Implementation**: Five features only, in-memory storage, console-only, standard library, no over-engineering
✅ **V. AI-Assisted Development**: Code generation from spec with human review, documented in commits with "(AI-assisted)" marker
✅ **VI. Testing and Quality Validation**: Manual testing against all acceptance criteria, edge case validation, demonstration scenarios in README

**All constitution principles satisfied.** No violations requiring justification.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-console-app/
├── spec.md              # Feature specification (completed)
├── plan.md              # This file (implementation plan)
├── checklists/
│   └── requirements.md  # Spec quality checklist (validated)
└── tasks.md             # Task breakdown (to be created by /sp.tasks)
```

### Source Code (repository root)

```text
phase-1/
├── .specify/
│   ├── memory/
│   │   └── constitution.md
│   └── templates/
├── specs/
│   └── 001-todo-console-app/
├── history/
│   ├── prompts/
│   │   ├── constitution/
│   │   └── 001-todo-console-app/
│   └── adr/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py           # Task dataclass
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py   # TaskService class (CRUD operations)
│   ├── cli/
│   │   ├── __init__.py
│   │   └── cli.py            # CLI interface (menu, input handling)
│   ├── __init__.py
│   └── main.py               # Application entry point
├── README.md                 # Setup, usage, demo scenarios
└── pyproject.toml            # UV project configuration
```

**Structure Decision**: Selected "Single project" structure (Option 1 from template) as this is a standalone console application. The `src/` directory contains three modules:
- `models/`: Data structures (Task dataclass)
- `services/`: Business logic (TaskService with in-memory storage and CRUD operations)
- `cli/`: User interface (menu display, input validation, command routing)

This separation adheres to constitution's modular design principle and single-responsibility principle, making code testable and maintainable.

## Complexity Tracking

> **No violations detected.** This section intentionally left empty as all constitution checks pass.

## Architecture

### Component Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         main.py                             │
│  - Entry point                                              │
│  - Initializes TaskService                                  │
│  - Starts CLI loop                                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                      cli/cli.py                             │
│  - Display menu                                             │
│  - Capture user input                                       │
│  - Validate input (ID format, empty strings)                │
│  - Route commands to TaskService                            │
│  - Display results and error messages                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               services/task_service.py                      │
│  - TaskService class                                        │
│  - In-memory storage: List[Task]                            │
│  - CRUD operations:                                         │
│    • create_task(title, desc) -> Task                       │
│    • get_all_tasks() -> List[Task]                          │
│    • get_task_by_id(id) -> Optional[Task]                   │
│    • update_task(id, title, desc) -> bool                   │
│    • delete_task(id) -> bool                                │
│    • toggle_complete(id) -> bool                            │
│  - ID generation: incremental integer counter               │
│  - Input validation (length limits, required fields)        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   models/task.py                            │
│  - Task dataclass                                           │
│    • id: int                                                │
│    • title: str                                             │
│    • description: str                                       │
│    • completed: bool = False                                │
│  - Method: format_status() -> str  (returns "[ ]" or "[x]") │
│  - Method: __str__() for display formatting                 │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

**Example: Add Task Flow**
1. User selects "1. Add Task" from menu (cli.py)
2. CLI prompts for title and description
3. CLI validates inputs (non-empty, length limits)
4. CLI calls `task_service.create_task(title, desc)`
5. TaskService validates again, generates next ID
6. TaskService creates Task instance, adds to in-memory list
7. TaskService returns Task object
8. CLI displays confirmation: "Task <ID> created successfully"
9. CLI returns to main menu

**Example: View Tasks Flow**
1. User selects "2. View Tasks" from menu
2. CLI calls `task_service.get_all_tasks()`
3. TaskService returns `List[Task]`
4. CLI checks if list is empty → display "No tasks found"
5. Otherwise, CLI iterates tasks and displays:
   ```
   [x] ID: 1 | Title: Implement login
       Description: Create user authentication system
   [ ] ID: 2 | Title: Write tests
       Description: Add unit tests for auth module
   ```
6. CLI returns to main menu

### Error Handling Strategy

**Input Validation Errors** (handled in CLI layer):
- Empty title/description → "Title cannot be empty" → re-prompt
- Invalid ID format (non-numeric) → "Invalid ID format. Please enter a number." → re-prompt
- Invalid menu option → "Invalid option. Please select a valid menu item." → re-display menu

**Business Logic Errors** (handled in TaskService):
- Task ID not found → Return `None` or `False` → CLI displays "Task with ID {id} not found"
- Title/description exceeds length limits → Raise `ValueError` → CLI catches and displays specific error

**System Errors** (handled at main.py level):
- Unexpected exceptions → Log to stderr, display generic "An error occurred", return to menu (don't crash)

All errors allow user to retry without restarting application (per constitution principle VI).

## Architectural Decisions

### ADR-001: Task Representation - Dataclass vs. Dictionary

**Decision**: Use Python `dataclass` for Task entity

**Context**: Need to represent tasks with four attributes (id, title, description, completed). Two options considered:
1. Dataclass: Structured type with explicit fields
2. Dictionary: Flexible key-value pairs

**Rationale**:
- **Type Safety**: Dataclass provides type hints for IDE support and static analysis
- **Readability**: Explicit field definitions (`task.title`) clearer than dict access (`task['title']`)
- **Validation**: Dataclass supports field validators and post-init processing
- **Consistency**: Aligns with constitution's "clean code" principle (clear, descriptive naming)
- **Minimal Overhead**: Dataclass is standard library, no external dependency

**Trade-offs Accepted**:
- Slightly more verbose than dict (requires class definition)
- Less flexible for dynamic fields (not needed for this spec)

**Alternatives Rejected**:
- Dictionary: Lacks type safety, error-prone key access, harder to maintain
- Named Tuple: Immutable (spec requires update functionality)
- Full class with `__init__`: Unnecessary boilerplate for simple data structure

### ADR-002: ID Generation - Incremental Integer vs. UUID

**Decision**: Use incremental integer starting from 1

**Context**: Each task needs a unique identifier. Two primary options:
1. Incremental integer (1, 2, 3, ...)
2. UUID (universally unique identifier)

**Rationale**:
- **Simplicity**: Integers are easy to understand and type for users
- **User Experience**: Sequential IDs are predictable and memorable in console interface
- **Scope**: Single-session, single-user application doesn't require global uniqueness
- **Performance**: Integer comparison faster than UUID (negligible at <100 tasks scale)
- **Spec Alignment**: Spec mentions "numeric ID" and shows examples like "ID: 1", "ID: 2"

**Trade-offs Accepted**:
- ID gaps after deletion (acceptable per spec assumptions)
- Not suitable for distributed systems (not required)

**Alternatives Rejected**:
- UUID: Overly complex for single-session use; 36-char strings awkward in console
- Timestamp-based: Can have collisions, harder to type
- Random integers: Risk of collision, not sequential

### ADR-003: CLI Input Style - Free Commands vs. Menu Navigation

**Decision**: Use numbered menu navigation with prompted inputs

**Context**: User interaction model for console interface. Options:
1. Free-form commands (e.g., `add "title" "description"`)
2. Menu navigation with prompts

**Rationale**:
- **User-Friendliness**: Menu-driven is more discoverable (users see all options)
- **Error Prevention**: Prompts guide users step-by-step, reducing syntax errors
- **Spec Alignment**: Spec acceptance criteria reference "select 'Add Task'" suggesting menu-style
- **Consistency**: Each operation follows same pattern (menu → prompts → confirmation)
- **Validation**: Easier to validate individual prompted inputs than parsing command strings

**Trade-offs Accepted**:
- Slightly more verbose for experienced users (multiple prompts vs. one-line command)
- Not scriptable (can't chain commands easily)

**Alternatives Rejected**:
- Free-form commands: Requires argument parsing, error-prone, steeper learning curve
- Hybrid (menu + commands): Added complexity violates minimal viable implementation principle

**Implementation Notes**:
- Menu displays on every loop iteration
- Input validation happens immediately after each prompt
- Confirmation messages displayed before returning to menu

## Development Workflow

### Spec-Driven Iterative Approach

**Workflow Pattern** (per constitution):
1. **Spec First**: Feature requirements defined in spec.md (completed)
2. **Plan**: Architecture and design documented in plan.md (this file)
3. **Implement**: Code modules following plan
4. **Validate**: Manual testing against spec acceptance criteria
5. **Refine Spec**: If gaps discovered, update spec.md and commit to history
6. **Commit**: Git commit with descriptive message and "(AI-assisted)" tag if applicable

**Phase Structure**:

```
Phase 0: Foundation Setup
└─> Phase 1: Data Model & Service
    └─> Phase 2: CLI Core (Add/View)
        └─> Phase 3: Extended Operations (Update/Delete/Mark)
            └─> Phase 4: Polish & Validation
```

### Phase 0: Foundation Setup

**Goal**: Initialize project structure and validate environment

**Tasks**:
1. Verify Python 3.13+ installed
2. Initialize UV project with `pyproject.toml`
3. Create directory structure: `src/models/`, `src/services/`, `src/cli/`
4. Add `__init__.py` files to make packages importable
5. Create placeholder README.md with project description

**Acceptance**: `src/` structure exists, `python --version` shows 3.13+, UV project initialized

**Estimated Complexity**: Low (setup only, no business logic)

### Phase 1: Data Model & Service Layer

**Goal**: Implement Task model and TaskService with CRUD operations

**Tasks**:
1. **models/task.py**:
   - Define Task dataclass with fields: `id`, `title`, `description`, `completed`
   - Add `format_status()` method returning "[ ]" or "[x]"
   - Add `__str__()` method for formatted display
   - Include docstrings for class and methods

2. **services/task_service.py**:
   - Define TaskService class
   - Initialize `tasks: List[Task] = []` and `next_id: int = 1`
   - Implement `create_task(title: str, description: str) -> Task`
     - Validate title/desc not empty (raise ValueError)
     - Validate length limits (200 title, 1000 desc)
     - Generate ID, create Task, append to list, increment next_id
   - Implement `get_all_tasks() -> List[Task]`
   - Implement `get_task_by_id(task_id: int) -> Optional[Task]`
   - Implement `update_task(task_id: int, title: str, description: str) -> bool`
   - Implement `delete_task(task_id: int) -> bool`
   - Implement `toggle_complete(task_id: int) -> bool`
   - Include comprehensive docstrings

**Acceptance**:
- Can instantiate TaskService
- Can create task and retrieve by ID
- All CRUD methods return expected values/types
- Validation errors raised appropriately

**Estimated Complexity**: Medium (core business logic, critical for all features)

### Phase 2: CLI Core - Add & View Tasks

**Goal**: Implement menu interface with Add and View operations (User Story 1 / P1)

**Tasks**:
1. **cli/cli.py**:
   - Define `display_menu()` function showing 6 options
   - Define `run_cli(task_service: TaskService)` main loop
   - Implement `handle_add_task(task_service)`:
     - Prompt for title (validate non-empty)
     - Prompt for description (validate non-empty)
     - Call `task_service.create_task()`
     - Display confirmation message
   - Implement `handle_view_tasks(task_service)`:
     - Call `get_all_tasks()`
     - If empty, display "No tasks found"
     - Otherwise, iterate and display formatted tasks with status indicators
   - Add input validation helper `validate_non_empty(input, field_name) -> str`
   - Include docstrings

2. **main.py**:
   - Initialize TaskService instance
   - Call `cli.run_cli(task_service)`
   - Wrap in try-except for graceful error handling

**Acceptance**:
- Menu displays with 6 options
- Can add task with title and description → confirmation shown
- Can view tasks → displays list with status indicators
- Empty list shows "No tasks found"
- Invalid inputs (empty title) show error and re-prompt

**Test Scenarios** (from spec User Story 1):
- Add task "Implement login" / "Create user authentication system" → ID 1 assigned
- Add 2 more tasks → IDs 2, 3 assigned
- View tasks → all 3 displayed with [ ] status
- View tasks with empty list → "No tasks found"

**Estimated Complexity**: Medium (user interaction, validation, formatting)

### Phase 3: Extended Operations - Update, Delete, Mark Complete

**Goal**: Implement remaining CRUD operations (User Stories 2, 3, 4 / P2, P3, P4)

**Tasks**:
1. **cli/cli.py** (extend):
   - Implement `handle_mark_complete(task_service)`:
     - Prompt for task ID (validate numeric)
     - Call `task_service.toggle_complete(id)`
     - Display success message with new status OR "Task not found"
   - Implement `handle_update_task(task_service)`:
     - Prompt for task ID (validate numeric)
     - Verify task exists, display current details
     - Prompt for new title and description
     - Call `task_service.update_task()`
     - Display success OR "Task not found"
   - Implement `handle_delete_task(task_service)`:
     - Prompt for task ID (validate numeric)
     - Call `task_service.delete_task()`
     - Display success OR "Task not found"
   - Add input validation helper `validate_task_id(input) -> Optional[int]`
   - Wire handlers to menu options in `run_cli()`

**Acceptance**:
- Can mark task complete by ID → status changes to [x]
- Can mark complete task incomplete → toggles back to [ ]
- Can update task title and description → changes persist
- Can delete task by ID → removed from list
- Invalid IDs show "Task with ID {id} not found"
- Non-numeric IDs show "Invalid ID format"

**Test Scenarios** (from spec User Stories 2, 3, 4):
- Mark task 2 complete → [x] indicator shown in view
- Mark task 2 again → [ ] indicator (toggle)
- Update task 1 title to "Updated Title" → persists in view
- Delete task 2 → only tasks 1, 3 remain

**Estimated Complexity**: Medium (multiple operations, ID lookup, error handling)

### Phase 4: Polish, README & Final Validation

**Goal**: Finalize application, documentation, and comprehensive testing

**Tasks**:
1. **Code Review**:
   - Verify PEP 8 compliance (use `black` or manual review)
   - Check all functions have docstrings
   - Ensure error messages match spec examples
   - Verify max 50 lines per function (constitution rule)

2. **README.md**:
   - **Setup Instructions**:
     - Python 3.13+ installation
     - Running with UV: `uv run python src/main.py`
   - **Usage Guide**:
     - Menu navigation
     - Example commands for each operation
   - **Demonstration Scenarios** (from constitution):
     - Add three tasks
     - List all tasks with status
     - Update one task
     - Mark one complete
     - Delete one task
     - List remaining tasks

3. **Manual Testing**:
   - Execute all acceptance scenarios from spec (12 scenarios across 4 user stories)
   - Test all edge cases (5 documented in spec):
     - Empty title/description → validation error
     - Long inputs (200+ title, 1000+ desc) → truncate or error
     - Non-numeric ID → format error
     - Exit application → clean termination
     - Invalid menu option → error and re-prompt
   - Verify success criteria:
     - SC-001: Full lifecycle works without crashes
     - SC-002: Feature location under 10 seconds
     - SC-003: Error messages under 1 second, retry enabled
     - SC-004: Status indicators consistent
     - SC-005: Operations under 500ms for 100 tasks
     - SC-006: Code is modular, PEP 8 compliant, documented

4. **Final Commit**:
   - Commit all code with message: `feat: implement todo console app (AI-assisted)`
   - Update spec status from "Draft" to "Implemented"
   - Create PHR documenting implementation completion

**Acceptance**:
- All 12 acceptance scenarios pass
- All 5 edge cases handled correctly
- All 6 success criteria validated
- README complete with setup and demo
- Code review complete (PEP 8, docstrings, no violations)

**Estimated Complexity**: Low-Medium (validation and documentation, no new features)

## Testing Strategy

### Manual Testing Approach

Per constitution principle VI, manual testing is required as no automated test framework is specified.

**Testing Phases**:

1. **Unit-Level Validation** (during Phase 1):
   - Test TaskService methods in isolation using Python REPL
   - Verify `create_task()` generates correct IDs
   - Verify `get_task_by_id()` returns correct task or None
   - Verify `update_task()`, `delete_task()`, `toggle_complete()` modify state correctly

2. **Integration Testing** (during Phases 2-3):
   - Run full application in console
   - Execute each user story's acceptance scenarios
   - Verify CLI correctly routes to TaskService
   - Verify results displayed match expected output

3. **Edge Case Testing** (during Phase 4):
   - Systematically test all 5 edge cases from spec
   - Test with 0 tasks (empty list)
   - Test with 100 tasks (performance validation)
   - Test rapid operations (add, delete, add, mark complete)

**Test Documentation** (in README.md):

```markdown
## Testing Checklist

### User Story 1: Create and View Tasks (P1)
- [ ] Add task "Implement login" / "Create auth system" → ID 1, [ ] status
- [ ] Add 2 more tasks → IDs 2, 3 assigned
- [ ] View tasks → all 3 displayed with ID, title, desc, [ ] status
- [ ] View empty list → "No tasks found" message

### User Story 2: Mark Tasks Complete (P2)
- [ ] Mark task 2 complete → [x] status shown
- [ ] Mark task 2 again → [ ] status (toggle)
- [ ] Mark invalid ID 999 → "Task with ID 999 not found"

### User Story 3: Update Task Details (P3)
- [ ] Update task 1 title to "Updated Title" → persists
- [ ] Update task 1 description → persists
- [ ] Update invalid ID 999 → "Task not found"

### User Story 4: Delete Tasks (P4)
- [ ] Delete task 2 → removed from list
- [ ] View tasks → only 1, 3 remain
- [ ] Delete invalid ID 999 → "Task not found"

### Edge Cases
- [ ] Add task with empty title → "Title cannot be empty"
- [ ] Add task with 250-char title → handle gracefully
- [ ] Enter "abc" for task ID → "Invalid ID format"
- [ ] Select menu option "9" → "Invalid option"
- [ ] Exit application → clean termination, no errors

### Success Criteria Validation
- [ ] SC-001: Full lifecycle (add, view, update, mark, delete) → no crashes
- [ ] SC-002: Locate any feature in menu → under 10 seconds
- [ ] SC-003: Error messages → displayed under 1 second, retry enabled
- [ ] SC-004: Status indicators → [ ] and [x] consistent across operations
- [ ] SC-005: Performance → add/view/update/delete on 100 tasks → under 500ms each
- [ ] SC-006: Code quality → PEP 8 compliant, modular, documented
```

**Testing Tools**:
- Python REPL for service layer validation
- Console terminal for full application testing
- Manual timing for performance validation (use `time` command or stopwatch)

**Defect Handling**:
- If test fails, note in testing checklist
- Fix defect in code
- Re-run failed test scenario
- Update spec if requirement was ambiguous (commit to history)

## Quality Validation Steps

### Pre-Implementation Checklist

Before starting Phase 1:
- [x] Spec.md completed and validated (checklist passed)
- [x] Plan.md completed (this file)
- [x] Constitution principles reviewed
- [x] Architectural decisions documented (ADRs 001-003)
- [ ] Development environment verified (Python 3.13+, UV installed)

### During Implementation

After each phase:
- [ ] Code follows PEP 8 (use `python -m black --check src/` or manual review)
- [ ] All functions have docstrings (Google style)
- [ ] No functions exceed 50 lines
- [ ] Error handling uses specific exceptions (ValueError, KeyError, etc.)
- [ ] User-facing error messages match spec examples
- [ ] Phase acceptance criteria met (documented per phase above)

### Post-Implementation Checklist

Before marking feature complete:
- [ ] All 12 acceptance scenarios pass
- [ ] All 5 edge cases handled correctly
- [ ] All 6 success criteria validated
- [ ] README.md complete with setup, usage, demo scenarios
- [ ] Code review complete (no constitution violations)
- [ ] Demonstration run recorded in README (transcript or screenshots optional)
- [ ] Spec status updated to "Implemented"
- [ ] Final commit with "(AI-assisted)" marker
- [ ] PHR created documenting completion

## Risks & Mitigation

### Risk 1: Input Validation Gaps

**Description**: User enters unexpected input (unicode, special chars, very long strings) not covered in edge cases

**Likelihood**: Medium | **Impact**: Medium (crashes or incorrect behavior)

**Mitigation**:
- Add try-except around all input prompts
- Test with intentionally malformed input during Phase 4
- Fallback to generic error message if unexpected exception occurs

### Risk 2: ID Management After Deletion

**Description**: Deleting tasks creates ID gaps; users might expect sequential IDs

**Likelihood**: Low | **Impact**: Low (spec explicitly allows gaps)

**Mitigation**:
- Document behavior in README
- Spec assumption already states "gaps in sequence are acceptable"
- If user feedback indicates confusion, add explanation in view output

### Risk 3: Performance Degradation at Scale

**Description**: Linear search for `get_task_by_id()` may slow down with many tasks

**Likelihood**: Low | **Impact**: Low (spec targets <100 tasks, linear search acceptable)

**Mitigation**:
- Success criterion SC-005 validates performance at 100 tasks
- If needed, switch to dict-based storage (`{id: Task}`) - minimal code change
- Constitution permits optimization only if justified by actual performance failure

## Next Steps

1. **Immediate**: Run `/sp.tasks` to generate detailed task breakdown from this plan
2. **After `/sp.tasks`**: Execute Phase 0 (Foundation Setup)
3. **Iterative Implementation**: Phases 1-4 in sequence, validating after each phase
4. **Final Validation**: Complete testing checklist and quality validation steps
5. **Documentation**: Update README with demo scenarios
6. **Completion**: Update spec status, create PHR, commit final code

---

**Plan Status**: ✅ Complete - Ready for `/sp.tasks`
**Architecture Decisions**: 3 ADRs documented (dataclass, incremental IDs, menu navigation)
**Constitution Compliance**: All 6 principles validated
**Next Command**: `/sp.tasks`
