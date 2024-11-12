"""Conda meta.yaml template generator."""

from typing import Dict, Any

def get_conda_meta_template(
    project_name: str,
    config: Dict[str, Any] = None
) -> str:
    """
    Generate the conda meta.yaml template with user configuration.
    
    Args:
        project_name: Name of the project
        config: Configuration dictionary containing user settings
        
    Returns:
        Formatted meta.yaml content
    """
    if config is None:
        config = {}
    
    # Get user information from config or use defaults
    metadata = config.get('metadata', {})
    author = metadata.get('author', 'Your Name')
    author_email = metadata.get('author_email', 'your.email@company.com')
    github_username = metadata.get('github_username', 'your-github-username')
    
    # Get Python version requirements
    python_version = config.get('python_version', {})
    min_python = python_version.get('min_version', '3.8')
    
    return f'''package:
  name: {project_name}
  version: "0.1.0"

source:
  path: .

build:
  number: 0
  noarch: python
  script: "{{{{ PYTHON }}}} -m pip install . -vv"

requirements:
  host:
    - python >={min_python}
    - pip
    - setuptools
    - hatchling
  run:
    - python >={min_python}
    # Add your runtime dependencies here as needed:
    # - numpy
    # - pandas

# test:
#   requires:
#     - pytest
#   imports:
#     - {project_name}
#   commands:
#     - pytest

about:
  home: https://github.com/{github_username}/{project_name}
  license: MIT
  license_family: MIT
  license_file: LICENSE
  summary: A brief description of the Python package
  description: |
    A longer description of your package that can span
    multiple lines and provide more details about its
    functionality and purpose.
  doc_url: https://github.com/{github_username}/{project_name}
  dev_url: https://github.com/{github_username}/{project_name}

extra:
  recipe-maintainers:
    - {github_username}
  maintainers:
    - {author} <{author_email}>
'''