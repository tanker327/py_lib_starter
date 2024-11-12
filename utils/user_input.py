"""User input utilities for collecting project information."""

import re
from typing import Optional, Tuple

class UserInputError(Exception):
    """Exception for user input validation errors."""
    pass

def validate_email(email: str) -> bool:
    """
    Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_pattern.match(email))

def validate_username(username: str) -> bool:
    """
    Validate username format.
    
    Args:
        username: Username to validate
        
    Returns:
        True if valid, False otherwise
    """
    # Username should be at least 2 characters long and contain only letters, numbers, spaces
    username_pattern = re.compile(r'^[a-zA-Z0-9 ]{2,}$')
    return bool(username_pattern.match(username))

def get_user_input() -> Tuple[str, str]:
    """
    Get and validate user input for name and email.
    
    Returns:
        Tuple of (username, email)
        
    Raises:
        UserInputError: If validation fails
    """
    username = input("Enter your name: ").strip()
    if not validate_username(username):
        raise UserInputError(
            "Invalid username. Username must be at least 2 characters long "
            "and contain only letters, numbers, and spaces."
        )

    email = input("Enter your email: ").strip()
    if not validate_email(email):
        raise UserInputError(
            "Invalid email address. Please enter a valid email address."
        )
    
    # Confirm information
    print("\nPlease confirm your information:")
    print(f"Name:  {username}")
    print(f"Email: {email}")
    
    confirm = input("\nIs this correct? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes']:
        raise UserInputError("User cancelled information confirmation")
    
    return username, email