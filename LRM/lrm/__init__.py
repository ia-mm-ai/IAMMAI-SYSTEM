"""A local relevance workspace, independent of actor and source authority."""

from .model import LRMError
from .store import Workspace

__all__ = ["LRMError", "Workspace"]
__version__ = "0.2.0"
