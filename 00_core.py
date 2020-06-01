# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# default_exp core

# %% [markdown]
# # Core module
#
# > First steps...

# %%
#hide
from nbdev.showdoc import *


# %%
#export

def double(x):
    """Doubles an input number

    >>> double(2)
    4
    """
    return x * 2


# %%
#export

def triple(x):
    """ Triples an input number
    
    >>> triple(3)
    9
    """
    return x * 3


# %%
double(3) + triple(4)


# %%
#export

def power(x, y):
    """ Raises x ** y
    
    > power(2, 3)
    8
    """
    return x ** y

# %%
#export

def sin(x):
    """ Computes the sin(x)

    >>> import math
    >>> sin(30 * math.pi / 180)
    0.5
    """
    import math
    return math.sin(x)


# %%
#export

def cos(q):
    """ Computes the cos(x)
    """
    import math
    return math.cos(q)


# %%
