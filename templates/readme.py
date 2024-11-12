"""README.md template generator."""

def get_minimal_readme(project_name: str) -> str:
    """Generate a minimal README template."""
    return f'''# {project_name}

A Python library for [brief description].

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from {project_name} import CoreFeature

feature = CoreFeature()
result = feature.process(data)
```

## Development

1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

3. Run tests:
   ```bash
   pytest
   ```
'''

def get_full_readme(project_name: str) -> str:
    """Generate a comprehensive README template."""
    return f'''# {project_name}

[Brief description of your library]

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

### Basic Installation

```bash
pip install -e .
```

### Development Installation

Install with development tools (pytest, black, isort, mypy):
```bash
pip install -e ".[dev]"
```

### Optional Features

The library supports optional feature groups:

```bash
# Install specific feature groups (uncomment in pyproject.toml first)
pip install -e ".[http]"     # HTTP related functionality
pip install -e ".[yaml]"     # YAML processing support
pip install -e ".[data]"     # Data processing tools

# Install multiple feature groups
pip install -e ".[dev,http,data]"
```

## Quick Start

```python
from {project_name} import CoreFeature
from {project_name}.utils import setup_logging

# Set up logging
setup_logging()

# Initialize and use the core feature
feature = CoreFeature()
result = feature.process(data)
```

## Development

### Setup Development Environment

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov={project_name}

# Run specific test file
pytest tests/test_core.py
```

### Code Quality

```bash
# Format code
black .

# Sort imports
isort .

# Type checking
mypy src
```

## Project Structure

```
{project_name}/
├── src/
│   └── {project_name}/
│       ├── __init__.py      # Package initialization
│       ├── core.py          # Core functionality
│       ├── utils.py         # Utility functions
│       └── exceptions.py    # Custom exceptions
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/
│   ├── api.md
│   ├── getting_started.md
│   └── examples.md
└── [configuration files]
```

## Documentation

- [API Documentation](docs/api.md)
- [Getting Started](docs/getting_started.md)
- [Examples](docs/examples.md)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Run tests and ensure they pass
5. Submit a pull request

## License

[Your chosen license]

## Contact

[Your contact information]
'''

def get_readme_template(project_name: str, full: bool = False) -> str:
    """
    Get the README.md template.
    
    Args:
        project_name: Name of the project
        full: Whether to generate a full or minimal README
        
    Returns:
        README content
    """
    if full:
        return get_full_readme(project_name)
    return get_minimal_readme(project_name)