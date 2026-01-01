---

description: "Task list for In-Memory Python Console Todo Application"
---

# Tasks: In-Memory Python Console Todo Application

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Manual testing only - no automated tests per constitution requirement

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, at repository root
- Paths shown below use single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Verify Python 3.13+ installed and accessible via command line
- [X] T002 Initialize UV project with pyproject.toml in repository root
- [X] T003 Create src/ directory structure: src/models/, src/services/, src/cli/
- [X] T004 [P] Create __init__.py in src/ to make it a package
- [X] T005 [P] Create __init__.py in src/models/ to make it a package
- [X] T006 [P] Create __init__.py in src/services/ to make it a package
- [X] T007 [P] Create __init__.py in src/cli/ to make it a package
- [X] T008 Create placeholder README.md with project title and description

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 Define Task dataclass in src/models/task.py with fields: id (int), title (str), description (str), completed (bool, default False)
- [X] T010 Add format_status() method to Task class in src/models/task.py returning "[ ]" for incomplete or "[x]" for complete
- [X] T011 Add __str__() method to Task class in src/models/task.py for formatted display output
- [X] T012 Add Google-style docstring to Task class in src/models/task.py documenting class purpose and attributes
- [X] T013 Create TaskService class in src/services/task_service.py with __init__ method initializing empty task list and next_id counter
- [X] T014 Implement create_task(title: str, description: str) -> Task method in src/services/task_service.py with validation for empty fields and length limits (200 title, 1000 desc)
- [X] T015 Implement get_all_tasks() -> List[Task] method in src/services/task_service.py returning copy of task list
- [X] T016 Implement get_task_by_id(task_id: int) -> Optional[Task] method in src/services/task_service.py with linear search
- [X] T017 Implement update_task(task_id: int, title: str, description: str) -> bool method in src/services/task_service.py returning True if task found and updated, False otherwise
- [X] T018 Implement delete_task(task_id: int) -> bool method in src/services/task_service.py returning True if task found and removed, False otherwise
- [X] T019 Implement toggle_complete(task_id: int) -> bool method in src/services/task_service.py flipping completed status and returning True if task found, False otherwise
- [X] T020 Add comprehensive Google-style docstrings to all methods in src/services/task_service.py documenting parameters, return values, and raised exceptions

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Implement core task creation and viewing functionality with menu-driven interface

**Independent Test**: Launch application, add 2-3 tasks with different titles and descriptions, view task list to verify all tasks display with correct ID, title, description, and status indicators ([ ] for incomplete)

### Implementation for User Story 1

- [X] T021 [P] [US1] Create display_menu() function in src/cli/cli.py showing 6 numbered menu options: Add Task, View Tasks, Update Task, Delete Task, Mark Complete/Incomplete, Exit
- [X] T022 [P] [US1] Create validate_non_empty(user_input: str, field_name: str) -> str helper function in src/cli/cli.py raising ValueError if input is empty
- [X] T023 [US1] Implement handle_add_task(task_service: TaskService) function in src/cli/cli.py prompting for title and description, validating non-empty, calling task_service.create_task(), and displaying confirmation message
- [X] T024 [US1] Implement handle_view_tasks(task_service: TaskService) function in src/cli/cli.py calling get_all_tasks(), displaying "No tasks found" if empty, otherwise iterating and printing each task with format_status() indicator
- [X] T025 [US1] Create run_cli(task_service: TaskService) function in src/cli/cli.py with infinite loop displaying menu, capturing user choice, routing to appropriate handler, and handling "Exit" option
- [X] T026 [US1] Add Google-style docstrings to all functions in src/cli/cli.py documenting purpose, parameters, and behavior
- [X] T027 [US1] Create src/main.py entry point importing TaskService and run_cli, initializing TaskService instance, calling run_cli(task_service)
- [X] T028 [US1] Wrap run_cli() call in src/main.py with try-except block catching all exceptions, logging to stderr, and exiting gracefully

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently - can add tasks and view task list with status indicators

---

## Phase 4: User Story 2 - Mark Tasks Complete (Priority: P2)

**Goal**: Implement task completion status tracking with toggle functionality

