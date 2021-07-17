# code from ---> pandas/core/common.py

from collections import abc

def _iterable_not_string(obj) -> bool:
    """
    Check if the object is an iterable but not a string.

    Parameters
    ----------
    obj : The object to check.

    Returns
    -------
    is_iter_not_string : bool
        Whether `obj` is a non-string iterable.

    Examples
    --------
    >>> _iterable_not_string([1, 2, 3])
    True
    >>> _iterable_not_string("foo")
    False
    >>> _iterable_not_string(1)
    False
    """
    return isinstance(obj, abc.Iterable) and not isinstance(obj, str)

def flatten(l):
    """
    Flatten an arbitrarily nested sequence.

    Parameters
    ----------
    l : sequence
        The non string sequence to flatten

    Notes
    -----
    This doesn't consider strings sequences.

    Returns
    -------
    flattened : generator
    """
    for el in l:
        if _iterable_not_string(el):
            for s in flatten(el):
                yield s
        else:
            yield el


in_data = [1,2,3,[4,[5,[6,[7]]]]]
flatten_data = list(flatten(in_data))
print(flatten_data)
