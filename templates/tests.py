"""Test module templates."""

from typing import Dict

def get_test_templates(project_name: str) -> Dict[str, str]:
    """
    Get the test module templates.
    
    Args:
        project_name: Name of the project
        
    Returns:
        Dictionary of filename to content mappings
    """
    return {
        "__init__.py": "",  # Empty init file

        "test_core.py": f'''"""Tests for core functionality."""
import pytest
from {project_name}.core import CoreFeature
from {project_name}.exceptions import ValidationError

def test_core_feature_initialization():
    """Test CoreFeature initialization."""
    feature = CoreFeature()
    assert feature.config == {{}}
    
    config = {{"param": "value"}}
    feature = CoreFeature(config)
    assert feature.config == config

def test_core_feature_process():
    """Test CoreFeature process method."""
    feature = CoreFeature()
    test_data = [1, 2, 3]
    result = feature.process(test_data)
    assert isinstance(result, list)
''',

        "test_utils.py": f'''"""Tests for utility functions."""
import pytest
from {project_name}.utils import validate_input, setup_logging
from {project_name}.exceptions import ValidationError

def test_validate_input_with_valid_data():
    """Test validate_input with valid data."""
    valid_data = [1, 2, 3]
    assert validate_input(valid_data) is True

def test_validate_input_with_invalid_data():
    """Test validate_input with invalid data."""
    invalid_data = None
    with pytest.raises(ValidationError):
        validate_input(invalid_data)

def test_validate_input_with_non_list():
    """Test validate_input with non-list data."""
    invalid_data = "not a list"
    with pytest.raises(ValidationError):
        validate_input(invalid_data)

def test_setup_logging():
    """Test setup_logging configuration."""
    setup_logging(level="DEBUG")
    # Add assertions for logging configuration if needed
'''
    }