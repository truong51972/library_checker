import os
from package.sqlQuery import initializeData

os.system('python.exe -m pip install --upgrade pip')

try:
    import pyqt5
except:
    print('hahaha')
    os.system('pip install pyqt5')

initializeData()