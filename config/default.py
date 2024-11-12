"""Default configuration for library setup."""

from typing import Dict, Any, List

# Project Structure
DEFAULT_DIRECTORIES: List[str] = [
    'src',
    'tests',
    'docs',
]

# Python Version Requirements
PYTHON_VERSION: Dict[str, str] = {
    'min_version': '3.9',
    'max_version': None,  # None means no upper limit
}

# Development Dependencies
DEV_DEPENDENCIES: Dict[str, str] = {
    'pytest': '>=7.0.0',
    'black': '>=22.0.0',
    'isort': '>=5.0.0',
    'mypy': '>=0.950',
}

# Optional Feature Groups
OPTIONAL_FEATURES: Dict[str, Dict[str, str]] = {
    'http': {
        'requests': '>=2.28.0',
    },
    'yaml': {
        'pyyaml': '>=6.0',
    },
    'data': {
        'pandas': '>=1.3.0',
        'numpy': '>=1.20.0',
    },
}

# File Templates Configuration
TEMPLATE_CONFIG: Dict[str, Any] = {
    'readme': {
        'default_style': 'minimal',  # or 'full'
        'include_license': True,
        'include_contributing': True,
    },
    'docs': {
        'format': 'markdown',  # or 'rst'
        'include_api_docs': True,
        'include_examples': True,
    },
    'tests': {
        'framework': 'pytest',
        'include_fixtures': True,
        'include_conftest': True,
    },
}

# Project Metadata
DEFAULT_METADATA: Dict[str, Any] = {
    'author': 'Your Name',
    'author_email': 'your.email@company.com',
    'license': 'MIT',
    'keywords': [],
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        f'Programming Language :: Python :: {PYTHON_VERSION["min_version"]}',
        'Operating System :: OS Independent',
    ],
}

# Code Style Settings
CODE_STYLE: Dict[str, Any] = {
    'line_length': 88,
    'target_python_version': PYTHON_VERSION["min_version"],
    'isort_profile': 'black',
}

# Testing Configuration
TEST_CONFIG: Dict[str, Any] = {
    'test_dir': 'tests',
    'pytest_options': [
        '-v',
        '--tb=short',
        '--strict-markers',
    ],
    'coverage_options': {
        'source': ['src'],
        'omit': ['tests/*', 'setup.py'],
        'min_coverage': 80,
    },
}

# Documentation Settings
DOC_CONFIG: Dict[str, Any] = {
    'doc_dir': 'docs',
    'doc_format': 'markdown',
    'sections': [
        'api',
        'getting_started',
        'examples',
    ],
}

# Git Configuration
GIT_CONFIG: Dict[str, Any] = {
    'init_git': True,
    'create_gitignore': True,
    'initial_branch': 'main',
    'git_hooks': {
        'pre-commit': [
            'black .',
            'isort .',
            'mypy src',
            'pytest',
        ],
    },
}

# Logging Configuration
LOG_CONFIG: Dict[str, Any] = {
    'default_level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'date_format': '%Y-%m-%d %H:%M:%S',
}

# Build Configuration
BUILD_CONFIG: Dict[str, Any] = {
    'build_backend': 'hatchling',
    'requires': ['hatchling'],
    'include_package_data': True,
    'zip_safe': False,
}

# Template Files
REQUIRED_FILES: List[str] = [
    'pyproject.toml',
    'setup.cfg',
    'README.md',
    '.gitignore',
    'CHANGELOG.md',
]

# Source Files
REQUIRED_SOURCE_FILES: List[str] = [
    '__init__.py',
    'core.py',
    'utils.py',
    'exceptions.py',
]

# Default Project URLs
PROJECT_URLS: Dict[str, str] = {
    'Bug Tracker': '',
    'Documentation': '',
    'Source Code': '',
}

def get_default_config() -> Dict[str, Any]:
    """
    Get the complete default configuration.
    
    Returns:
        Dictionary containing all default configuration settings
    """
    return {
        'directories': DEFAULT_DIRECTORIES,
        'python_version': PYTHON_VERSION,
        'dev_dependencies': DEV_DEPENDENCIES,
        'optional_features': OPTIONAL_FEATURES,
        'template_config': TEMPLATE_CONFIG,
        'metadata': DEFAULT_METADATA,
        'code_style': CODE_STYLE,
        'test_config': TEST_CONFIG,
        'doc_config': DOC_CONFIG,
        'git_config': GIT_CONFIG,
        'log_config': LOG_CONFIG,
        'build_config': BUILD_CONFIG,
        'required_files': REQUIRED_FILES,
        'required_source_files': REQUIRED_SOURCE_FILES,
        'project_urls': PROJECT_URLS,
    }

def update_config(custom_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update default configuration with custom settings.
    
    Args:
        custom_config: Custom configuration to override defaults
        
    Returns:
        Updated configuration dictionary
    """
    config = get_default_config()
    
    def deep_update(original: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively update nested dictionaries."""
        for key, value in update.items():
            if (
                key in original 
                and isinstance(original[key], dict) 
                and isinstance(value, dict)
            ):
                deep_update(original[key], value)
            else:
                original[key] = value
        return original
    
    return deep_update(config, custom_config)

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate configuration settings.
    
    Args:
        config: Configuration to validate
        
    Returns:
        True if valid, raises ValueError if invalid
    """
    # Add validation logic here
    required_keys = [
        'directories',
        'python_version',
        'dev_dependencies',
        'required_files',
    ]
    
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration key: {key}")
    
    return True