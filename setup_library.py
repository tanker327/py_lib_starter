#!/usr/bin/env python3
"""
Setup script to create a new Python library project structure.
Usage: python setup_library.py my_library_name
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Dict, Any

# Template content for different file types
def get_templates(project_name: str) -> Dict[str, str]:
    """Return templates with project name already formatted."""
    return {
    "pyproject.toml": f'''[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{project_name}"
version = "0.1.0"
description = "Internal library for common functionality across projects"
requires-python = ">=3.8"
authors = [
    {{name = "Your Name", email = "your.email@company.com"}}
]
dependencies = []  # Keep empty by default, add specific dependencies as needed

[project.optional-dependencies]
# Development tools
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "isort>=5.0.0",
    "mypy>=0.950",
]
# Example optional feature groups (commented out by default)
# http = [
#     "requests>=2.28.0",
# ]
# yaml = [
#     "pyyaml>=6.0",
# ]
# data = [
#     "pandas>=1.3.0",
#     "numpy>=1.20.0",
# ]

[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v -s --tb=short"
''',

    "setup.cfg": f'''[metadata]
name = {project_name}
version = 0.1.0
description = Internal library for common functionality across projects
long_description = file: README.md
long_description_content_type = text/markdown

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.8
install_requires =
    # Add your package dependencies here

[options.packages.find]
where = src

[options.extras_require]
dev =
    pytest>=7.0.0
    black>=22.0.0
    isort>=5.0.0
    mypy>=0.950
# Example optional dependencies (commented out by default)
# http =
#     requests>=2.28.0
# yaml =
#     pyyaml>=6.0
# data =
#     pandas>=1.3.0
#     numpy>=1.20.0
''',

    "README.md": f'''# {project_name}

Internal library for common functionality across projects.

## Features

- Modular architecture with optional feature groups
- Type-hinted APIs
- Comprehensive test coverage
- Well-documented codebase

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

The library supports optional feature groups that can be installed based on your needs:

```bash
# Install specific feature group (uncomment in pyproject.toml first)
pip install -e ".[http]"     # HTTP related functionality
pip install -e ".[yaml]"     # YAML processing support
pip install -e ".[data]"     # Data processing tools

# Install multiple feature groups
pip install -e ".[dev,http,data]"
```

## Usage

Basic usage:
```python
from {project_name} import CoreFeature
from {project_name}.utils import setup_logging

# Set up logging
setup_logging()

# Initialize and use the core feature
feature = CoreFeature()
result = feature.process(data)
```

Error handling:
```python
from {project_name} import CoreFeature
from {project_name}.exceptions import ValidationError, ProcessingError

try:
    feature = CoreFeature()
    result = feature.process(data)
except ValidationError as e:
    print(f"Validation failed: {{e}}")
except ProcessingError as e:
    print(f"Processing failed: {{e}}")
```

## Development

1. Create and activate a virtual environment:
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
   # Run all tests
   pytest

   # Run tests with coverage
   pytest --cov={project_name}

   # Run specific test file
   pytest tests/test_core.py
   ```

4. Code formatting and linting:
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
│   ├── test_core.py        # Core tests
│   └── test_utils.py       # Utility tests
├── docs/
│   ├── api.md              # API documentation
│   ├── getting_started.md  # Getting started guide
│   └── examples.md         # Usage examples
├── pyproject.toml          # Project configuration
├── setup.cfg              # Setup configuration
├── README.md             # This file
└── CHANGELOG.md         # Version changelog
```

## Adding New Features

1. Create new modules in `src/{project_name}/`
2. Add corresponding test files in `tests/`
3. Update documentation in `docs/`
4. Add any new dependencies to `pyproject.toml`

## Dependencies

The package uses a modular dependency system:

- **Core**: No dependencies required
- **Development**: pytest, black, isort, mypy
- **Optional Groups** (uncomment in pyproject.toml as needed):
  - `http`: requests
  - `yaml`: pyyaml
  - `data`: pandas, numpy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Run tests and ensure they pass
5. Submit a pull request

## License

[Your License Here]

## Contact

[Your Contact Information]
'''
''',

    "CHANGELOG.md": '''# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - YYYY-MM-DD

### Added
- Initial release
- Basic project structure
- Core functionality
''',

    ".gitignore": '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# Distribution
dist/
build/
*.egg-info/
''',

    f"src/{project_name}/__init__.py": f'''"""
{project_name} - Internal library for common functionality across projects
"""

from .core import *
from .utils import *
from .exceptions import *

__version__ = "0.1.0"
''',

    f"src/{project_name}/core.py": '''"""Core functionality of the library."""
from typing import Any, Dict, List, Optional

class CoreFeature:
    """Main feature class of the library."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
    
    def process(self, data: List[Any]) -> List[Any]:
        """Process the input data using the core feature.
        
        Args:
            data: Input data to process
            
        Returns:
            Processed data
        """
        # Implementation here
        return data
