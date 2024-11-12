"""Setup.cfg template."""

from typing import Dict, Any

def get_setup_cfg_template(project_name: str, config: Dict[str, Any] = None) -> str:
    """
    Generate setup.cfg template with user configuration.
    
    Args:
        project_name: Name of the project
        config: Configuration dictionary containing user settings
        
    Returns:
        Formatted setup.cfg content
    """
    if config is None:
        config = {}
        
    return f"""[metadata]
name = {project_name}
# Additional setup.cfg content...
"""