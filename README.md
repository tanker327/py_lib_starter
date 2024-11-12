# py lib starter

A powerful command-line tool for generating standardized Python library project structures. This tool helps you create well-organized Python packages with modern best practices, complete configuration files, and development tools setup.

## Features

- 🎯 Interactive project setup with user information collection
- 📁 Modern project structure with src-layout
- ⚙️ Comprehensive configuration files (pyproject.toml, setup.cfg)
- 🐍 Support for both pip and conda package management
- 🔧 Pre-configured development tools (pytest, black, isort, mypy)
- 📝 Auto-generated documentation templates
- 🔒 License file generation
- 🎨 Git initialization and configuration

## Installation

### Using pip

```bash
# Clone the repository
git clone https://github.com/yourusername/py_lib_starter.git
cd py_lib_starter

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Using conda

```bash
# Clone the repository
git clone https://github.com/yourusername/py_lib_starter.git
cd py_lib_starter

# Create and activate conda environment
conda create -n py_lib_starter python=3.11
conda activate py_lib_starter

# Install conda-build (if you plan to build conda packages)
conda install conda-build

# Install in development mode
pip install -e .
```

## Usage

### Creating a New Project

```bash
# Basic usage
create-pylib my_new_project

# The tool will interactively ask for:
# - Your name
# - Your email
# - Your GitHub username
```

### Generated Project Structure

```
my_new_project/
├── src/
│   └── my_new_project/
│       ├── __init__.py      # Package initialization
│       ├── core.py          # Core functionality
│       ├── utils.py         # Utility functions
│       └── exceptions.py    # Custom exceptions
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # Pytest configuration
│   └── test_core.py        # Basic tests
├── docs/
│   ├── api.md
│   ├── getting_started.md
│   └── examples.md
├── pyproject.toml          # Project configuration
├── setup.cfg              # Setup configuration
├── meta.yaml             # Conda build configuration
├── LICENSE              # MIT License
├── README.md           # Project documentation
└── CHANGELOG.md       # Version changelog
```

## Building Generated Projects

### Using pip

```bash
cd my_new_project

# Install in development mode
pip install -e ".[dev]"

# Build distribution files
python -m build

# Install from wheel
pip install dist/my_new_project-0.1.0-py3-none-any.whl
```

### Using conda

```bash
cd my_new_project

# Build conda package
conda build .

# Install locally
conda install --use-local my_new_project
```

## Development Tools

Generated projects come with:

- **Testing**: pytest with coverage reporting
- **Code Formatting**: black, isort
- **Type Checking**: mypy
- **Linting**: pylint, ruff
- **Documentation**: Markdown templates
- **Version Control**: Git initialization

## Configuration Files

### pyproject.toml
- Modern Python packaging configuration
- Development dependencies
- Tool configurations (black, isort, mypy)

### meta.yaml
- Conda build configuration
- Package metadata
- Build and test requirements

### setup.cfg
- Package configuration
- Tool settings
- Compatibility options

## Project Templates

The tool includes templates for:
- Core package structure
- Test files
- Documentation
- Configuration files
- License (MIT)
- Git configuration

## Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## Troubleshooting

### Common Issues

1. **Package Not Found**
   ```bash
   # Make sure you're in the right directory and the package is installed
   pip install -e .
   ```

2. **Conda Build Fails**
   ```bash
   # Ensure conda-build is installed
   conda install conda-build
   
   # Check if all required files exist
   ls LICENSE meta.yaml
   ```

3. **Test Failures**
   ```bash
   # Install development dependencies
   pip install -e ".[dev]"
   
   # Run tests to verify
   pytest
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by modern Python packaging best practices
- Built with tools from the Python ecosystem
- Structured following community standards