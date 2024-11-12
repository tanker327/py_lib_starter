"""PyProject.toml template generator."""

from typing import Dict, Any

def get_pyproject_template(
    project_name: str,
    config: Dict[str, Any] = None
) -> str:
    """
    Generate the pyproject.toml template with user configuration.
    
    Args:
        project_name: Name of the project
        config: Configuration dictionary containing user settings
        
    Returns:
        Formatted pyproject.toml content
    """
    if config is None:
        config = {}
    
    # Get user information from config or use defaults
    metadata = config.get('metadata', {})
    author = metadata.get('author', 'Your Name')
    author_email = metadata.get('author_email', 'your.email@company.com')
    
    # Get Python version requirements
    python_version = config.get('python_version', {})
    min_python = python_version.get('min_version', '3.8')
    
    # Get code style settings
    code_style = config.get('code_style', {})
    line_length = code_style.get('line_length', 88)
    
    return f'''[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{project_name}"
version = "0.1.0"
description = "Internal library for common functionality across projects"
readme = "README.md"
requires-python = ">={min_python}"
license = "MIT"
authors = [
    {{name = "{author}", email = "{author_email}"}}
]
maintainers = [
    {{name = "{author}", email = "{author_email}"}}
]
keywords = [
    "internal",
    "library",
    "tools"
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: {min_python}",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Operating System :: OS Independent",
    "Typing :: Typed",
]
dependencies = []  # Keep empty by default, add specific dependencies as needed

[project.optional-dependencies]
# Development tools
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.1.0",
    "black>=22.0.0",
    "isort>=5.0.0",
    "mypy>=0.950",
    "pylint>=2.17.0",
    "pre-commit>=3.3.0",
]

# Example optional feature groups (commented out by default)
# http = [
#     "requests>=2.28.0",
#     "httpx>=0.24.0",
#     "aiohttp>=3.8.0",
# ]
# yaml = [
#     "pyyaml>=6.0",
# ]
# data = [
#     "pandas>=2.0.0",
#     "numpy>=1.24.0",
# ]
# all = [
#     "requests>=2.28.0",
#     "httpx>=0.24.0",
#     "aiohttp>=3.8.0",
#     "pyyaml>=6.0",
#     "pandas>=2.0.0",
#     "numpy>=1.24.0",
# ]

[project.urls]
"Homepage" = "https://github.com/username/{project_name}"
"Bug Tracker" = "https://github.com/username/{project_name}/issues"
"Documentation" = "https://github.com/username/{project_name}/docs"
"Source Code" = "https://github.com/username/{project_name}"

[tool.hatch.build.targets.wheel]
packages = ["src/{project_name}"]

[tool.black]
line-length = {line_length}
target-version = ['py38']
include = '\\.pyi?$'
extend-exclude = '''
# A regex preceded with ^/ will apply only to files and directories
# in the root of the project.
^/docs/
'''

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = {line_length}
known_first_party = ["{project_name}"]
known_third_party = ["pytest"]

[tool.mypy]
python_version = "{min_python}"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true
ignore_missing_imports = true

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q --cov={project_name} --cov-report=term-missing"
testpaths = [
    "tests",
]
pythonpath = [
  "src"
]
filterwarnings = [
    "error",
    "ignore::DeprecationWarning",
    "ignore::UserWarning",
]

[tool.coverage.run]
branch = true
source = ["src"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
]
ignore_errors = true
omit = [
    "tests/*",
    "setup.py",
]

[tool.pylint.messages_control]
disable = [
    "C0111",  # missing-docstring
    "C0103",  # invalid-name
    "C0330",  # bad-continuation
    "C0326",  # bad-whitespace
    "W0621",  # redefined-outer-name
    "W0108",  # unnecessary-lambda
    "R0903",  # too-few-public-methods
    "R0913",  # too-many-arguments
    "R0914",  # too-many-locals
]

[tool.pylint.format]
max-line-length = {line_length}

[tool.pylint.basic]
good-names = [
    "i",
    "j",
    "k",
    "ex",
    "Run",
    "_",
    "fp",
    "id",
]

[tool.ruff]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "C",  # flake8-comprehensions
    "B",  # flake8-bugbear
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
    "C901",  # too complex
]
target-version = "py38"
line-length = {line_length}

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.semantic_release]
version_variable = ["src/{project_name}/__init__.py:__version__"]
branch = "main"
upload_to_pypi = false
build_command = "python -m build"
'''