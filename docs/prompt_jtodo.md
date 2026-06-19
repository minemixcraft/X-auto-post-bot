# Minimalist Markdown Journal & To-Do CLI Specification

Use this prompt with any advanced AI coding assistant to generate the zero-dependency Python tracker:

```markdown
Act as an expert Python software engineer. Create a beautiful, zero-dependency, interactive command-line interface (CLI) tool in Python named `jtodo.py` that acts as a "Minimalist Markdown Journal & To-Do CLI" and runs on Windows, macOS, and Linux.

### Key Requirements

1. **Zero-Dependency Architecture**:
   - Use ONLY Python standard library modules.
   - Do NOT use external terminal libraries like `curses`, `prompt_toolkit`, `click`, or `urwid`.
   - Implement custom raw keyboard event listeners for navigation using `msvcrt` on Windows, and `termios`/`tty` on Unix systems.

2. **File Formats**:
   - **`todo.md`**: Should parse list items with checkboxes formatted as `- [ ] <text>` (unchecked) or `- [x] <text>` (checked). It should support headings (`#`, `##`) and retain them during updates.
   - **`journal.md`**: Standard daily journal log. Appending a log entry should automatically place it under a `## 📅 YYYY-MM-DD` date heading, formatted as `- 🕒 HH:MM:SS | <entry_text>`.

3. **Interactive Terminal UI (TUI) Layout**:
   - **Header**: A clean ASCII-bordered header card containing the application title.
   - **Tasks Section**: Lists the items parsed from `todo.md`.
   - **Journal Section**: Displays the last 5 logged entries from `journal.md`.
   - **Actions Menu**: A list of selectable action items below the tasks:
     - `[ Add New Task ]`
     - `[ Log Journal Entry ]`
     - `[ Quit ]`
   - **Status Bar**: A section at the bottom for success/error informational messages.

4. **Double Cursor Navigation (Keyboard Selectable)**:
   - Use the **Up/Down arrow keys** (or **W/S**) to move a pointer cursor (`>`) vertically through the list.
   - The navigation cursor should flow smoothly from the task list items directly down into the Actions Menu items, and back up.
   - Pressing **Space** or **Enter**:
     - If highlighting a task item: Toggles its checkbox status between `[ ]` and `[x]`, updates the file, and logs the change to `journal.md`.
     - If highlighting `[ Add New Task ]`: Prompts the user to type a new task, appends it to `todo.md`, and logs it.
     - If highlighting `[ Log Journal Entry ]`: Prompts the user to type a log entry and appends it under the current day's header in `journal.md`.
     - If highlighting `[ Quit ]`: Exits the program.
   - Also allow quick direct shortcuts at any time (e.g. `A` for Add Task, `J` for Journal, `Q`/`Esc` to Quit).

5. **Aesthetics & Styling**:
   - Use clean, vibrant ANSI escape sequences for text colors (Cyan for cursors/headers, Green for checks/successes, Red for unchecked/warnings, Yellow for highlights, Gray for completed tasks and logs).
   - Use a subtle background highlight color (e.g. `\033[48;5;236m`) for the currently selected line.
   - Support ANSI escape modes on Windows by loading `ctypes.windll.kernel32.SetConsoleMode` to ensure color codes render correctly.
   - Clean Unicode icons or clean ASCII text elements (no heavy emojis if running in pure ASCII mode, keep text styling premium).
```
