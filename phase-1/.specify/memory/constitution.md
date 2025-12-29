<!--
Sync Impact Report:
Version change: Initial → 1.0.0
Modified principles: N/A (initial creation)
Added sections: All sections (Preamble, Development Principles, Code Standards, Project Structure, AI Usage, Testing & Quality, Amendments)
Removed sections: None
Templates requiring updates:
  ✅ plan-template.md - reviewed (Constitution Check section references this file)
  ✅ spec-template.md - reviewed (requirements align with constitution principles)
  ✅ tasks-template.md - reviewed (task structure supports constitution principles)
Follow-up TODOs: None
-->

# The Evolution of Todo - Phase I Constitution

## Preamble

This constitution establishes the foundational principles, development practices, and quality standards for "The Evolution of Todo - Phase I: Todo In-Memory Python Console App" hackathon project. The purpose is to ensure consistent, high-quality delivery through spec-driven development (SDD), clean code principles, and ethical AI-assisted development using Qwen.

**Project Goals:**
- Build a functional command-line todo application with in-memory storage
- Demonstrate spec-driven development methodology using Spec-Kit Plus
- Implement five core features: Add Task, Delete Task, Update Task, View Task List, Mark as Complete
- Maintain clean, maintainable Python code following industry best practices
- Leverage AI assistance (Qwen) responsibly for code generation

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)

All development MUST follow the spec-first approach:
- Specifications are written BEFORE any implementation begins
- Every feature requires a complete spec.md in the specs history folder before coding
- Specs define user stories, acceptance criteria, and success metrics
- Implementation strictly follows approved specifications
- Deviations from spec require spec amendments and approval

**Rationale**: Spec-driven development prevents scope creep, ensures clear requirements understanding, and provides traceability from requirements to implementation.

### II. Spec-Kit Plus Integration

All specification management MUST use Spec-Kit Plus tools and conventions:
- Specifications stored in `specs/` directory with proper structure
- History maintained in `history/prompts/` for all spec iterations
- ADRs (Architecture Decision Records) created for significant decisions
- PHRs (Prompt History Records) generated for all user interactions
- Templates followed from `.specify/templates/` for consistency

**Rationale**: Spec-Kit Plus provides structured governance, traceability, and consistency across the development lifecycle.

### III. Clean Code Standards (MANDATORY)

All Python code MUST adhere to:
- PEP 8 style guide for Python code formatting
- Modular design with single-responsibility principle
- Clear, descriptive naming for variables, functions, and classes
- Comprehensive error handling with specific exception types
- No external dependencies beyond standard library unless justified
- Docstrings for all public functions and classes

**Rationale**: Clean code ensures maintainability, readability, and reduces technical debt, making the codebase accessible for review and future enhancements.

### IV. Minimal Viable Implementation

Implementation MUST prioritize simplicity:
- Build only the five specified core features
- Use in-memory storage (lists/dictionaries) - no database
- Console-only interface - no GUI or web interface
- Standard library preferred over external packages
- No premature optimization or over-engineering

**Rationale**: For hackathon delivery, simplicity ensures completion within time constraints while maintaining quality and demonstrating core competencies.

### V. AI-Assisted Development with Qwen

Qwen AI assistance MUST be used ethically and responsibly:
- Generate code from approved specifications only
- Every AI-generated code block MUST be reviewed and understood
- No blind copying of generated code into the project
- Prompt Qwen with clear, spec-based requirements
- Document AI-generated sections in commit messages
- Human developer remains accountable for all code quality

**Rationale**: AI tools accelerate development but require human oversight to ensure correctness, security, and alignment with project standards.

### VI. Testing and Quality Validation

Quality assurance MUST include:
- Manual testing of all five features against acceptance criteria
- Validation that implementation matches specification
- Testing edge cases (empty lists, invalid IDs, missing data)
- Demonstration scenarios documented and executable
- Code review against this constitution before finalization

**Rationale**: Without automated tests, manual validation ensures features work as specified and meet quality standards before delivery.

## Code Standards

### Python Code Quality

**Formatting**:
- 4-space indentation (no tabs)
- Maximum line length of 88 characters (Black formatter compatible)
- UTF-8 encoding for all source files

**Structure**:
- Modular design: separate files for models, services, CLI interface
- Class-based task management with clear interfaces
- Function length: maximum 50 lines, ideally under 20
- Avoid global state; prefer function parameters and return values

