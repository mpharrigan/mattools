import pickle

__all__ = ['pload']


def pload(fn):
    with open(fn, 'rb') as f:
        return pickle.load(f)