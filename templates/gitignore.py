"""Gitignore template."""

def get_gitignore_template() -> str:
    """
    Get the .gitignore template.
    
    Returns:
        Gitignore content
    """
    return '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/
.coverage.*
coverage.xml
*.cover

# Distribution
dist/
build/
*.egg-info/

# Documentation
docs/_build/

# Jupyter Notebook
.ipynb_checkpoints

# Environment variables
.env
.venv

# mypy
.mypy_cache/
.dmypy.json
dmypy.json
'''