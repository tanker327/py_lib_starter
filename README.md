# Python Library Setup Tool

A sophisticated command-line tool for generating standardized Python library project structures with modern best practices, comprehensive configurations, and development tools.

## Features

- 🎯 Interactive project setup with user information collection
- 📁 Standardized project structure generation
- ⚙️ Modern configuration with pyproject.toml
- 🐍 Virtual environment setup
- 🔧 Development tools integration (pytest, black, isort, mypy)
- 📝 Comprehensive documentation templates
- 🔒 Git initialization with hooks
- 🎨 Customizable project templates
- 🛠️ Modular and extensible architecture

## Project Structure

```
library_setup/
├── __init__.py
├── main.py              # Main script and CLI handling
├── templates/
│   ├── __init__.py
│   ├── pyproject.py     # pyproject.toml template
│   ├── setup_cfg.py     # setup.cfg template
│   ├── readme.py        # README.md template
│   ├── gitignore.py     # .gitignore template
│   ├── docs.py          # Documentation templates
│   ├── core.py         # Core module templates
│   ├── tests.py        # Test file templates
│   └── changelog.py    # CHANGELOG.md template
├── utils/
│   ├── __init__.py
│   ├── file_ops.py     # File operations
│   ├── validation.py   # Input validation
│   └── user_input.py   # User input handling
└── config/
    ├── __init__.py
    └── default.py      # Default configuration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tanker327/py_lib_starter.git
cd library-setup
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e .
```

## Usage

### Basic Usage

Create a new Python library project:
```bash
python -m library_setup my_project_name
```

The tool will:
1. Ask for your name and email
2. Create the project structure
3. Initialize git repository
4. Set up virtual environment
5. Configure development tools

### Command Line Options

```bash
python -m library_setup [OPTIONS] PROJECT_NAME

Options:
  --path PATH          Base path for project creation
  --full-readme        Generate comprehensive README
  -h, --help          Show help message
```

### Generated Project Structure

The tool creates a standardized project structure:

```
my_project/
├── src/
│   └── my_project/
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
├── scripts/            # Utility scripts
├── examples/           # Usage examples
├── pyproject.toml     # Project configuration
├── setup.cfg          # Setup configuration
├── README.md         # Project documentation
├── CHANGELOG.md      # Version changelog
└── .gitignore       # Git ignore rules
```

### Configuration

The tool uses a modular configuration system defined in `config/default.py`:

```python
# Custom configuration example
config = {
    'metadata': {
        'author': 'John Doe',
        'author_email': 'john@example.com',
    },
    'git_config': {
        'init_git': True,
        'git_hooks': {
            'pre-commit': [
                'black .',
                'isort .',
                'pytest',
            ],
        },
    },
    'venv_config': {
        'create_venv': True,
    },
}
```

### Development Tools

Generated projects include configuration for:

- **Code Formatting**: black, isort
- **Type Checking**: mypy
- **Testing**: pytest with coverage
- **Linting**: pylint, ruff
- **Git Hooks**: pre-commit hooks
- **Documentation**: Markdown templates

## Features in Detail

### 1. Project Templates

- **Modern Configuration**: Uses pyproject.toml with comprehensive settings
- **Type Hints**: All template code includes type hints
- **Documentation**: Ready-to-use documentation structure
- **Testing**: Pre-configured test suite with pytest

### 2. Development Workflow

- **Git Integration**: Automatic repository initialization
- **Virtual Environment**: Python environment setup
- **Development Tools**: Pre-configured development tools
- **Code Quality**: Integrated code quality tools

### 3. Project Structure

- **Source Layout**: Uses the `src/` layout for better packaging
- **Tests**: Separate test directory with examples
- **Documentation**: Comprehensive documentation structure
- **Scripts**: Directory for utility scripts

### 4. Customization

- **Templates**: Easily modify templates in the templates/ directory
- **Configuration**: Customize default settings in config/default.py
- **File Operations**: Extend file operations in utils/file_ops.py

## Best Practices Implemented

1. **Project Structure**:
   - src/ layout for better packaging
   - Separate test directory
   - Comprehensive documentation

2. **Development Tools**:
   - Modern code formatting
   - Type checking
   - Comprehensive testing
   - Automated quality checks

3. **Documentation**:
   - API documentation
   - Getting started guide
   - Usage examples
   - Change log

4. **Version Control**:
   - Git initialization
   - Pre-configured hooks
   - Comprehensive .gitignore

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests:
   ```bash
   pytest
   ```
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Permission Errors**:
   ```bash
   # Ensure you have write permissions
   chmod +x library_setup/main.py
   ```

2. **Import Errors**:
   ```bash
   # Install in development mode
   pip install -e .
   ```

3. **Git Initialization Fails**:
   ```bash
   # Ensure git is installed
   git --version
   ```

### Support

For issues and questions:
1. Check the [documentation](docs/)
2. Open an issue on GitHub
3. Contact the maintainers

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by modern Python packaging best practices
- Built with tools and patterns from the Python community
- Thanks to all contributors and users

