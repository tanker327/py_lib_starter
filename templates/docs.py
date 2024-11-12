"""Documentation templates."""

from typing import Dict

def get_doc_templates(project_name: str) -> Dict[str, str]:
    """
    Get the documentation templates.
    
    Args:
        project_name: Name of the project
        
    Returns:
        Dictionary of filename to content mappings
    """
    return {
        "api.md": f'''# API Documentation

## Core

### CoreFeature

Main feature class of the library.

#### Methods

- `__init__(config: Optional[Dict[str, Any]] = None)`
  - Initialize the feature with optional configuration
  - Args:
    - config: Configuration dictionary

- `process(data: List[Any]) -> List[Any]`
  - Process the input data
  - Args:
    - data: Input data to process
  - Returns:
    - Processed data

## Utils

### Functions

- `setup_logging(level: str = "INFO") -> None`
  - Set up logging configuration
  - Args:
    - level: Logging level (default: "INFO")

- `validate_input(data: List[Any]) -> bool`
  - Validate input data
  - Args:
    - data: Input data to validate
  - Returns:
    - True if valid
  - Raises:
    - ValidationError if invalid

## Exceptions

- `LibraryError`: Base exception for the library
- `ValidationError`: Raised when input validation fails
- `ProcessingError`: Raised when processing fails
''',

        "getting_started.md": f'''# Getting Started

## Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

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

## Development Setup

1. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run tests:
   ```bash
   pytest
   ```

3. Format code:
   ```bash
   black .
   isort .
   ```

4. Type checking:
   ```bash
   mypy src
   ```
''',

        "examples.md": f'''# Examples

## Basic Usage

```python
from {project_name} import CoreFeature

# Initialize with default configuration
feature = CoreFeature()
result = feature.process([1, 2, 3])

# Initialize with custom configuration
feature = CoreFeature({{"param": "value"}})
result = feature.process([4, 5, 6])
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

## Logging Setup

```python
from {project_name}.utils import setup_logging

# Set up with default level (INFO)
setup_logging()

# Set up with custom level
setup_logging(level="DEBUG")
```
'''
    }