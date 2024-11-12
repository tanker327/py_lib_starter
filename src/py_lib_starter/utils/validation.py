"""Validation utilities for project creation."""

import re
from typing import Pattern

# Regex for valid Python package names
PACKAGE_NAME_PATTERN: Pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*$')

class ValidationError(Exception):
    """Base exception for validation errors."""
    pass

def validate_project_name(name: str) -> None:
    """
    Validate the project name.
    
    Args:
        name: The project name to validate
        
    Raises:
        ValidationError: If the project name is invalid
    """
    if not PACKAGE_NAME_PATTERN.match(name):
        raise ValidationError(
            "Project name must start with a letter and contain only "
            "letters, numbers, and underscores"
        )
    
    # Check reserved words
    import keyword
    if keyword.iskeyword(name):
        raise ValidationError(f"Project name '{name}' is a Python keyword")
    
    # Check length
    if len(name) < 2:
        raise ValidationError("Project name must be at least 2 characters long")
    if len(name) > 50:
        raise ValidationError("Project name must not exceed 50 characters")