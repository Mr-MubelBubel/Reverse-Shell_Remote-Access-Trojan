# Compile the 'client.py' with this file to execute it on systems without python3 installed.
# Install 'py -3.x -m pip install cx_Freeze' to compile the 'client.py' to an executable.
#!/usr/bin/python3

import sys, os
from unicodedata import name
from xml.etree.ElementInclude import include
from cx_Freeze import setup, Executable

# Dependencies and environment-settings
os.environ['TCL_LIBRARY'] = r'C:\Users\{User}\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\{User}\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

include_dlls = [r'C:\Users\{User}\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll', r'C:\Users\{User}\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll']

build_exe_options = {"packages": ["os", "socket", "subprocess", "sys", "tkinter"], "include_files": include_dlls}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name="revShell",
        version="1.0",
        description="GUI reverse Shell!",
        options={"build_exe": build_exe_options},
        executables=[Executable("revShell.py", base=base)])
