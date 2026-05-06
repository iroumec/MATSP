"""
Package declaration for configuration utilities.
"""

from .builder import build_config
from .structures import Config

__all__ = [
    "Config",
    "build_config"
]