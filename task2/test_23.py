#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:09:22 2018

@author: jingyiwang

Goal:read input.txt and check that the number of unicode characters in the file is 6.
"""
import io

def countCharacter(fileName):
    f = io.open(fileName,"r",encoding="utf-8")
    line = f.readline().rstrip('\n')
    return len(line)

def test_countCharacter():
    assert countCharacter('task2/input.txt') == 6
