"""README.md template generator."""

from typing import Dict, Any

def get_readme_template(
    project_name: str,
    config: Dict[str, Any] = None
) -> str:
    """Generate README.md content."""
    if config is None:
        config = {}
    
    # Get user information
    metadata = config.get('metadata', {})
    author = metadata.get('author', 'Your Name')
    github_username = metadata.get('github_username', 'your-github-username')
    
    return f'''# {project_name}

[Brief description of your project]

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

You can install this package using either pip or conda.

### Option 1: Installation with pip

1. **Development Installation (Recommended during development)**:
   ```bash
   # Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   
   # Install in editable mode with development dependencies
   pip install -e ".[dev]"
   ```

2. **Build and Install from Source**:
   ```bash
   # Install build tools
   pip install build

   # Build the package
   python -m build

   # Install the built package
   pip install dist/{project_name}-0.1.0-py3-none-any.whl
   ```

### Option 2: Installation with conda

1. **Development Installation**:
   ```bash
   # Create and activate conda environment
   conda create -n {project_name} python=3.11
   conda activate {project_name}

   # Install conda-build if not already installed
   conda install conda-build

   # Install in development mode
   pip install -e .
   ```

2. **Build and Install Locally**:
   ```bash
   # Build the conda package
   conda build .

   # Install the local package
   conda install --use-local {project_name}
   ```

3. **Installing Dependencies**:
   ```bash
   # Install development dependencies
   pip install -e ".[dev]"
   ```

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/{github_username}/{project_name}.git
   cd {project_name}
   ```

2. **Set up the development environment**:
   ```bash
   # Using pip
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   pip install -e ".[dev]"

   # OR using conda
   conda create -n {project_name} python=3.11
   conda activate {project_name}
   pip install -e ".[dev]"
   ```

3. **Run tests**:
   ```bash
   pytest
   ```

4. **Code formatting and linting**:
   ```bash
   # Format code
   black .
   
   # Sort imports
   isort .
   
   # Type checking
   mypy src
   ```

## Usage

```python
from {project_name} import CoreFeature

# Initialize the feature
feature = CoreFeature()

# Use the feature
result = feature.process(data)
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
├── pyproject.toml          # Project configuration
├── setup.cfg              # Setup configuration
├── meta.yaml             # Conda build configuration
├── README.md            # This file
└── CHANGELOG.md        # Version changelog
```

## Package Management

### Using pip

1. **Update version number**:
   - Edit `src/{project_name}/__init__.py`
   - Update `__version__ = "x.y.z"`

2. **Clean previous builds**:
   ```bash
   rm -rf dist/ build/ *.egg-info/
   ```

3. **Build new version**:
   ```bash
   python -m build
   ```

### Using conda

1. **Build conda package**:
   ```bash
   # Build package
   conda build .
   
   # Get build location
   conda build . --output
   ```

2. **Install locally**:
   ```bash
   conda install --use-local {project_name}
   ```

3. **Create conda environment file**:
   ```bash
   conda env export > environment.yml
   ```

## Documentation

- [API Documentation](docs/api.md)
- [Getting Started](docs/getting_started.md)
- [Examples](docs/examples.md)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- {author}

## Acknowledgments

- List any acknowledgments here
'''