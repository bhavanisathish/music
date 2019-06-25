# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:18:38 2019

@author: lenovA
"""

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Music",
        version = "0.1",
        description = "Music Player!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("music.py", base=base)])


