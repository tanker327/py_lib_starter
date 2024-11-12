"""File operation utilities for project creation."""

import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any, List
import logging

from ..templates import (
    get_pyproject_template,
    get_setup_cfg_template,
    get_readme_template,
    get_gitignore_template,
    get_core_templates,
    get_test_templates,
    get_doc_templates,
    get_changelog_template
)

# Configure logging
logger = logging.getLogger(__name__)

class FileOperationError(Exception):
    """Base exception for file operations."""
    pass

def create_directory(path: Path, mode: int = 0o755) -> None:
    """
    Create directory if it doesn't exist.
    
    Args:
        path: Directory path to create
        mode: Directory permissions (default: 0o755)
        
    Raises:
        FileOperationError: If directory creation fails
    """
    try:
        path.mkdir(parents=True, exist_ok=True)
        os.chmod(path, mode)
        logger.debug(f"Created directory: {path}")
    except Exception as e:
        raise FileOperationError(f"Failed to create directory {path}: {e}")

def write_file(path: Path, content: str, mode: int = 0o644) -> None:
    """
    Write content to a file.
    
    Args:
        path: File path to write to
        content: Content to write
        mode: File permissions (default: 0o644)
        
    Raises:
        FileOperationError: If file writing fails
    """
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        os.chmod(path, mode)
        logger.debug(f"Written file: {path}")
    except Exception as e:
        raise FileOperationError(f"Failed to write file {path}: {e}")

def initialize_git(project_path: Path, config: Dict[str, Any]) -> None:
    """
    Initialize git repository and create initial commit.
    
    Args:
        project_path: Path to project directory
        config: Project configuration
        
    Raises:
        FileOperationError: If git initialization fails
    """
    try:
        # Get git configuration
        git_config = config.get('git_config', {})
        init_git = git_config.get('init_git', True)
        
        if not init_git:
            logger.info("Skipping git initialization as per configuration")
            return
        
        # Initialize git repository
        subprocess.run(['git', 'init'], cwd=project_path, check=True)
        logger.info("Initialized git repository")
        
        # Configure git user if provided
        metadata = config.get('metadata', {})
        author_name = metadata.get('author')
        author_email = metadata.get('author_email')
        
        if author_name and author_email:
            subprocess.run(['git', 'config', 'user.name', author_name], cwd=project_path, check=True)
            subprocess.run(['git', 'config', 'user.email', author_email], cwd=project_path, check=True)
        
        # Initial commit
        subprocess.run(['git', 'add', '.'], cwd=project_path, check=True)
        subprocess.run(
            ['git', 'commit', '-m', 'Initial commit'],
            cwd=project_path,
            check=True,
            env={**os.environ, 'GIT_AUTHOR_NAME': author_name, 'GIT_AUTHOR_EMAIL': author_email}
        )
        
        # Set up pre-commit hooks if configured
        git_hooks = git_config.get('git_hooks', {})
        if git_hooks:
            setup_git_hooks(project_path, git_hooks)
            
        logger.info("Git repository initialized with initial commit")
        
    except subprocess.CalledProcessError as e:
        raise FileOperationError(f"Git operation failed: {e}")
    except Exception as e:
        raise FileOperationError(f"Failed to initialize git: {e}")

def setup_git_hooks(project_path: Path, hooks_config: Dict[str, List[str]]) -> None:
    """
    Set up git hooks based on configuration.
    
    Args:
        project_path: Path to project directory
        hooks_config: Hook configuration dictionary
        
    Raises:
        FileOperationError: If hook setup fails
    """
    hooks_dir = project_path / '.git' / 'hooks'
    
    try:
        for hook_name, commands in hooks_config.items():
            hook_path = hooks_dir / hook_name
            hook_content = "#!/bin/sh\n\n" + "\n".join(commands)
            
            write_file(hook_path, hook_content, mode=0o755)
            logger.debug(f"Created git hook: {hook_name}")
            
    except Exception as e:
        raise FileOperationError(f"Failed to set up git hooks: {e}")

