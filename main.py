#!/usr/bin/env python3
"""
Setup script to create a new Python library project structure.
Usage: python -m library_setup my_library_name
"""

import sys
import argparse
from pathlib import Path
from typing import Optional, Dict, Any

from .utils.file_ops import create_project_structure
from .utils.validation import validate_project_name
from .utils.user_input import get_user_input, UserInputError
from .config.default import get_default_config, update_config

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Create a new Python library project structure'
    )
    parser.add_argument(
        'project_name',
        help='Name of the project (use underscores for spaces)'
    )
    parser.add_argument(
        '--path',
        help='Base path for project creation (default: current directory)',
        default=None
    )
    parser.add_argument(
        '--full-readme',
        action='store_true',
        help='Generate a comprehensive README instead of the minimal version'
    )
    
    return parser.parse_args()

def setup_project(
    project_name: str,
    base_path: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None
) -> None:
    """
    Set up the project structure.
    
    Args:
        project_name: Name of the project
        base_path: Base path for project creation
        config: Custom configuration options
    """
    # Get default configuration
    project_config = get_default_config()
    
    # Update with custom config if provided
    if config:
        project_config = update_config(config)
    
    # Create project structure with configuration
    create_project_structure(project_name, base_path, project_config)

def main() -> None:
    """Main function to create the project structure."""
    try:
        # Parse command line arguments
        args = parse_args()
        
        # Validate project name
        validate_project_name(args.project_name)
        
        # Get user information
        print("\nWelcome to the Python Library Setup Tool!")
        print("Please provide some information about yourself.\n")
        
        username, email = get_user_input()
        
        # Update configuration with user information
        config = {
            'metadata': {
                'author': username,
                'author_email': email,
            },
            'template_config': {
                'readme': {
                    'default_style': 'full' if args.full_readme else 'minimal',
                }
            }
        }
        
        print(f"\nCreating project '{args.project_name}'...")
        
        # Create project structure
        setup_project(args.project_name, args.path, config)
        
        print(f"\nSuccessfully created project structure for {args.project_name}")
        print("\nNext steps:")
        print(f"1. cd {args.project_name}")
        print("2. python -m venv venv")
        print("3. source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
        print("4. pip install -e \".[dev]\"")
        print("\nHappy coding!")
        
    except UserInputError as e:
        print(f"\nError with user input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nError creating project structure: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()