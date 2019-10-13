"""{{ cookiecutter.project_short_description }}"""

from ._meta import __author__, __copyright__, __email__, __home__
from ._version import __version__
from .lib import greet

__all__ = [
    '__author__',
    '__copyright__',
    '__email__',
    '__home__',
    '__version__',
    greet.__name__,
]