**Independent Test**: Create 2-3 tasks using US1 functionality, mark one task complete by ID, view task list to verify [x] status indicator, mark same task incomplete to verify toggle back to [ ] indicator

### Implementation for User Story 2

- [X] T029 [P] [US2] Create validate_task_id(user_input: str) -> Optional[int] helper function in src/cli/cli.py attempting int conversion and returning None if ValueError occurs
- [X] T030 [US2] Implement handle_mark_complete(task_service: TaskService) function in src/cli/cli.py prompting for task ID, validating numeric format, calling task_service.toggle_complete(id), displaying success with new status or "Task with ID {id} not found" error
- [X] T031 [US2] Wire handle_mark_complete to menu option "5. Mark Complete/Incomplete" in run_cli() function in src/cli/cli.py
- [X] T032 [US2] Add docstring to handle_mark_complete() in src/cli/cli.py documenting toggle behavior

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - can create, view, and toggle completion status

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: Implement task detail modification functionality

**Independent Test**: Create 2 tasks using US1, update the title and description of one task by ID, view task list to confirm changes persisted with same task ID

### Implementation for User Story 3

- [X] T033 [US3] Implement handle_update_task(task_service: TaskService) function in src/cli/cli.py prompting for task ID, validating numeric format, verifying task exists via get_task_by_id(), prompting for new title and description, calling task_service.update_task(id, title, desc), displaying success or "Task with ID {id} not found" error
- [X] T034 [US3] Wire handle_update_task to menu option "3. Update Task" in run_cli() function in src/cli/cli.py
- [X] T035 [US3] Add docstring to handle_update_task() in src/cli/cli.py documenting update behavior and validation

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently - can create, view, toggle status, and update task details

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Implement task deletion functionality

**Independent Test**: Create 3 tasks using US1, delete one task by ID, view task list to verify only 2 tasks remain with original IDs (gaps in ID sequence are acceptable)

### Implementation for User Story 4

- [X] T036 [US4] Implement handle_delete_task(task_service: TaskService) function in src/cli/cli.py prompting for task ID, validating numeric format, calling task_service.delete_task(id), displaying "Task {id} deleted successfully" or "Task with ID {id} not found" error
- [X] T037 [US4] Wire handle_delete_task to menu option "4. Delete Task" in run_cli() function in src/cli/cli.py
- [X] T038 [US4] Add docstring to handle_delete_task() in src/cli/cli.py documenting deletion behavior

**Checkpoint**: All user stories should now be independently functional - full CRUD operations available

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories, final validation, and documentation

- [X] T039 [P] Review all code in src/ for PEP 8 compliance using manual inspection or `python -m black --check src/`
- [X] T040 [P] Verify all functions have Google-style docstrings with parameter and return value documentation
- [X] T041 [P] Check that no functions exceed 50 lines (constitution requirement)
- [X] T042 [P] Verify error messages match spec examples exactly: "Title cannot be empty", "Task with ID {id} not found", "Invalid ID format. Please enter a number.", "Invalid option. Please select a valid menu item."
- [X] T043 Update README.md with "Setup Instructions" section documenting Python 3.13+ requirement and running command: `uv run python src/main.py`
- [X] T044 Update README.md with "Usage Guide" section showing menu navigation and example commands for each operation
- [X] T045 Update README.md with "Demonstration Scenarios" section from constitution: add 3 tasks, list with status, update one, mark one complete, delete one, list remaining
- [X] T046 Execute manual test: Add task with empty title → verify "Title cannot be empty" error and re-prompt
- [X] T047 Execute manual test: Add task with 250-character title → verify graceful handling (accept or error)
- [X] T048 Execute manual test: Enter "abc" for task ID when marking complete → verify "Invalid ID format" error
- [X] T049 Execute manual test: Select invalid menu option "9" → verify "Invalid option" error and menu re-display
- [X] T050 Execute manual test: Exit application → verify clean termination without errors
- [X] T051 Execute manual test: Full lifecycle - add task, view, update, mark complete, delete → verify no crashes (SC-001)
- [X] T052 Execute manual test: Locate any feature in menu → verify under 10 seconds (SC-002)
- [X] T053 Execute manual test: Trigger error (invalid ID) → verify error message displays under 1 second and retry enabled (SC-003)
- [X] T054 Execute manual test: Add 3 tasks, mark one complete, view list → verify [ ] and [x] indicators consistent (SC-004)
- [X] T055 Execute manual test: Create 100 tasks, perform add/view/update/delete/mark operations → verify each under 500ms (SC-005)
- [X] T056 Code review validation: Verify modular structure (models/services/cli separation), PEP 8 compliance, and docstrings present (SC-006)
- [X] T057 Update spec.md status from "Draft" to "Implemented"
- [X] T058 Git commit all code with message: `feat: implement todo console app (AI-assisted)`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Uses US1 functionality for testing but is independently implementable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Uses US1 functionality for testing but is independently implementable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Uses US1 functionality for testing but is independently implementable

