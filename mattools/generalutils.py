import numpy as np

__all__ = ['mm']


def mm(arr):
    """Return (min, max) [for setting pyplot limits]"""
    return (np.min(arr), np.max(arr))