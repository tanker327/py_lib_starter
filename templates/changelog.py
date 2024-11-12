"""Changelog template."""

from datetime import datetime

def get_changelog_template() -> str:
    """
    Get the CHANGELOG.md template.
    
    Returns:
        Changelog content
    """
    today = datetime.now().strftime("%Y-%m-%d")
    
    return f'''# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - {today}

### Added
- Initial release
- Basic project structure
- Core functionality
  - CoreFeature class
  - Basic data processing
- Utility functions
  - Logging setup
  - Input validation
- Exception hierarchy
- Documentation
  - API documentation
  - Getting started guide
  - Usage examples
'''