### Within Each User Story

- Tasks within US1 have dependencies: T021, T022 can run in parallel, then T023-T024 (both use helpers), then T025 (uses handlers), then T026-T028
- Tasks within US2, US3, US4 are mostly sequential but can integrate into existing CLI quickly

### Parallel Opportunities

- All Setup tasks T004-T007 (creating __init__.py files) marked [P] can run in parallel
- Within Foundational phase: T009-T012 (Task model) can run in parallel with T020 (docstrings added later)
- Within US1: T021, T022 can run in parallel (menu display and validation helper)
- All Polish phase code review tasks T039-T042 marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch these tasks together (if team capacity allows):
Task T021: Create display_menu() function in src/cli/cli.py
Task T022: Create validate_non_empty() helper function in src/cli/cli.py

# After T021, T022 complete, these can run in parallel:
Task T023: Implement handle_add_task() in src/cli/cli.py (uses T022)
Task T024: Implement handle_view_tasks() in src/cli/cli.py (uses T021)

# After T023, T024 complete:
Task T025: Implement run_cli() in src/cli/cli.py (uses T021, T023, T024)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T008)
2. Complete Phase 2: Foundational (T009-T020) - CRITICAL, blocks all stories
3. Complete Phase 3: User Story 1 (T021-T028)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - Can add tasks with title and description
   - Can view task list with status indicators
   - Empty list shows "No tasks found"
5. Demo/deliver MVP if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (T021-T028) → Test independently → **Deploy/Demo (MVP!)** 🎯
3. Add User Story 2 (T029-T032) → Test independently → Deploy/Demo
4. Add User Story 3 (T033-T035) → Test independently → Deploy/Demo
5. Add User Story 4 (T036-T038) → Test independently → Deploy/Demo
6. Complete Polish (T039-T058) → Final validation and documentation
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T020)
2. Once Foundational is done:
   - Developer A: User Story 1 (T021-T028)
   - Developer B: User Story 2 (T029-T032) - waits for T025 to exist, then adds handler
   - Developer C: User Story 3 (T033-T035) - waits for T025 to exist, then adds handler
   - Developer D: User Story 4 (T036-T038) - waits for T025 to exist, then adds handler
3. Stories complete and integrate independently

**Note**: In practice, US2-US4 will need US1's run_cli() function (T025) to wire their handlers, creating a soft dependency. However, their handler functions can be written and tested independently, then integrated into run_cli() once available.

---

## Notes

- [P] tasks = different files, no dependencies within phase
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Manual testing only per constitution - no pytest or automated test framework
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- File paths are explicit in every task description for clarity
- Task IDs (T001-T058) are sequential in execution order for easy tracking

---

**Total Tasks**: 58
**Setup**: 8 tasks
**Foundational**: 12 tasks (BLOCKING)
**User Story 1 (P1 - MVP)**: 8 tasks
**User Story 2 (P2)**: 4 tasks
**User Story 3 (P3)**: 3 tasks
**User Story 4 (P4)**: 3 tasks
**Polish & Validation**: 20 tasks

**Parallel Opportunities**: 11 tasks marked [P] can run in parallel with others in their phase
**Independent Stories**: All 4 user stories are independently testable after foundational phase
**Suggested MVP Scope**: Complete through Phase 3 (User Story 1) for minimal viable product