def setup_virtual_environment(project_path: Path, python_version: str = None) -> None:
    """
    Set up virtual environment for the project.
    
    Args:
        project_path: Path to project directory
        python_version: Specific Python version to use (optional)
        
    Raises:
        FileOperationError: If venv creation fails
    """
    try:
        venv_path = project_path / 'venv'
        
        if python_version:
            subprocess.run(['python' + python_version, '-m', 'venv', 'venv'], cwd=project_path, check=True)
        else:
            subprocess.run(['python', '-m', 'venv', 'venv'], cwd=project_path, check=True)
            
        logger.info("Created virtual environment")
        
    except subprocess.CalledProcessError as e:
        raise FileOperationError(f"Failed to create virtual environment: {e}")

def create_project_structure(
    project_name: str,
    base_path: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None
) -> None:
    """
    Create the complete project structure.
    
    Args:
        project_name: Name of the project
        base_path: Base path for project creation
        config: Configuration options including user information
        
    Raises:
        FileOperationError: If project creation fails
    """
    try:
        # Set up base path
        if base_path is None:
            base_path = os.getcwd()
        base_path = Path(base_path) / project_name
        
        logger.info(f"Creating project structure at: {base_path}")
        
        # Create directory structure
        dirs = [
            'src',
            f'src/{project_name}',
            'tests',
            'docs',
            'scripts',
            'examples'
        ]
        
        for dir_path in dirs:
            create_directory(base_path / dir_path)
        
        # Create project files
        files_to_create = {
            'pyproject.toml': get_pyproject_template(project_name, config),
            'setup.cfg': get_setup_cfg_template(project_name, config),
            'README.md': get_readme_template(project_name, config),
            '.gitignore': get_gitignore_template(),
            'CHANGELOG.md': get_changelog_template(),
        }
        
        # Create core module files
        core_files = get_core_templates(project_name)
        for filename, content in core_files.items():
            files_to_create[f'src/{project_name}/{filename}'] = content
        
        # Create test files
        test_files = get_test_templates(project_name)
        for filename, content in test_files.items():
            files_to_create[f'tests/{filename}'] = content
        
        # Create documentation files
        doc_files = get_doc_templates(project_name)
        for filename, content in doc_files.items():
            files_to_create[f'docs/{filename}'] = content
        
        # Write all files
        for filepath, content in files_to_create.items():
            write_file(base_path / filepath, content)
        
        # Initialize git repository if configured
        if config and config.get('git_config', {}).get('init_git', True):
            initialize_git(base_path, config)
        
        # Set up virtual environment if configured
        if config and config.get('venv_config', {}).get('create_venv', True):
            python_version = config.get('python_version', {}).get('min_version')
            setup_virtual_environment(base_path, python_version)
            
        logger.info(f"Successfully created project structure for {project_name}")
        
    except Exception as e:
        logger.error(f"Failed to create project structure: {e}")
        # Clean up if project creation fails
        if base_path.exists():
            shutil.rmtree(base_path)
        raise FileOperationError(f"Failed to create project structure: {e}")

def validate_project_path(path: Path) -> None:
    """
    Validate project path.
    
    Args:
        path: Path to validate
        
    Raises:
        FileOperationError: If path validation fails
    """
    if path.exists() and any(path.iterdir()):
        raise FileOperationError(f"Directory {path} already exists and is not empty")
    
    try:
        # Test write permissions
        test_file = path / '.test_write_permission'
        path.mkdir(parents=True, exist_ok=True)
        test_file.touch()
        test_file.unlink()
    except Exception as e:
        raise FileOperationError(f"No write permission in directory {path}: {e}")

def cleanup_project_path(path: Path) -> None:
    """
    Clean up project path in case of failure.
    
    Args:
        path: Path to clean up
    """
    try:
        if path.exists():
            shutil.rmtree(path)
            logger.debug(f"Cleaned up directory: {path}")
    except Exception as e:
        logger.error(f"Failed to clean up directory {path}: {e}")