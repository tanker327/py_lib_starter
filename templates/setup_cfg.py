"""Setup.cfg template."""

def get_setup_cfg_template(project_name: str) -> str:
    """
    Get the setup.cfg template.
    
    Args:
        project_name: Name of the project
        
    Returns:
        Formatted setup.cfg content
    """
    return f'''[metadata]
name = {project_name}
version = 0.1.0
description = Internal library for common functionality across projects
long_description = file: README.md
long_description_content_type = text/markdown

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.8
install_requires =
    # Add your package dependencies here

[options.packages.find]
where = src

[options.extras_require]
dev =
    pytest>=7.0.0
    black>=22.0.0
    isort>=5.0.0
    mypy>=0.950
# Example optional dependencies (commented out by default)
# http =
#     requests>=2.28.0
# yaml =
#     pyyaml>=6.0
# data =
#     pandas>=1.3.0
#     numpy>=1.20.0
'''