import pickle

__all__ = ['pload']


def pload(fn):
    """Load from a filename real quick

    Side note: why doesn't pickle define this function for me??
    """
    with open(fn, 'rb') as f:
        return pickle.load(f)