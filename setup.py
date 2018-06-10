from cx_Freeze import setup, Executable
import os

base = None

executables = [Executable("Bot.py", base=base)]

packages = ["idna", "discord", "asyncio", "datetime"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

os.environ['TCL_LIBRARY'] = r'C:\Users\Martin\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Martin\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(
    name = "Robert",
    options = options,
    version = "1",
    description = 'countdown to bfa',
    executables = executables
)