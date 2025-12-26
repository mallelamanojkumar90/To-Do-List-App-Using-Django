# UV Package Manager - Quick Reference

This project uses **uv**, an ultra-fast Python package installer and resolver, instead of pip.

## Why UV?

- ⚡ **10-100x faster** than pip
- 🔒 **Better dependency resolution**
- 🎯 **Drop-in replacement** for pip
- 📦 **Built-in virtual environment management**

## Installation

### Windows (PowerShell)

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Common Commands

### Create Virtual Environment

```bash
uv venv
```

This creates a `.venv` directory in your project.

### Activate Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
# Install from requirements.txt
uv pip install -r requirements.txt

# Install a single package
uv pip install django

# Install with specific version
uv pip install django==5.0
```

### List Installed Packages

```bash
uv pip list
```

### Freeze Dependencies

```bash
uv pip freeze > requirements.txt
```

### Uninstall Package

```bash
uv pip uninstall package-name
```

## Project Setup with UV

1. **Navigate to project directory:**

   ```bash
   cd "c:\Manojkumar\development\To-Do List App Using Django"
   ```

2. **Create virtual environment:**

   ```bash
   uv venv
   ```

3. **Activate virtual environment:**

   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. **Install dependencies:**

   ```bash
   uv pip install -r requirements.txt
   ```

5. **Run Django commands as usual:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Comparison: pip vs uv

| Command           | pip                               | uv                                   |
| ----------------- | --------------------------------- | ------------------------------------ |
| Create venv       | `python -m venv venv`             | `uv venv`                            |
| Install package   | `pip install django`              | `uv pip install django`              |
| Install from file | `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| List packages     | `pip list`                        | `uv pip list`                        |
| Freeze packages   | `pip freeze`                      | `uv pip freeze`                      |

## Benefits for This Project

1. **Faster installation**: Dependencies install in seconds instead of minutes
2. **Better caching**: Packages are cached globally and reused across projects
3. **Reliable resolution**: Better at resolving dependency conflicts
4. **Same workflow**: All pip commands work with `uv pip`

## Troubleshooting

### UV not found after installation

- **Windows**: Restart PowerShell or add to PATH manually
- **macOS/Linux**: Run `source ~/.bashrc` or `source ~/.zshrc`

### Permission errors

- Run terminal as administrator (Windows)
- Use `sudo` for installation (macOS/Linux)

### Virtual environment issues

- Delete `.venv` folder and recreate: `uv venv`
- Ensure you're in the correct directory

## Additional Resources

- UV Documentation: https://github.com/astral-sh/uv
- UV Installation Guide: https://astral.sh/uv
- UV vs pip Benchmark: https://github.com/astral-sh/uv#benchmarks

## Note

UV is a drop-in replacement for pip, so all your existing pip knowledge and workflows still apply. Just prefix commands with `uv` and enjoy the speed boost! 🚀
