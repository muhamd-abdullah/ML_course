# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    a = tx.T.dot(tx)
    b = tx.T.dot(y)
    return np.linalg.solve(a, b)
    '''
    Using simple equations (derivative of squared loss = 0), we found an expression that minimize the loss:
    -> xT.x . w = xT.y
    -> w = (xT.x)^-1 . xT.y

    Now,
    - np.linalg.solve(a, b) --> solves: a.w = b --> returns 'w' i-e a^-1.b
    - np.linalg.solve(xT.x , xT.y) --> solves: xT.x . w = xT.y --> returns 'w'
    '''
