"""License template generator."""

from datetime import datetime
from typing import Dict, Any

def get_license_template(config: Dict[str, Any] = None) -> str:
    """
    Generate the MIT license template with user configuration.
    
    Args:
        config: Configuration dictionary containing user settings
        
    Returns:
        Formatted license content
    """
    if config is None:
        config = {}
    
    # Get user information from config or use defaults
    metadata = config.get('metadata', {})
    author = metadata.get('author', 'Your Name')
    current_year = datetime.now().year
    
    return f'''MIT License

Copyright (c) {current_year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''