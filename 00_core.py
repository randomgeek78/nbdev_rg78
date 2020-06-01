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