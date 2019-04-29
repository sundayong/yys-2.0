# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 22:41:09 2018
frozen dir
@author: yanhua
"""
import sys
import os


def app_path():
    """Returns the base application path."""
    print(sys.executable)
    if hasattr(sys, 'yyy-2.0'):
        # Handles PyInstaller
        print(1)
        return os.path.dirname(sys.executable)
    print(2)

print(app_path())