''',

    f"src/{project_name}/utils.py": '''"""Utility functions for the library."""
from typing import Any, List
import logging

logger = logging.getLogger(__name__)

def setup_logging(level: str = "INFO") -> None:
    """Set up logging configuration.
    
    Args:
        level: Logging level (default: "INFO")
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def validate_input(data: List[Any]) -> bool:
    """Validate input data.
    
    Args:
        data: Input data to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Implementation here
    return True
''',

    f"src/{project_name}/exceptions.py": '''"""Custom exceptions for the library."""

class MyLibraryError(Exception):
    """Base exception for the library."""
    pass

class ValidationError(MyLibraryError):
    """Raised when input validation fails."""
    pass

class ProcessingError(MyLibraryError):
    """Raised when processing fails."""
    pass
''',

    "tests/__init__.py": '',

    "tests/test_core.py": f'''import pytest
from {project_name}.core import CoreFeature
from {project_name}.exceptions import ValidationError

def test_core_feature_initialization():
    feature = CoreFeature()
    assert feature.config == {{}}
    
    config = {{"param": "value"}}
    feature = CoreFeature(config)
    assert feature.config == config

def test_core_feature_process():
    feature = CoreFeature()
    test_data = [1, 2, 3]
    result = feature.process(test_data)
    assert isinstance(result, list)
''',

    "tests/test_utils.py": f'''import pytest
from {project_name}.utils import validate_input
from {project_name}.exceptions import ValidationError

def test_validate_input():
    valid_data = [1, 2, 3]
    assert validate_input(valid_data) is True
    
    with pytest.raises(ValidationError):
        validate_input(None)
''',

    "docs/api.md": f'''# API Documentation

## Core

### CoreFeature

Main feature class of the library.

#### Methods

- `__init__(config: Optional[Dict[str, Any]] = None)`
- `process(data: List[Any]) -> List[Any]`

## Utils

### Functions

- `setup_logging(level: str = "INFO") -> None`
- `validate_input(data: List[Any]) -> bool`

## Exceptions

- `MyLibraryError`
- `ValidationError`
- `ProcessingError`
''',

    "docs/getting_started.md": f'''# Getting Started

## Installation

1. Clone the repository
2. Install the package:
   ```bash
   pip install -e .
   ```

## Basic Usage

```python
from {project_name} import CoreFeature
from {project_name}.utils import setup_logging

# Set up logging
setup_logging()

# Initialize the core feature
feature = CoreFeature()

# Process some data
data = [1, 2, 3]
result = feature.process(data)
```
''',

    "docs/examples.md": f'''# Examples

## Basic Usage

```python
from {project_name} import CoreFeature

# Initialize the feature
feature = CoreFeature({{"param": "value"}})

# Process data
data = [1, 2, 3]
result = feature.process(data)
```

## Error Handling

```python
from {project_name} import CoreFeature
from {project_name}.exceptions import ValidationError, ProcessingError

try:
    feature = CoreFeature()
    result = feature.process(data)
except ValidationError as e:
    print(f"Validation failed: {{e}}")
except ProcessingError as e:
    print(f"Processing failed: {{e}}")
```
'''
    }

def create_directory_structure(base_path: Path, project_name: str) -> None:
    """Create the directory structure for the project."""
    # Create main project directory
    base_path.mkdir(exist_ok=True)
    
    # Create subdirectories
    dirs = [
        'src',
        f'src/{project_name}',
        'tests',
        'docs',
    ]
    
    for dir_path in dirs:
        (base_path / dir_path).mkdir(parents=True, exist_ok=True)

def create_file(path: Path, content: str) -> None:
    """Create a file with the given content."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def setup_project(project_name: str, base_path: str = None) -> None:
    """Set up the entire project structure."""
    if base_path is None:
        base_path = os.getcwd()
    
    base_path = Path(base_path) / project_name
    
    # Create directory structure
    create_directory_structure(base_path, project_name)
    
    # Get templates with project name formatted
    templates = get_templates(project_name)
    
    # Create files
    for filepath, content in templates.items():
        # Handle special cases for src and tests directories
        if filepath.startswith(f'src/{project_name}/'):
            actual_path = base_path / 'src' / project_name / filepath.split('/')[-1]
        elif filepath.startswith('src/'):
            actual_path = base_path / 'src' / filepath[4:]
        else:
            actual_path = base_path / filepath
        
        # Create parent directories if they don't exist
        actual_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create the file
        create_file(actual_path, content)

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description='Create a new Python library project structure'
    )
    parser.add_argument(
        'project_name',
        help='Name of the project (use underscores for spaces)'
    )
    parser.add_argument(
        '--path',
        help='Base path for project creation (default: current directory)',
        default=None
    )
    
    args = parser.parse_args()
    
    try:
        setup_project(args.project_name, args.path)
        print(f"Successfully created project structure for {args.project_name}")
    except Exception as e:
        print(f"Error creating project structure: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()