**Error Handling**:
- Use specific exceptions (ValueError, KeyError, etc.)
- Never use bare `except:` clauses
- Provide meaningful error messages to users
- Handle edge cases explicitly (empty task lists, invalid IDs)

**Documentation**:
- Docstrings for all public functions (Google style)
- Inline comments only for non-obvious logic
- README.md with setup, usage, and examples

**Dependencies**:
- Prefer Python standard library
- If external package needed, justify in spec and document in requirements.txt
- Pin versions for reproducibility

## Project Structure

### Repository Layout

```
phase-1/
├── .specify/
│   ├── memory/
│   │   └── constitution.md          # This file
│   └── templates/                    # Spec-Kit Plus templates
├── specs/
│   └── <feature>/
│       ├── spec.md                   # Feature specifications
│       ├── plan.md                   # Implementation plans
│       └── tasks.md                  # Task breakdowns
├── history/
│   ├── prompts/                      # PHRs organized by stage
│   └── adr/                          # Architecture Decision Records
├── src/
│   ├── models/
│   │   └── task.py                   # Task data model
│   ├── services/
│   │   └── task_service.py           # Business logic
│   ├── cli/
│   │   └── cli.py                    # Command-line interface
│   └── main.py                       # Application entry point
├── README.md                         # Project documentation
└── pyproject.toml                    # UV project configuration
```

**Rules**:
- All source code in `src/` directory
- Specs and planning documents in `specs/` and `history/`
- No source code files outside of `src/`
- Entry point is `src/main.py` runnable via `uv run python src/main.py`

## AI Usage Guidelines

### Ethical Qwen Integration

**Prompt Guidelines**:
- Include relevant spec excerpts in prompts
- Request specific functions or modules, not entire applications
- Ask for explanations alongside code generation
- Request multiple approaches when architecture decisions needed

**Review Process**:
1. Generate code via Qwen based on approved spec
2. Read and understand every generated line
3. Verify alignment with spec and constitution
4. Test generated code manually
5. Refactor for clarity and standards compliance if needed
6. Commit with message indicating AI assistance: `feat: implement add task (AI-assisted)`

**Prohibited Practices**:
- Do NOT paste code without reading and understanding
- Do NOT use AI to bypass spec-driven process
- Do NOT accept generated code that violates PEP 8 or clean code principles
- Do NOT use AI for writing specs (specs require human judgment and domain knowledge)

**Accountability**:
- Developer is fully responsible for all committed code
- AI is a tool, not a decision-maker
- Quality, security, and correctness remain human responsibilities

## Testing and Quality

### Manual Testing Requirements

Since automated tests are not required for Phase I, manual validation MUST cover:

**Per-Feature Testing**:
- Test happy path scenarios from spec acceptance criteria
- Test edge cases: empty lists, invalid inputs, missing fields
- Verify error messages are clear and helpful
- Confirm data persistence within session (in-memory)

**Integration Testing**:
- Run all five features in sequence in a single session
- Verify state consistency across operations
- Test task ID management (uniqueness, validity)

**Demonstration Scenarios**:
Document and test these scenarios in README.md:
1. Add three tasks with different titles and descriptions
2. List all tasks showing status indicators
3. Update one task's details
4. Mark one task as complete
5. Delete one task by ID
6. List remaining tasks verifying changes

### Spec Validation

Before marking implementation complete:
- Checklist: All acceptance criteria from spec.md satisfied
- Cross-reference: Each feature in spec has corresponding implementation
- Code review: All code adheres to constitution standards
- Documentation: README includes setup and demo instructions

## Governance

**Authority**: This constitution supersedes all other project practices and guidelines. When conflicts arise, constitution principles take precedence.

**Compliance**: All code reviews, spec approvals, and commits MUST verify compliance with this constitution. Non-compliant work MUST be rejected and remediated.

**Complexity Justification**: Any deviation from simplicity principles (e.g., adding external dependencies, creating additional features) MUST be documented in spec with explicit justification and approval.

**Amendment Process**:
1. Identify need for constitution change (new principle, modified standard, governance update)
2. Propose amendment in writing with rationale and impact analysis
3. Document decision in ADR (Architecture Decision Record)
4. Update constitution version (see versioning below)
5. Propagate changes to dependent templates (plan, spec, tasks)
6. Commit with message: `docs: amend constitution to v[X.Y.Z] ([brief change])`

**Versioning**:
- MAJOR: Backward-incompatible governance changes (e.g., removing core principles)
- MINOR: New principles or sections added (e.g., adding new code standards)
- PATCH: Clarifications, typo fixes, wording improvements (no semantic change)

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
