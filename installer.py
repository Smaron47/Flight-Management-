import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': ['tkinter','sqlite3','datetime','tkcalendar','reportlab','PIL'],
        'include_files': ['flights.db','bg.png','images.ico']
    }
}


executables = [Executable('main.py', base=base,icon="images.ico")]

setup(name='Lets Fly',
      version='1.2',
      description='no description',
      options=options,
      executables=executables)
