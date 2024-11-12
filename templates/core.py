"""Core module templates."""

from typing import Dict

def get_core_templates(project_name: str) -> Dict[str, str]:
    """
    Get the core module templates.
    
    Args:
        project_name: Name of the project
        
    Returns:
        Dictionary of filename to content mappings
    """
    return {
        "__init__.py": f'''"""
{project_name} - Internal library for common functionality across projects
"""

from .core import *
from .utils import *
from .exceptions import *

__version__ = "0.1.0"
''',

        "core.py": '''"""Core functionality of the library."""
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

        "utils.py": '''"""Utility functions for the library."""
from typing import Any, List
import logging
from .exceptions import ValidationError

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
        
    Raises:
        ValidationError: If data is None or not a list
    """
    if data is None:
        raise ValidationError("Input data cannot be None")
    if not isinstance(data, list):
        raise ValidationError("Input data must be a list")
    return True
''',

        "exceptions.py": '''"""Custom exceptions for the library."""

class LibraryError(Exception):
    """Base exception for the library."""
    pass

class ValidationError(LibraryError):
    """Raised when input validation fails."""
    pass

class ProcessingError(LibraryError):
    """Raised when processing fails."""
    pass
'''
    }