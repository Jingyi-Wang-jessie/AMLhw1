from __future__ import division
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:23:43 2018

@author: jingyiwang

Goal: test if two divided eight is 0.25, using built-in functions and numpy array.
"""

import numpy as np
import numpy.testing as npt

def builtin_divide(x1,x2):
    return x1/x2

def numpy_divide(x1,x2):
    return np.array([x1/x2])

def test_builtin():
    assert builtin_divide(2,8) == 0.25
    
def test_numpy():
    npt.assert_array_equal(numpy_divide(2,8),np.array([0.25]))
