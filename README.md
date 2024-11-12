# Python Library Setup Script

A command-line tool to automatically generate a standardized Python library project structure. This script creates a complete project scaffold with all necessary files, configurations, and documentation for creating internal Python libraries.

## Features

- 📁 Creates standardized project structure
- ⚙️ Generates all necessary configuration files
- 📝 Sets up documentation templates
- 🧪 Includes test infrastructure
- 🐍 Follows Python best practices
- 📦 Modern packaging setup with `pyproject.toml`

## Project Structure Generated

```
my_library/
├── src/
│   └── my_library/
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
├── README.md             # Project README
├── CHANGELOG.md         # Version changelog
└── .gitignore          # Git ignore rules
```

## Installation

1. Download the script:
```bash
curl -O https://github.com/tanker327/py_lib_starter/setup_library.py
# or wget https://github.com/tanker327/py_lib_starter/setup_library.py
```

2. Make it executable (Unix/Linux):
```bash
chmod +x setup_library.py
```

## Usage

### Basic Usage

```bash
python setup_library.py my_library_name
```

### Specify Custom Path

```bash
python setup_library.py my_library_name --path /path/to/projects
```

## Examples

### Example 1: Creating a Data Processing Library

```bash
python setup_library.py data_processing_lib
cd data_processing_lib
```

This creates a library structure ready for implementing data processing functionality:

```python
# src/data_processing_lib/core.py
from typing import List, Any

class DataProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return data

# Usage
from data_processing_lib import DataProcessor
processor = DataProcessor()
result = processor.process([1, 2, 3])
```

### Example 2: Creating a Machine Learning Utils Library

```bash
python setup_library.py ml_utils --path ~/projects
cd ~/projects/ml_utils
```

The generated structure is ready for ML utility functions:

```python
# src/ml_utils/core.py
import numpy as np

class ModelEvaluator:
    def calculate_metrics(self, y_true, y_pred):
        return {
            "accuracy": np.mean(y_true == y_pred),
            "samples": len(y_true)
        }

# Usage
from ml_utils import ModelEvaluator
evaluator = ModelEvaluator()
metrics = evaluator.calculate_metrics(y_true, y_pred)
```

## Post-Generation Steps

1. Initialize Git repository:
```bash
git init
```

2. Install the package in development mode:
```bash
pip install -e ".[dev]"
```

3. Run the tests:
```bash
pytest
```

## Configuration

The generated project includes several pre-configured tools:

- **Black**: Code formatting
- **isort**: Import sorting
- **mypy**: Static type checking
- **pytest**: Testing framework

### Development Dependencies

The project is set up with development dependencies in `pyproject.toml`:

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "isort>=5.0.0",
    "mypy>=0.950",
]
```

## Best Practices

The generated project structure follows these best practices:

1. **Source Layout**: Uses the `src/` layout for better packaging
2. **Type Hints**: All template code includes type hints
3. **Documentation**: Includes templates for API docs and examples
4. **Testing**: Ready-to-use test infrastructure
5. **Logging**: Built-in logging setup
6. **Exception Handling**: Custom exception hierarchy

## License

This script is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Common Issues and Solutions

### Issue: Permission Denied

```bash
# Solution:
chmod +x setup_library.py
```

### Issue: Import Errors After Installation

```bash
# Solution:
pip install -e ".[dev]"
```

### Issue: Tests Not Found

```bash
# Solution:
python -m pytest
```

## Contact

For questions and support, please raise an issue in the GitHub repository.
