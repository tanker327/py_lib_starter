"""Templates for project creation."""

from .pyproject import get_pyproject_template
from .setup_cfg import get_setup_cfg_template
from .readme import get_readme_template
from .gitignore import get_gitignore_template
from .core import get_core_templates
from .tests import get_test_templates
from .docs import get_doc_templates
from .changelog import get_changelog_template
from .license import get_license_template
from .conda_meta import get_conda_meta_template 

__all__ = [
    'get_pyproject_template',
    'get_setup_cfg_template',
    'get_readme_template',
    'get_gitignore_template',
    'get_core_templates',
    'get_test_templates',
    'get_doc_templates',
    'get_changelog_template',
    'get_conda_meta_template',
    'get_license_template',
]
