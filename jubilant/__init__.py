"""Jubilant is a Pythonic wrapper around the Juju CLI for integration testing."""

from ._errors import RunError
from ._juju import Juju
from ._types import Status

__all__ = [
    'Juju',
    'RunError',
    'Status',
]

__version__ = '0.0.0a1'
