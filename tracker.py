# tracker.py
# Beautiful, zero-dependency Markdown Journal & To-Do CLI in Python
# Supports keyboard arrow navigation to check/uncheck items

import os
import sys
import re
from datetime import datetime

# Windows console ANSI support configuration
if sys.platform == "win32":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ANSI Colors
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_CYAN = "\033[36m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_RED = "\033[31m"
C_MAGENTA = "\033[35m"
C_BLUE = "\033[34m"
C_GRAY = "\033[90m"
C_BG_DARK = "\033[48;5;236m"

# Files
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TODO_FILE = os.path.join(SCRIPT_DIR, "docs", "todo.md")
JOURNAL_FILE = os.path.join(SCRIPT_DIR, "docs", "journal.md")

# Cross-platform single key reader
try:
    import msvcrt
    def read_key():
        ch = msvcrt.getch()
        if ch in (b'\x00', b'\xe0'):
            ch2 = msvcrt.getch()
            if ch2 == b'H': return 'up'
            if ch2 == b'P': return 'down'
            return None
        if ch in (b'\r', b'\n'):
            return 'enter'
        if ch == b' ':
            return 'space'
        if ch == b'\x1b':
            return 'esc'
        try:
            return ch.decode('utf-8').lower()
        except:
            return None
except ImportError:
    # Unix fallback (macOS/Linux)
    import tty
    import termios
    def read_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                # Check for arrow keys
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A': return 'up'
                    if ch3 == 'B': return 'down'
                return 'esc'
            if ch in ('\r', '\n'):
                return 'enter'
            if ch == ' ':
                return 'space'
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def ensure_files_exist():
    # Pre-populate todo.md with the X-Bot checklist if it doesn't exist
    if not os.path.exists(TODO_FILE):
        default_todo = """# [TODO] X-Bot Task Checklist

## GreenHaven (GH) - [STATUS] Blocked (Suspended)
- [ ] [ERR] One or more client apps suspended. [FIX] Delete suspended app in X Developer Portal first.
- [ ] GreenHaven: Create a new App in the X Developer Portal
- [ ] GreenHaven: Configure App Permissions to 'Read and Write'
- [ ] GreenHaven: Generate new Consumer Keys and Access Tokens
- [ ] GreenHaven: Update config/credentials.env with new GH_ keys
- [ ] GreenHaven: Run upload_secrets.ps1 to upload keys to GitHub

## Moonchill (MC) - [STATUS] Done
- [x] Moonchill: Verify and generate unique keys in the X Developer Portal
- [x] Moonchill: Update config/credentials.env with new MC_ keys
- [x] Moonchill: Run upload_secrets.ps1 to upload keys to GitHub

## Stray Cat 1 (SC1) - [STATUS] Action Required (402 Payment Required)
- [ ] [ERR] HTTPException 402 Payment Required. [FIX] Purchase API credits on X Developer Console.
- [x] Stray Cat 1: Add keys to config/credentials.env under SC1_ keys
- [x] Stray Cat 1: Run upload_secrets.ps1 to upload keys to GitHub

## Stray Cat 2 (SC2) - [STATUS] Action Required (402 Payment Required)
- [ ] [ERR] HTTPException 402 Payment Required. [FIX] Purchase API credits on X Developer Console.
- [x] Stray Cat 2: Verify App permissions are set to 'Read and Write'
- [x] Stray Cat 2: Regenerate keys/tokens in X Developer Portal to resolve 401
- [x] Stray Cat 2: Add keys to config/credentials.env under SC2_ keys
- [x] Stray Cat 2: Run upload_secrets.ps1 to upload keys to GitHub
"""
        with open(TODO_FILE, "w", encoding="utf-8") as f:
            f.write(default_todo)

    # Pre-populate journal.md if it doesn't exist
    if not os.path.exists(JOURNAL_FILE):
        default_journal = f"""# X-Bot Operations Journal

## Date: {datetime.now().strftime('%Y-%m-%d')}
- {datetime.now().strftime('%H:%M:%S')} | Created and initialized X-Bot Task & Journal CLI.
"""
        with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
            f.write(default_journal)

def load_todos():
    todos = []
    if not os.path.exists(TODO_FILE):
        return todos, []
        
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        match = re.match(r'^\s*-\s*\[([ xX])\]\s*(.*)$', line)
        if match:
            checked = match.group(1).lower() == 'x'
            text = match.group(2).strip()
            todos.append({
                'line_idx': idx,
                'checked': checked,
                'text': text
            })
    return todos, lines

def save_todos(lines):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

def toggle_todo(item_num):
    todos, lines = load_todos()
    if item_num < 1 or item_num > len(todos):
        return False, "Invalid task number."
        
    todo = todos[item_num - 1]
    line_idx = todo['line_idx']
    new_status = ' ' if todo['checked'] else 'x'
    
    # Replace the exact [ ] or [x] in the original line
    lines[line_idx] = re.sub(r'\[([ xX])\]', f'[{new_status}]', lines[line_idx], count=1)
    save_todos(lines)
    
    status_text = "unchecked" if todo['checked'] else "checked"
    log_journal(f"Toggled task: '{todo['text']}' to {status_text}")
    return True, f"Toggled task status!"

def add_todo(task_text):
    if not task_text.strip():
        return False, "Task text cannot be empty."
        
    ensure_files_exist()
    with open(TODO_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n- [ ] {task_text.strip()}")
        
    log_journal(f"Added new task: '{task_text.strip()}'")
    return True, "Task added successfully!"

def log_journal(entry_text):
    if not entry_text.strip():
        return False, "Journal entry cannot be empty."
        
    ensure_files_exist()
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')
    
    with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    date_header = f"## 📅 {date_str}"
    entry_line = f"- 🕒 {time_str} | {entry_text.strip()}\n"
    
    if date_header in content:
        # Insert entry directly after the date header
        pattern = re.escape(date_header) + r'\s*\n'
        new_content = re.sub(pattern, f"{date_header}\n{entry_line}", content, count=1)
    else:
        # Append new date header and entry at the end of the file
        new_content = content.rstrip() + f"\n\n{date_header}\n{entry_line}"
        
    with open(JOURNAL_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    return True, "Journal entry added!"

def get_latest_journal_entries(limit=5):
    if not os.path.exists(JOURNAL_FILE):
        return []
    with open(JOURNAL_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    entries = []
    for line in reversed(lines):
        if line.strip().startswith("- 🕒"):
            entries.append(line.strip())
            if len(entries) >= limit:
                break
    return entries

def render_ui(selected_idx, message="", is_error=False):
    clear_screen()
    ensure_files_exist()
    todos, lines = load_todos()
    
    # 1. Print Header (ASCII Border style)
    print(f" {C_CYAN}╔══════════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f" {C_CYAN}║{C_RESET}               {C_BOLD}{C_GREEN}d[o_0]b X-BOT OPERATIONS TRACKER & JOURNAL CLI{C_RESET}               {C_CYAN}║{C_RESET}")
    print(f" {C_CYAN}╚══════════════════════════════════════════════════════════════════════╝{C_RESET}")
    
    # 2. Print To-Do List
    print(f"\n [TASKS] Active Task List (todo.md) - Use Up/Down to select, Space/Enter to toggle:")
    print(f" ========================================================================")
    
    if not todos:
        print(f"   No tasks found in todo.md.")
    else:
        # Map line index to index in the todos list
        line_to_todo_idx = {}
        for t_idx, todo in enumerate(todos):
            line_to_todo_idx[todo['line_idx']] = t_idx
            
        for l_idx, line in enumerate(lines):
            line_stripped = line.strip()
            
            # Check if this line is an actual task
            if l_idx in line_to_todo_idx:
                t_idx = line_to_todo_idx[l_idx]
                todo = todos[t_idx]
                is_selected = (t_idx == selected_idx)
                cursor = f"{C_CYAN}> {C_RESET}" if is_selected else "  "
                
                if todo['checked']:
                    checkbox = f"{C_GREEN}[x]{C_RESET}"
                    text_style = C_GRAY
                else:
                    checkbox = f"{C_RED}[ ]{C_RESET}"
                    text_style = C_BOLD + (C_CYAN if is_selected else C_RESET)
                
                # Strip emojis from the line and replace tags
                text_content = todo['text']
                text_content = re.sub(r'[\u2000-\u32FF\ud83c-\ud83d\udb40-\udb4f\ufe00-\ufe0f]', '', text_content)
                text_content = re.sub(r'(?i)\[ERR\]', f"{C_BOLD}{C_RED}[ERR]{C_RESET}{text_style}", text_content)
                text_content = re.sub(r'(?i)\[FIX\]', f"{C_BOLD}{C_YELLOW}[FIX]{C_RESET}{text_style}", text_content)
                text_content = re.sub(r'(?i)\[STATUS\]', f"{C_BOLD}{C_BLUE}[STATUS]{C_RESET}{text_style}", text_content)
                
                line_str = f" {cursor}{checkbox} {text_style}{text_content}{C_RESET}"
                if is_selected:
                    print(f"{C_BG_DARK}{line_str}{C_RESET}")
                else:
                    print(line_str)
                    
            # Check if it is a section heading (starts with ##)
            elif line_stripped.startswith("##"):
                heading_text = line_stripped[2:].strip()
                heading_text = re.sub(r'[\u2000-\u32FF\ud83c-\ud83d\udb40-\udb4f\ufe00-\ufe0f]', '', heading_text)
                heading_text = re.sub(r'(?i)\[ERR\]', f"{C_BOLD}{C_RED}[ERR]{C_RESET}{C_BOLD}{C_CYAN}", heading_text)
                heading_text = re.sub(r'(?i)\[FIX\]', f"{C_BOLD}{C_YELLOW}[FIX]{C_RESET}{C_BOLD}{C_CYAN}", heading_text)
                heading_text = re.sub(r'(?i)\[STATUS\]', f"{C_BOLD}{C_BLUE}[STATUS]{C_RESET}{C_BOLD}{C_CYAN}", heading_text)
                print(f"\n {C_BOLD}{C_CYAN}{heading_text}{C_RESET}")
                
            # Check if it is a root heading (starts with #)
            elif line_stripped.startswith("#"):
                title_text = line_stripped[1:].strip()
                title_text = re.sub(r'[\u2000-\u32FF\ud83c-\ud83d\udb40-\udb4f\ufe00-\ufe0f]', '', title_text)
                print(f" {C_BOLD}{C_GREEN}{title_text}{C_RESET}")
            
    # 3. Print Latest Journal Entries
    print(f"\n [JOURNAL] Recent Journal Activity (journal.md):")
    print(f" ========================================================================")
    
    journal_entries = get_latest_journal_entries()
    if not journal_entries:
        print(f"   No journal entries recorded yet.")
    else:
        for entry in journal_entries:
            # Strip emojis from the entry line
            entry_clean = re.sub(r'[\u2000-\u32FF\ud83c-\ud83d\udb40-\udb4f\ufe00-\ufe0f]', '', entry)
            match = re.match(r'^-\s*([\d:]+)\s*\|\s*(.*)$', entry_clean)
            if match:
                time_part = match.group(1)
                text_part = match.group(2)
                print(f"   {C_BLUE}{time_part}{C_RESET} | {C_GRAY}{text_part}{C_RESET}")
            else:
                print(f"   {C_GRAY}{entry_clean}{C_RESET}")
                
    # 4. Print Action Menu (Cursor Selectable)
    print(f"\n [ACTIONS] Menu (Use Up/Down to select, Enter/Space to execute):")
    print(f" ========================================================================")
    
    actions = [
        ("Add New Task", len(todos)),
        ("Log Journal Entry", len(todos) + 1),
        ("Quit", len(todos) + 2)
    ]
    
    for label, idx in actions:
        is_selected = (selected_idx == idx)
        cursor = f"{C_CYAN}> {C_RESET}" if is_selected else "  "
        if is_selected:
            option_str = f" {cursor}{C_BOLD}{C_CYAN}[ {label} ]{C_RESET}"
            print(f"{C_BG_DARK}{option_str}{C_RESET}")
        else:
            print(f" {cursor}{C_GRAY}[ {label} ]{C_RESET}")
            
    # 5. Print CLI Controls
    print(f"\n [CONTROLS] Keyboard Controls:")
    print(f"   Up/Down (or W/S) : Navigate Tasks & Menu Options")
    print(f"   Space/Enter      : Toggle Task / Execute Menu Option")
    print(f"   A / J / Q / Esc  : Direct Key Shortcuts")
    print(f" ========================================================================")
    
    # 6. Print Status Messages
    if message:
        color = C_RED if is_error else C_GREEN
        print(f" [INFO] {color}{message}{C_RESET}")

def main():
    # Configure UTF-8 stdout encoding for Windows
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    selected_idx = 0
    message = ""
    is_error = False
    
    while True:
        todos, _ = load_todos()
        
        # Ensure selected index stays in bounds
        total_items = len(todos) + 3
        if total_items > 0:
            if selected_idx >= total_items:
                selected_idx = total_items - 1
            if selected_idx < 0:
                selected_idx = 0
                
        render_ui(selected_idx, message, is_error)
        message = ""
        is_error = False
        
        key = read_key()
        if key is None:
            continue
            
        if key == 'up' or key == 'w' or key == 'k':
            if selected_idx > 0:
                selected_idx -= 1
        elif key == 'down' or key == 's' or key == 'j':
            if selected_idx < len(todos) + 2:
                selected_idx += 1
        elif key == 'space' or key == 'enter':
            if selected_idx < len(todos):
                success, msg = toggle_todo(selected_idx + 1)
                message = msg
                is_error = not success
            elif selected_idx == len(todos):
                print(f"\n Enter new task description: ", end="")
                try:
                    task_text = input().strip()
                    if task_text:
                        success, msg = add_todo(task_text)
                        message = msg
                        is_error = not success
                except (KeyboardInterrupt, EOFError):
                    pass
            elif selected_idx == len(todos) + 1:
                print(f"\n Enter journal entry: ", end="")
                try:
                    entry_text = input().strip()
                    if entry_text:
                        success, msg = log_journal(entry_text)
                        message = msg
                        is_error = not success
                except (KeyboardInterrupt, EOFError):
                    pass
            elif selected_idx == len(todos) + 2:
                print(f"\n Goodbye!")
                break
        elif key == 'a':
            print(f"\n Enter new task description: ", end="")
            try:
                task_text = input().strip()
                if task_text:
                    success, msg = add_todo(task_text)
                    message = msg
                    is_error = not success
            except (KeyboardInterrupt, EOFError):
                pass
        elif key == 'j':
            print(f"\n Enter journal entry: ", end="")
            try:
                entry_text = input().strip()
                if entry_text:
                    success, msg = log_journal(entry_text)
                    message = msg
                    is_error = not success
            except (KeyboardInterrupt, EOFError):
                pass
        elif key == 'q' or key == 'esc':
            print(f"\n Goodbye!")
            break

if __name__ == "__main__":
    main()
